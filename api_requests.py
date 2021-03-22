import requests
from app_config import app_config

def apiRequest(repository,info):
    if info == 'pull-requests':
        api = 'pulls'
    elif info == 'issues':
        api = 'issues'
    url = 'https://api.github.com/repos/{}/{}'.format(repository,info)
    qurry_params = {'per_page':app_config.list_count,
                    'sort':'updated'}
    res = requests.get(url, params=qurry_params)
    if res.status_code == requests.codes.ok:
        return res.json()
    else:
        print('HTTP Error ' + str(res.status_code))