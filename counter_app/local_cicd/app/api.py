from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import URL
import os


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = URL.create(
    "mysql+pymysql",
    username=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    database=os.getenv("MYSQL_DATABASE"),
    port=os.getenv("MYSQL_PORT")
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)


class CounterModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    counter_name = db.Column(db.String(16), unique=True)
    counter_value = db.Column(db.Integer)


class CounterApi(Resource):
    def get(self):
        counter = get_counter_by_name("counter")
        if counter is None:
            counter = CounterModel(counter_name="counter", counter_value=0)
            db.session.add(counter)
            db.session.commit()
        return counter.counter_value

    def put(self):
        counter = get_counter_by_name("counter")
        if counter is None:
            counter = CounterModel(counter_name="counter", counter_value=0)
            db.session.add(counter)
            db.session.commit()
        counter.counter_value += 1
        db.session.commit()
        return counter.counter_value

def get_counter_by_name(counter_name):
  return CounterModel.query.filter_by(counter_name=counter_name).first()

api.add_resource(CounterApi, '/counter')

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)

