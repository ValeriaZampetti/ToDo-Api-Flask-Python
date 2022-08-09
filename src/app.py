from flask import Flask, jsonify
from flask import request
import json


app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
]

@app.route('/todos', methods=['GET'])
def todo_list():
    json_todo_list = jsonify(todos)
    return json_todo_list, 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    json_todo_list = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_todo_list, 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos 
    new_todos=list(filter(lambda todo: todos.index(todo) != position, todos))
    todos=new_todos


    print("This is the position to delete: ",position)
    return jsonify(todos), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
