from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rd

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
API_KEY = "topSecretApiKey"


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in
                self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record

@app.route("/random")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    cafe = rd.choice(cafes)
    return jsonify(cafe=cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    cafes_to_dict = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=cafes_to_dict)


@app.route("/search")
def search():
    location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter(Cafe.location == location)
    cafes_to_dict = [cafe.to_dict() for cafe in cafes]
    if len(cafes_to_dict) == 0:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."})
    return jsonify(cafes=cafes_to_dict)


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe()
    new_cafe.name = request.form.get("name")
    new_cafe.img_url = request.form.get("img_url")
    new_cafe.map_url = request.form.get("map_url")
    new_cafe.location = request.form.get("location")
    new_cafe.has_sockets = bool(request.form.get("has_sockets"))
    new_cafe.has_toilet = bool(request.form.get("has_toilet"))
    new_cafe.has_wifi = bool(request.form.get("has_wifi"))
    new_cafe.can_take_calls = bool(request.form.get("can_take_calls"))
    new_cafe.seats = request.form.get("seats")
    new_cafe.coffee_price = request.form.get("coffee_price")
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    new_price = request.form.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe is None:
        return jsonify(response={
            "Not found": "Sorry a cafe with that id was not found in the database."}), 404
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."}), 200


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key != API_KEY:
        return jsonify(
            response={"error": "You don't have permissions to do this."}), 403
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe is None:
        return jsonify(
            response={"error": "Doesn't exist a cafe with the given id."}), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully deleted the cafe."}), 200


if __name__ == '__main__':
    app.run(debug=True)
