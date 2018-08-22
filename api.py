import todo
import requests
import apiError
resp = todo.add_task("Take out trash")
if resp.status_code != 201:
    raise Exception('Cannot create task: {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))

resp = todo.get_tasks()
if resp.status_code != 200:
    raise Exception('Cannot fetch all tasks: {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))