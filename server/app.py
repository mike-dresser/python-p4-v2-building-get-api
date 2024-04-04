# server/app.py

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"

# start building your API here
@app.route('/games')
def games():
    all_games = Game.query.all()
    games = []
    for game in all_games:
        games.append(game.to_dict())
    response = make_response(
        jsonify(games),
        200,
        {"content-type": "application/json"}
    )
    return response


@app.route('/games/<int:id>')
def game_by_id(id):
    game_obj = Game.query.filter_by(id=id).first()
    if game_obj:
        return make_response(game_obj.to_dict(), 200)
    else:
        return make_response({"error": f'No game with id {id} found'}, 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

