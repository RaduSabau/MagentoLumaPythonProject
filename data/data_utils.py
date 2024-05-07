import json


def read_users_json():
    f = open('../data/users-fixture.json')
    data = json.load(f)
    return data
