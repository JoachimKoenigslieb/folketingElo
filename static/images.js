function getLeft() {
	return document.getElementsByClassName('left')[0]
}

function getRight() {
	return document.getElementsByClassName('right')[0]
}

function requestMatchup() {
	fetch('./get-matchup', {method: 'POST', headers: {'Content-Type': 'application/json'}})
		.then(resp => resp.json())
			.then(resp => {
				leftImg = resp[0]
				rightImg = resp[1]

				left = getLeft()
				left.setAttribute('src', leftImg)
				
				right = getRight()
				right.setAttribute('src', rightImg)
			})
}

function getLeaderboard() {
	fetch('./leaderboard', {method: 'POST', headers: {'Content-Type': 'application/json'}})
		.then(resp => resp.json())
			.then(resp => {
				console.log(resp)
				listTop = document.getElementsByClassName("topN")[0]
				listTop.innerHTML = '<h1>Hotteste</h1>'

				for (i=0; i < resp.N; i++){
					listTop.innerHTML += `<img src="${resp.top[i]}" class="leaderboardImg">`
				}

				listBot = document.getElementsByClassName('botN')[0]
				listBot.innerHTML = '<h1>Notteste</h1>'

				for (i=0; i < resp.N; i++){
					listBot.innerHTML += `<img src="${resp.bottom[i]}" class="leaderboardImg">`
				}
			})

}

function vote(e) {
	target = (e.target.getAttribute('src'))

	left = getLeft()
	right = getRight()

	fetch('./vote', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({'target': target, 'right':right.getAttribute('src'), 'left': left.getAttribute('src') })})

	requestMatchup()
}

function registerEvents() {
	left = document.getElementsByClassName('left')[0]
	right = document.getElementsByClassName('right')[0]

	left.addEventListener("click", vote)
	right.addEventListener("click", vote)
}