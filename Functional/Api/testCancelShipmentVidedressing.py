import requests, json, unittest, ConfigParser, re, conftest, pytest


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


    def testCancelShipmentWithExistentIdParameter(self):
        req = open('./requests/de/cancelShipment/cancelShipmentWithExistentIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.delete(url, headers=headers)
        assert r.status_code == 200
        assert r.text == ''

    def testCancelShipmentWithCanceledOrder(self):
        req = open('./requests/de/cancelShipment/cancelShipmentWithCanceledOrder.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.delete(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}
        if r.text != '':
            error_dict = r.json()
        assert ('messages' in error_dict)

    def testCancelShipmentWithExistentIdParameterFromOtherClient(self):
        req = open('./requests/de/cancelShipment/cancelShipmentWithExistentIdParameterFromOtherClient.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.delete(url, headers=headers)
        print r.text, r.status_code

if __name__ == '__main__':
    unittest.main()
