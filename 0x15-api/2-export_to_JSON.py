#!/usr/bin/python3
"""task 2"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    fname = argv[1] + ".json"
    todos = []
    api_url = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])
    api_t = "https://jsonplaceholder.typicode.com/todos"
    resp_t = requests.get(api_t, params={"userId": argv[1]}).json()
    resp_u = requests.get(api_url).json()
    idd = argv[1]
    for item in resp_t:
        list_t = {}
        list_t["task"] = item.get('title')
        list_t["completed"] = item.get('completed')
        list_t["username"] = resp_u.get('username')
        todos.append(list_t)
    dictionary = {}
    dictionary[idd] = todos
    with open(fname, 'w+') as f:
        json.dump(dictionary, f)
