import requests

def post(user_name, first_name, user_id):
    res_post = requests.post(f'https://petstore.swagger.io/v2/user',
                             headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                             data='{  '
                                  f'"id": {user_id},  '
                                  f'"username": "{user_name}",  '
                                  f'"firstName": "{first_name}",  '
                                  '"lastName": "string",  '
                                  '"email": "string",  '
                                  '"password": "string",  '
                                  '"phone": "string", '
                                  '"userStatus": 0}')
    requests_status_post = res_post.status_code
    result_post = ""
    if 'application/json' in res_post.headers['Content-Type']:
        result_post = res_post.json()
    else:
        result_post = res_post.text
    print(f'\npost https://petstore.swagger.io/v2/user')
    print(requests_status_post)
    print(result_post)

def get(user_name):
    res_get = requests.get( f"https://petstore.swagger.io/v2/user/{user_name}", headers = {'accept': 'application/json'})
    requests_status_get = res_get.status_code
    result_get = ""
    if 'application/json' in res_get.headers['Content-Type']:
        result_get = res_get.json()
    else:
        result_get = res_get.text
    print(f'\nget https://petstore.swagger.io/v2/user/{user_name}')
    print(requests_status_get)
    print(result_get)

def put(user_name, new_first_name, user_id):
    res_put = requests.put(f'https://petstore.swagger.io/v2/user/{user_name}',
                           headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                           data='{ '
                                f'"id": {user_id},  '
                                f'"username": "{user_name}",  '
                                f'"firstName": "{new_first_name}",  '
                                '"lastName": "string",  '
                                '"email": "string",  '
                                '"password": "string",  '
                                '"phone": "string",  '
                                '"userStatus": 0}')
    requests_status_put = res_put.status_code
    result_put = ""
    if 'application/json' in res_put.headers['Content-Type']:
        result_put = res_put.json()
    else:
        result_put = res_put.text
    print(f'\nput https://petstore.swagger.io/v2/user/{user_name}')
    print(requests_status_put)
    print(result_put)

def delete(user_name):
    res_delete = requests.delete(f'https://petstore.swagger.io/v2/user/{user_name}',
                                 headers={'accept': 'application/json'})
    requests_status_delete = res_delete.status_code
    result_delete = ""
    if 'application/json' in res_delete.headers['Content-Type']:
        result_delete = res_delete.json()
    else:
        result_delete = res_delete.text
    print(f'\ndelete https://petstore.swagger.io/v2/user/{user_name}')
    print(requests_status_delete)
    print(result_delete)

status='available'
username='qqq'
firstName='Olga'
new_firstName='Olga2'
userid=345

post(username, firstName, userid)
get(username)
put(username, new_firstName, userid)
get(username)
delete(username)
get(username)
