import requests, json, ConfigParser, pytest
import update_request_files as dateUpdate

def setup_module(module):
    print 'Updating dates in requests ...'
    dateUpdate.updateDates()


class TestServices():

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


    """-----------------NEGATIVE TEST CASES-----------------------------------"""

    def testCreateOrderWithoutRequiredParameter(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutRequiredParameter.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyRequiredParameter(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyRequiredParameter.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400

        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert ('messages' in error_dict)
        #self.failIf(not('messages' in error_dict), "No messages list found in response.\nResponse: %s" % r.text)

    def testCreateOrderWithInvalidCollectionDate(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithInvalidCollectionDate.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert ('messages' in error_dict)
        #self.failIf(not('messages' in error_dict), "No messages list found in response.\nResponse: %s" % r.text)


    def testCreateOrderWithInvalidParameterValueSpeChars(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithInvalidParameterValueSpeChars.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert ('messages' in error_dict)

    def _testCreateOrderDropoffServiceWithoutRequiredParameter(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderDropoffServiceWithoutRequiredParameter.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        print url
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert ('messages' in error_dict)

    # def _testCreateOrderDropoffServiceWithEmptyRequiredParameter(self):
    #     headers = {'Authorization': '%s' % self.key}
    #     req = open('./requests/de/createOrder/createOrderDropoffServiceWithEmptyRequiredParameter.request', 'r')
    #     data = json.load(req)
    #     url = "%s%s" % (self.baseUrl, '/v1/orders')
    #     print url
    #     r = requests.post(url, data=data, headers=headers)
    #     self.fail("Missing implementation")

    # def _testCreateOrderDropoffServiceWithInvalidParameterValue(self):
    #     headers = {'Authorization': '%s' % self.key}
    #     req = open('./requests/de/createOrder/createOrderDropoffServiceWithInvalidParameterValue.request', 'r')
    #     data = json.load(req)
    #     url = "%s%s" % (self.baseUrl, '/v1/orders')
    #     print url
    #     r = requests.post(url, None, data, headers=headers)
    #     self.fail("Missing implementation")

    # def _testCreateOrderDropoffServiceWithInvalidParameterValueSpeChars(self):
    #     headers = {'Authorization': '%s' % self.key}
    #     req = open('./requests/de/createOrder/createOrderDropoffServiceWithInvalidParameterValueSpeChars.request', 'r')
    #     data = json.load(req)
    #     url = "%s%s" % (self.baseUrl, '/v1/orders')
    #     print url
    #     r = requests.post(url, None, data, headers=headers)
    #     self.fail("Missing implementation")

    """-----------------HAPPY PATH------------------------------------"""

    def testCreateOrderWithOneShipment(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithOneShipment.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()
        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)

        shipments = response['shipments']
        assert (len(shipments) == 1)

        receipt_url = "%s" % shipments[0]['receipt']
        r = requests.get(receipt_url, headers=headers)

    def testCreateOrderWithOneShipmentAndInsurance(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithOneShipmentAndInsurance.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201

        response = {}
        if r.text != '':
            response = r.json()
        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)

        shipments = response['shipments']
        assert (len(shipments) == 1)


    def testCreateOrderWithMultipleShipments(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithMultipleShipments.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        print r.text
        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)
        shipments = response['shipments']
        assert (len(shipments) == 4)


    # def _testCreateOrderDropoffServiceWithMultipleShipments(self):
    #     headers = {'Authorization': '%s' % self.key}
    #     req = open('./requests/de/createOrder/createOrderDropoffServiceWithMultipleShipments.request', 'r')
    #     data = json.load(req)
    #     url = "%s%s" % (self.baseUrl, '/v1/orders')
    #     print url
    #     r = requests.post(url, None, data, headers=headers)
    #     self.fail("Missing implementation")

    # def _testCreateOrderDropoffServiceWithOneShipment(self):
    #     headers = {'Authorization': '%s' % self.key}
    #     req = open('./requests/de/createOrder/createOrderDropoffServiceWithOneShipment.request', 'r')
    #     data = json.load(req)
    #     url = "%s%s" % (self.baseUrl, '/v1/orders')
    #     print url
    #     r = requests.post(url, None, data, headers=headers)
    #     self.fail("Missing implementation")


    """CREATE ORDER REQUIRED FIELDS VALIDATIONS"""
    def testCreateOrderWithoutOrderCustomReference(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutOrderCustomReference.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()
        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)

    def testCreateOrderWithoutShipmentCustomReference(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutShipmentCustomReference.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()
        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)

    def testCreateOrderWithoutFromName(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromName.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert 'messages' in error_dict

    def testCreateOrderWithWrongPackageSize(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithWrongPackageSize.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert 'messages' in error_dict

    def testCreateOrderWithoutFromSurname(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromSurname.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert 'messages' in error_dict


    def testCreateOrderWithoutFromCompany(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromCompany.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)


    def testCreateOrderWithoutFromStreet1(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromStreet1.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert 'messages' in error_dict

    def testCreateOrderWithoutFromStreet2(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromStreet2.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)

    def testCreateOrderWithoutFromZipCode(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromZipCode.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutFromCity(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromCity.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutFromPhone(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromPhone.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutFromEmail(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutFromEmail.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}

        if r.text != '':
            response = r.json()

        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)

    #TO
    def testCreateOrderWithoutToName(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToName.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400

        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutToSurname(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToSurname.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutToCompany(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToCompany.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}
        if r.text != '':
            response = r.json()

        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)


    def testCreateOrderWithoutToStreet1(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToStreet1.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutToStreet2(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToStreet2.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}

        if r.text != '':
            response = r.json()

        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)

    def testCreateOrderWithoutToZipCode(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToZipCode.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert (r.status_code == 400)
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    def testCreateOrderWithoutToCity(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToCity.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutToPhone(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToPhone.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutToEmail(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutToEmail.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 201
        response = {}

        if r.text != '':
            response = r.json()

        assert ('order_reference' in response)
        assert ('shipments' in response)
        assert ('total_amount' in response)

    def testCreateOrderWithoutCollectionDate(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutCollectionDate.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutCollectionTime(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutCollectionTime.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert  r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutContent(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutContent.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithoutContentValue(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutContentValue.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    def testCreateOrderWithoutInsuranceAmount(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithoutInsuranceAmount.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    """EMPTY FIELDS VALIDATIONS"""
    def testCreateOrderWithEmptyOrderCustomReference(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyOrderCustomReference.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyShipmentCustomReference(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyShipmentCustomReference.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyFromName(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromName.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyFromSurname(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromSurname.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    def testCreateOrderWithEmptyFromCompany(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromCompany.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyFromStreet1(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromStreet1.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyFromStreet2(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromStreet2.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyFromZipCode(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromZipCode.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    def testCreateOrderWithEmptyFromCity(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromCity.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyFromPhone(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromPhone.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyFromEmail(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyFromEmail.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    #TO
    def testCreateOrderWithEmptyToName(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToName.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyToSurname(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToSurname.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyToCompany(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToCompany.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert  r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyToStreet1(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToStreet1.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyToStreet2(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToStreet2.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyToZipCode(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToZipCode.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyToCity(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToCity.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert  r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyToPhone(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToPhone.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyToEmail(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyToEmail.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyCollectionDate(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyCollectionDate.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyCollectionTime(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyCollectionTime.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyContent(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyContent.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testCreateOrderWithEmptyContentValue(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyContentValue.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    def testCreateOrderWithEmptyInsuranceAmount(self):
        headers = {'Authorization': '%s' % self.key}
        req = open('./requests/de/createOrder/createOrderWithEmptyInsuranceAmount.request', 'r')
        data = json.load(req)
        url = "%s%s" % (self.baseUrl, '/v1/orders')
        r = requests.post(url, None, data, headers=headers)
        assert  r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict
