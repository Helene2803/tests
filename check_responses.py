import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'
PATH_400 = 'yd-disk:/temp_folder'
PATH_404 = 'disk:////////'

token = os.getenv('TOKEN')
headers = {'Authorization': f'OAuth {token}'}
params_400 = {'path': PATH_400}
params_404 = {'path': PATH_404}

response_400 = requests.get(BASE_URL, headers=headers, params=params_400)
print(response_400.status_code)

response_404 = requests.get(BASE_URL, headers=headers, params=params_404)
print(response_404.status_code)

