from flask import Flask, render_template, request, url_for, redirect

from dotenv import load_dotenv
import os
from configpymongo.pymongo import mongo
from tasks.routes import todo_task
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo.init_app(app)


app.register_blueprint(todo_task, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True, port=4000)