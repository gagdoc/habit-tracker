import requests
from datetime import date

USERNAME = "gagdoc"
TOKEN = "hueowkdncoie2323oj"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

get_graph_endpoint = f"{graph_endpoint}/{GRAPHID}"

today = date.today()
today_str = today.strftime('%Y%m%d')

print(today_str)
get_graph_config = {
    "id": GRAPHID,
    "date": today_str,
    "quantity": "10"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=get_graph_endpoint, json=get_graph_config, headers=headers)

print(response.text)
