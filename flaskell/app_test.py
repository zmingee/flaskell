import unittest
import requests
import json


url = "http://0.0.0.0:5000/api"
headers = {'content-type': 'application/json'}
class FlaskAppTestCases(unittest.TestCase):

    def setUp(self):
        print("setup testcase")
        #self.mongo_client = MongoClient('localhost', 27017)
        #self.mongo_db = self.mongo_client.security_api

    def tearDown(self):
        print("teardown testcase")
        #self.mongo_client.close(


    def test_json_rpc_endpoint(self):
        print("test_single_subnet_address_scan")
        payload = {
            "method": "Security.scan_spam_dbs",
            "params": {"ips": "8.36.45.128/25"},
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers).json()
        import pprint; pprint.pprint(response)