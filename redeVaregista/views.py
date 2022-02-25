from django.shortcuts import render
import requests
from mockapi.models import MockApiResponse
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

    new_caskback = MockApiResponse.objects.create(
        document=content_payload['document'],
        createdAt=content_payload['createdAt'],
        cashback=content_payload['cashback'],
        message=content_payload['message'],
        id_legacy=content_payload['id']
    )

    new_caskback.save()

    return payload.status_code, content_payload
