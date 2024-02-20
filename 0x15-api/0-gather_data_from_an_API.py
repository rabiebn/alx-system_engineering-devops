#!/usr/bin/python3
"""
Gather's data from the API (https://jsonplaceholder.typicode.com/)
"""

import json
import requests
from sys import argv


def fetch_todo(emp_id):
    """ fetch's todo data """

    todo_list = []
    if (emp_id is None):
        return todo_list

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(emp_id))
    todo_list = json.loads(resp.text)

    return todo_list


def count_task(list):
    """count_task"""

    done_tasks = []
    done = 0
    for i in list:
        if i['completed']:
            done += 1
            done_tasks.append(i['title'])
    emp_tasks = {
        'NUMBER_OF_DONE_TASKS': done,
        'TOTAL_NUMBER_OF_TASKS': len(list),
        'TASK_TITLE': done_tasks
    }
    return emp_tasks


def get_name(emp_id):
    """get_name"""

    if (emp_id is None):
        return ''

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users?id={}'.format(emp_id))

    user_list = json.loads(resp.text)
    return user_list[0]['name']


if __name__ == '__main__':
    tasks = fetch_todo(argv[1])
    emp_tasks = count_task(tasks)
    print('Employee {} is done with tasks({}/{}):'.format(
        get_name(argv[1]), emp_tasks['NUMBER_OF_DONE_TASKS'],
        emp_tasks['TOTAL_NUMBER_OF_TASKS']
    ))
    for t in emp_tasks['TASK_TITLE']:
        print('\t {}'.format(t))
