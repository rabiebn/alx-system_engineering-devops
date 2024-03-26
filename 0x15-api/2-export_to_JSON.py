#!/usr/bin/python3
"""
Module exports data in the JSON format.
"""
import json
import requests


url = "https://jsonplaceholder.typicode.com/"


def fetch_emp_todo(emp_id):
    """fetchs employee's todo list"""
    req = requests.get(url + "todos?userId={}".format(emp_id))
    return req.json()


def fetch_emp_username(emp_id):
    """Fetchs employee's user name"""
    req = requests.get(url + 'users/{}'.format(emp_id))
    return req.json().get('username')


if __name__ == '__main__':
    from sys import argv

    emp_id = int(argv[1])
    emp_todos = fetch_emp_todo(emp_id)
    emp_username = fetch_emp_username(emp_id)
    file = '{}.json'.format(emp_id)

    todos_emp = {}
    tasks = []
    for task in emp_todos:
        if task.get('userId') == emp_id:
            task_dict = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": emp_username
                    }
            tasks.append(task_dict)
        todos_emp[str(emp_id)] = tasks

    with open(file, mode="w") as emp_file:
        json.dump(todos_emp, emp_file)
