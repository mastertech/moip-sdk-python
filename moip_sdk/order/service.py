import json

import requests

from moip_sdk import MOIP_API_URL
from moip_sdk.authorization.headers import headers
from moip_sdk.order.schemas import OrderSchema


def register_order(data):
    order_payload = OrderSchema().dumps(data)

    result = requests.post(f'{MOIP_API_URL}/orders/',
                           data=order_payload,
                           headers=headers)

    result = result.content.decode('utf-8')
    return json.loads(result)


def get_order(order):
    result = requests.get(f'{MOIP_API_URL}/orders/{order}',
                          headers=headers)

    result = result.content.decode('utf-8')
    return json.loads(result)


def get_orders_by_email(email):
    result = requests.get(f'{MOIP_API_URL}/orders?q={email}',
                          headers=headers)

    result = result.content.decode('utf-8')
    return json.loads(result)
