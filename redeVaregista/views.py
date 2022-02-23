from django.shortcuts import render
import requests

# Create your views here.


def make_request(request_data):
    url = 'https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback'

    data_content = {
        'document': request_data['cpf'],
        'cashback': request_data['cashback']
    }

    try:
        payload = requests.post(url, json=data_content)
    except Exception as err:
        print(f'EXCEPTION: {err}')
        payload = requests.post(url, data=data_content)

    if payload.status_code in (200, 201):
        content_payload = payload.json()
    else:
        content_payload = {}

    return payload.status_code, content_payload
