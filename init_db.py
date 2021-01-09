#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:59:28 2021

@author: joachim
"""


import glob
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

db = SessionLocal() #this might be stupid. Should i load i each time like in fastapi? Idk. databases are hard to get right

for file in glob.glob('./static/*.jpg'):
    picture = models.Picture(elo = 800, image_path = file, )
    db.add(picture)

db.commit()