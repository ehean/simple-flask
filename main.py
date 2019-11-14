from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

todos = {}
people = {
        "erik": {
            "age": 28,
            "weight": 180,
            "height": 172
        },
        "priyanka": {
            "age": 25,
            "weight": 120,
            "height": 154
        }
    }

app = Flask(__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('name')


class HelloWorld(Resource):
    def get(self):
        return { "msg": "Hello world" }


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class PersonApi(Resource):
    def get(self):
        args = parser.parse_args(strict=True)
        print(args)
        if "name" in args:
            if args["name"] in people:
                return jsonify(people[args["name"]])
        return "{}"
           
api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/todo/<string:todo_id>')
api.add_resource(PersonApi, '/person')
app.run(debug=True)


