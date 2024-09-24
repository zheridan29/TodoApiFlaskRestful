from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'Install requirements.txt'},
    'todo2': {'task': 'Install requirements.txt'},
    'todo3': {'task': 'Install requirements.txt'}
}

parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):
    def get(self, todo_id):
        return TODOS[todo_id], 200
    
    def delete(self, todo_id):
        del TODOS[todo_id]
        return '', 204
    
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
    
class TodoList(Resource):
    def get(self):
        return TODOS
    
    def post():
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201
    
# This is a comment.
if __name__ == '__main__':
    app.run(debug=True)
    