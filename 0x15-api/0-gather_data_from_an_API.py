#!/usr/bin/python3
"""
Module returns information about his/her TODO list progress,
for a given employee ID.
"""
import requests


url = "https://jsonplaceholder.typicode.com/"


def fetch_emp_todo(emp_id):
    """fetchs employee's todo list"""
    req = requests.get(url + "todos?userId={}".format(emp_id))
    return req.json()


def fetch_emp_info(emp_id):
    """Fetchs employee's info"""
    req = requests.get(url + 'users/{}'.format(emp_id))
    return req.json()


def done_tasks(emp_todos):
    """Returns a list of done tasks"""
    done = []
    for task in emp_todos:
        if task['completed']:
            done.append(task)
    return done


if __name__ == '__main__':
    from sys import argv

    emp_todos = fetch_emp_todo(int(argv[1]))
    emp_info = fetch_emp_info(int(argv[1]))
    done = done_tasks(emp_todos)

    print("Employee {} is done with tasks({}/{}):".format(
        emp_info['name'],
        len(done),
        len(emp_todos)
    ))
    for task in done:
        print("\t {}".format(task['title']))
