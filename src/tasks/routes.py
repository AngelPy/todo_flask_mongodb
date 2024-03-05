from flask import request, Blueprint, jsonify, Blueprint, render_template, redirect, url_for, session
from configpymongo.pymongo import mongo
from bson.objectid import ObjectId

todo_task = Blueprint('todo_task', __name__)

@todo_task.route("/create", methods=['GET', 'POST'])
def insert_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        completed = request.form['completed']

        response_ = mongo.db.todos.insert_one({
            'title': title,
            'description': description,
            'completed': completed
        })
        return redirect('/')
    return render_template('createform.html')

@todo_task.route("/")
def get_tasks():
    
    all_todos = mongo.db.todos.find()
    return render_template('index.html', todos = all_todos)

@todo_task.post("/<id>/delete/")
def delete_task(id):
    mongo.db.todos.delete_one({"_id": ObjectId(id)})
    return redirect('/')

@todo_task.route("/<id>/update/", methods=['GET', 'POST'])
def update_task(id):

    todo = mongo.db.todos.find_one({'_id':ObjectId(id)})

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        completed = request.form['completed']

        response_ = mongo.db.todos.update_one({'_id': ObjectId(id)}, {'$set': {
            'title': title,
            'description': description,
            'completed': completed
        }})
        return redirect('/')
    return render_template('updateform.html', todos = todo)

@todo_task.route("/login", methods=['GET', 'POST'])
def login():

    return render_template('login.html')

@todo_task.route("/register", methods=['GET', 'POST'])
def register():

    return render_template('register.html')