import sys
sys.path += ['src/main']
import unittest
from model import Config, Endpoint, Url

class TestEndpoint(unittest.TestCase):

    def test_decode_from(self):
        expected_endpoint = EndpointFixtures.get_endpoint()
        returned_endpoint = Endpoint.decode_from(EndpointFixtures.get_parsed_json())

        self.assertEqual(returned_endpoint.name, expected_endpoint.name)
        self.assertEqual(returned_endpoint.description, expected_endpoint.description)
        self.assertEqual(returned_endpoint.url, expected_endpoint.url)
        self.assertEqual(returned_endpoint.expected_status, expected_endpoint.expected_status)
        self.assertEqual(returned_endpoint.expected_content_type, expected_endpoint.expected_content_type)
        self.assertEqual(returned_endpoint.filters, expected_endpoint.filters)

    def test_decode_pagination_function_from_default(self):
        parsed_json = 'default'

        expected_function = lambda url, page: "{}?page={}".format(url, page)
        returned_function = Endpoint.decode_pagination_function_from(parsed_json)

        expected_result = expected_function('https://buyee.jp/item/search/category/2084019025', 2)
        returned_result = returned_function('https://buyee.jp/item/search/category/2084019025', 2)

        self.assertEqual(returned_result, expected_result)

    def test_decode_pagination_function_from_failure(self):
        parsed_json = 'other'
        with self.assertRaises(ValueError):
            Endpoint.decode_pagination_function_from(parsed_json)

class TestConfig(unittest.TestCase):

    def test_decode_from(self):
        parsed_json = {
            'endpoints': [
                EndpointFixtures.get_parsed_json()
            ]
        }
        config = Config.decode_from(parsed_json)
        self.assertEqual(len(config.endpoints), 1)

class EndpointFixtures:

    @staticmethod
    def get_parsed_json():
        parsed_json = {
            'name': 'Ibanez guitars on Yahoo Auctions',
            'description': 'Yahoo! JAPAN Auction ＞ Hobbies & Crafts ＞ Musical Instruments ＞ Guitars ＞ Electric Guitars ＞ Main Units ＞ Ibanez',
            'url': 'https://buyee.jp/item/search/category/2084019025',
            'pagination': 'default',
            'expected_status': [
                200
            ],
            'expected_content_type': [
                'text/html'
            ],
            'filters': [
                'rg2770z',
                'rga121',
                'rga321',
                'rgt220'
            ]
        }
        return parsed_json

    @staticmethod
    def get_endpoint():
        endpoint = Endpoint(
            name = 'Ibanez guitars on Yahoo Auctions',
            description = 'Yahoo! JAPAN Auction ＞ Hobbies & Crafts ＞ Musical Instruments ＞ Guitars ＞ Electric Guitars ＞ Main Units ＞ Ibanez',
            url = Url('https://buyee.jp/item/search/category/2084019025'),
            pagination_function = lambda url, page: "{}?page={}".format(url, page),
            expected_status = [
                200
            ],
            expected_content_type = [
                'text/html'
            ],
            filters = [
                'rg2770z',
                'rga121',
                'rga321',
                'rgt220'
            ]
        )
        return endpoint

if __name__ == '__main__':
    unittest.main()
