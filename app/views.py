from flask import Blueprint, request, jsonify
from .tasks import add_together, celery

main = Blueprint('main', __name__)


@main.route('/add', methods=['POST'])
def add():
    a = request.json.get('a')
    b = request.json.get('b')
    task = add_together.apply_async(args=[a, b])
    return jsonify({'task_id': task.id}), 202


@main.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    from celery.result import AsyncResult
    task = AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'result': None
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'result': task.result
        }
    else:
        response = {
            'state': task.state,
            'result': str(task.info),  # this is the exception raised
        }
    return jsonify(response)


@main.route('/schedule', methods=['POST'])
def schedule_task():
    data = request.json
    task_name = data.get('task_name')
    interval = data.get('interval')
    a = data.get('a')
    b = data.get('b')

    # Add a periodic task
    celery.add_periodic_task(
        interval,
        add_together.s(a, b),
        name=task_name,
        options={'expires': 3600}
    )
    return jsonify({'message': 'Task scheduled'}), 201


@main.route('/remove_schedule', methods=['POST'])
def remove_schedule():
    data = request.json
    task_name = data.get('task_name')

    # Remove the periodic task
    celery.control.revoke(task_name)
    return jsonify({'message': 'Task removed'}), 200
