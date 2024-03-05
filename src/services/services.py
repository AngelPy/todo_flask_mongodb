"""
from flask import request, Blueprint, jsonify, Blueprint, render_template, redirect, url_for
from configpymongo.pymongo import mongo
from bson.objectid import ObjectId

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
        return redirect(url_for('index'))
    return render_template('createform.html')

def get_tasks():
    
    all_todos = mongo.db.todos.find()
    return render_template('index.html', todos = all_todos)

def delete_task(id):
    mongo.db.todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))
"""