from flask import Flask, request, jsonify
import functools, json

app = Flask(__name__)

listofmovies = []
class MovieInfo:
	def __init__(self, name, start, end):
		self.name = name
		self.start = start
		self.end = end

@app.route('/get_max_profit_API', methods = ['GET'])
def get_max_profit_API():
	def compareEnds(movieA, movieB):
		return movieA.end - movieB.end

	jsonInfo = request.json
	moviesList = []
	for key, value in jsonInfo.items():
		temp = MovieInfo(jsonInfo[key]["name"], int(jsonInfo[key]["start"]), int(jsonInfo[key]["end"]))
		moviesList.append(temp)

	sortedByEnd = sorted(moviesList, key = functools.cmp_to_key(compareEnds))

	pickedMovies = []
	j = 0
	count = 0
	for i in range(1, len(sortedByEnd)):
		if (sortedByEnd[i].start > sortedByEnd[j].end):
			pickedMovies.append(sortedByEnd[j].name)
			count = count + 1
			j = i
	pickedMovies.append(sortedByEnd[j].name)
	count = count + 1
	j = 0
	return jsonify(Movies = pickedMovies, MaxProfit = count)


if (__name__ == "__main__"):
	app.run(debug = True)
