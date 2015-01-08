import requests, json, unittest, ConfigParser, re, conftest, pytest
import update_request_files as dateUpdate

def setup_module(module):
    print 'Updating dates in requests ...'
    dateUpdate.updateDates()


class TestServicesVidedressing():

    @pytest.fixture(autouse=True)
    def loadConfigInfo(self, testenv):
        config = ConfigParser.RawConfigParser()
        config.read('conf/main.cfg')

        if testenv == 'DEV':
            self.baseUrl = config.get('api_hosts', 'DEV_ENVIRONMENT_URL')
            self.key = config.get('api_credentials', 'DEV_API_KEY_DEV')

        if testenv == 'INT':
            self.baseUrl = config.get('api_hosts', 'TEST_ENVIRONMENT_URL')
            self.key = config.get('api_credentials', 'DEV_API_KEY')

        if testenv == 'VIDEDRESSING':
            self.baseUrl = config.get('api_hosts', 'TEST_ENVIRONMENT_URL')
            self.key = config.get('api_credentials', 'VIDEDRESSING_API_KEY')


    def testCreateOrderVidedressingWithService5601(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5601.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 1)


    def testCreateOrderVidedressingWithService5701(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5701.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        print response
        assert (len(shipments) == 1)


    def testCreateOrderVidedressingWithService5801(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5801.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 1)


    def testCreateOrderVidedressingWithService5601MultiShipment(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5601MultiShipment.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 2)


    def testCreateOrderVidedressingWithService5601MultiPackage(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5601MultiPackage.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 1)


    def testCreateOrderVidedressingWithService5701MultiShipment(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5701MultiShipment.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 2)


    def testCreateOrderVidedressingWithService5801MultiShipment(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5801MultiShipment.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 2)


    def testCreateOrderVidedressingWithService5701MultiPackage(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5701MultiPackage.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 1)



    def testCreateOrderVidedressingWithService5801MultiPackage(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithService5801MultiPackage.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 1)


    def testCreateOrderVidedressingWithEmptyCollectionDate(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithEmptyCollectionDate.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        response = {}
        if r.text != '':
            response = r.json()

        assert 'messages' in response


    def testCreateOrderVidedressingWithInvalidCollectionDate(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithInvalidCollectionDate.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        response = {}
        if r.text != '':
            response = r.json()

        assert 'messages' in response


    def testCreateOrderVidedressingWithoutCollectionDate(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderVidedressingWithoutCollectionDate.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert any('order_reference' in item for item in response)
        assert any('shipments' in item for item in response)
        assert any('insurance_coverage_amount' in item for item in response['shipments'])
        assert any('receipt' in item for item in response['shipments'])
        assert any('shipment_custom_reference' in item for item in response['shipments'])
        assert any('shipment_reference' in item for item in response['shipments'])
        assert any('status' in item for item in response['shipments'])
        assert any('total_price' in item for item in response['shipments'])
        assert any('total_amount' in item for item in response)

        shipments = response['shipments']
        assert (len(shipments) == 1)