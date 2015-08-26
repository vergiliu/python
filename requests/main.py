# http://flask-restful.readthedocs.org/en/latest/quickstart.html
# https://pypi.python.org/pypi/rom

from flask import Flask, jsonify, abort, request

app = Flask(__name__)
VERSION='1.0'
MAIN_PATH='/todo/api/v{}/'.format(VERSION)
# DELETE	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Delete a task

tasks = {'hello': 'world', 'buy': ['bread', 'eggs'], 'sell': 'old car',
         'do': ['bank errands', 'meet with Joe']
         }


@app.route(MAIN_PATH + 'tasks')
def get_all_tasks():
    # GET	http://[hostname]/todo/api/v1.0/tasks	Retrieve list of tasks
    return jsonify(tasks)


@app.route(MAIN_PATH + 'tasks', methods=['POST'])
def add_new_task():
    # POST	http://[hostname]/todo/api/v1.0/tasks	Create a new task
    if not request.json:
        abort(400)
    else:
        tasks[request.json['title']] = request.json['content']
        return jsonify(ok='200')


@app.route(MAIN_PATH + 'tasks/<task_name>', methods=['PUT'])
def update_a_task(task_name):
    if not request.json:
        tasks[task_name] = request.json['content']
    else:
        abort(400)


@app.route(MAIN_PATH + 'tasks/<task_id>')
def get_a_task(task_id):
    # GET	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Retrieve a task
    if task_id in tasks:
        return jsonify(task=tasks[task_id])
    else:
        return jsonify(error=404)

if __name__ == '__main__':
    app.run(debug=True)
