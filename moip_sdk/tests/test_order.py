import random
import unittest

from moip_sdk.customer.schemas import CustomerSchema
from moip_sdk.customer.service import register_customer
from moip_sdk.order.schemas import OrderSchema
from moip_sdk.order.service import get_order, get_orders_by_email, register_order


class OrderTestCase(unittest.TestCase):
    def setUp(self):
        customer_payload = {
            'ownId': random.randint(900000, 90000000),
            'fullname': 'João da Silva Teste',
            'email': 'joao.teste@mastertech.com.br',
            'birthDate': '2000-02-02',
            'taxDocument': {
                'type': 'CPF',
                'number': '55237990096'
            },
            'phone': {
                'countryCode': '55',
                'areaCode': '11',
                'number': '40028922'
            },
            'shippingAddress': {
                'city': 'Santa Catarina',
                'zipCode': '88132241',
                'street': 'Rua Bréscia',
                'streetNumber': '12',
                'state': 'SC',
                'country': 'Brazil',
                'district': 'Passa Vinte'
            }
        }

        self.customer = CustomerSchema().load(customer_payload)
        registered_customer = register_customer(self.customer)

        order_payload = {
            'ownId': random.randint(900000, 90000000),
            'amount': {
                'currency': 'BRL'
            },
            'items': [{
                'product': 'Curso Mastertech',
                'quantity': 1,
                'detail': 'Este é um teste para venda de um produto',
                'price': 40000,
            }],
            'customer': {
                'id': registered_customer['id']
            }
        }

        self.order = OrderSchema().load(order_payload)
        self.registered_order = register_order(self.order)

    def test_register_order(self):
        self.order['own_id'] = random.randint(900000, 90000000)
        response = register_order(self.order)

        self.assertIsNotNone(response['id'])
        self.assertEqual(len(response), 17)

    def test_get_order_by_id(self):
        response = get_order(self.registered_order['id'])

        self.assertIsNotNone(response['id'])
        self.assertEqual(len(response), 17)

    def test_get_order_with_invalid_id(self):
        response = get_order('ORD-GR')

        self.assertIsNotNone(response['error'])
        self.assertEqual(response['error'], 'resource not found')


if __name__ == '__main__':
    unittest.main()
