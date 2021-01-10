from dotenv import load_dotenv
from flask import Flask, send_file, request, render_template, jsonify
import random
import json
import glob


import models
from database import SessionLocal, engine

load_dotenv()

app = Flask(__name__)

models.Base.metadata.create_all(bind=engine)
db = SessionLocal() #this might be stupid. Should i load i each time like in fastapi? Idk. databases are hard to get right

def calc_matchup(elo_A, elo_B, winner):
    expected_A, expected_B = 1/(1 + 10**((elo_B - elo_A)/400)), 1/(1 + 10**((elo_A - elo_B)/400))
    
    print(f'expected A: {expected_A} expected_B {expected_B}')
    
    w,k = 1, 16
    score_A, score_B = w if winner == 0 else 0, w if winner == 1 else 0
    delta_A, delta_B = k * (score_A - expected_A), k * (score_B - expected_B)
    
    print(f'elo deltas: {delta_A}, {delta_B}')
    
    return elo_A+delta_A, elo_B+delta_B

def extract_name(pic):
    return ' '.join([name.replace('ae', 'æ').replace('oe','ø').title() for name in pic.image_path.split('.')[-2].split('/')[-1].split('-')])
    
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/get-matchup', methods = ['POST', 'GET'])
def get_matchup():
    files = glob.glob('./static/*.jpg')
    return json.dumps(random.sample(files, k=2))

@app.route('/leaderboard', methods = ['POST', 'GET'])
def leaderboard():
    if request.method == 'GET':
        return render_template('leaderboard.html')
    elif request.method == 'POST':
        pictures = db.query(models.Picture).all()
        
        N=3
        sorted_names = sorted([pic for pic in pictures], key = lambda pic: pic.elo, reverse=True)
        top_N = sorted_names[:N]
        bottom_N = sorted_names[-N:]
    
        top_N_names = [pic.image_path for pic in top_N]
        bottom_N_names = [pic.image_path for pic in bottom_N]

        response = json.dumps({'top': top_N_names, 'bottom': bottom_N_names, 'N': N})
        print(response)
        return response
    
@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    voted, left, right = data['target'], data['left'], data['right']

    left_img, right_img = db.query(models.Picture).filter_by(image_path = left).first(), db.query(models.Picture).filter_by(image_path = right).first()

    winner_bool = 0 if left == voted else 1
    new_elo_left, new_elo_right = calc_matchup(left_img.elo, right_img.elo, winner_bool)

    left_img.elo = new_elo_left
    right_img.elo = new_elo_right
    
    if winner_bool == 0:
        left_img.voted += 1
    elif winner_bool == 1:
        right_img.voted += 1
    
    print(left_img.voted, right_img.voted)
    
    db.commit()
    return 'ok'




