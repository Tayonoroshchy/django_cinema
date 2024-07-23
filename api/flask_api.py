from unittest import result

from flask import Flask, request, jsonify


app = Flask('movies_service')


@app.route('/api/movies', methods=['GET'], strict_slashes=False)
def get_movies_list() -> str:

    return jsonify(result)


@app.route('/api/movies/<movie_id>', methods=['GET'])
def get_movie_detail(movie_id: str) -> str:

    return jsonify(result)


if __name__ == '__flask_api__':
    app.run(host='127.0.0.1', port=8000, debug=True)
