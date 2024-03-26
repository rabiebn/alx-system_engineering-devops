#!/usr/bin/python3
"""
Module exports data in the CSV format.
"""
import csv
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
    file = '{}.csv'.format(emp_id)

    tasks = []
    for task in emp_todos:
        tasks.append([emp_id, emp_username,
                      task.get('completed'), task.get('title')])

    with open(file, mode='w') as emp_file:
        emp_writer = csv.writer(emp_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in tasks:
            emp_writer.writerow(task)
