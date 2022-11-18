import requests
from os.path import join


def login(url, username, password):
    login_json = {"username": username, "password": password}
    login_resp = requests.post(url='/'.join([url, 'api/auth/login']),
                               json=login_json)
    cookies = login_resp.cookies
    return cookies


def get_tasks(url, cookies):
    params = {'page_size': 100}
    data = requests.get(url='/'.join([url, 'api/tasks']),
                        cookies=cookies,
                        params=params)
    data = data.json()
    return data


def test_api():
    import requests
    import json

    url = 'http://192.168.50.205:8080/projects?page=1'
    # url = 'https://app.cvat.ai/api/jobs'
    response = requests.get(url)
    Text = response.text
    print('issPositionText:')
    print(response.content)
    issPositionJsonDoc = json.loads(response.content)

    fileName = 'issPosition.json'
    with open(fileName, 'w', encoding='utf-8') as jsonFile:
        json.dump(issPositionJsonDoc, jsonFile, ensure_ascii=False)
        jsonFile.flush()
    pass


if __name__ == '__main__':
    # parameters
    url = 'http://192.168.50.205:8080'
    username = 'admin'
    password = 'a1s2d3f4'

    # login
    cookies = login(url, username, password)

    # get_tasks
    data = get_tasks(url, cookies)
    for v in data['results']:
        task_id = v['id']
        task_name = v['name']
        state = v['segments'][0]['jobs'][0]['state']
        if state == 'completed':
            r = requests.get(
                url='/'.join([url, f'api/tasks/{task_id}/annotations/']),
                cookies=cookies,
                params={
                    'action': 'download',
                    'format': 'Datumaro 1.0'
                },
                stream=True
            )
            with open(f'{task_id}_annotations.zip', 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
