import requests, data
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Замените следующие значения своими данными


# Инициализация OAuth2-клиента
client = BackendApplicationClient(client_id=data.client_id)
oauth = OAuth2Session(client=client)

# Получение Access Token
token = oauth.fetch_token(token_url=data.token_url, auth=HTTPBasicAuth(data.client_id, data.client_secret))

# Вывод Access Token
print(token)
