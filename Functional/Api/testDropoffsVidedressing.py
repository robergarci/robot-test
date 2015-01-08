import requests, json, unittest, ConfigParser, re, conftest, pytest

class TestDropoffsVidedressing():

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

    def testGetDropoffVidedressingWithService5701(self):
        req = open('./requests/de/dropoffs/dropoffsVidedressingService5701.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}

        try:
            r = requests.get(url, headers=headers, timeout=20)
        except requests.exceptions.Timeout:
            pytest.fail("Request timeout. Request: %s" % url)


        response = {}
        if r.text != '':
            response = r.json()
            if type(response) == type({}):
                assert 'messages' not in response.keys

        assert any('commerce_name' in item for item in response)
        assert any('city' in item for item in response)
        assert any('opening_times' in item for item in response)
        assert any('zip' in item for item in response)
        assert any('country' in item for item in response)
        assert any('long' in item for item in response)
        assert any('phone' in item for item in response)
        assert any('state' in item for item in response)
        assert any('address' in item for item in response)
        assert any('lat' in item for item in response)
        assert any('type' in item for item in response)
        assert any('id' in item for item in response)


    def testGetDropoffVidedressingWithService5601(self):
        req = open('./requests/de/dropoffs/dropoffsVidedressingService5601.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}

        try:
            r = requests.get(url, headers=headers, timeout=20)
        except requests.exceptions.Timeout:
            pytest.fail("Request timeout. Request: %s" % url)


        response = {}
        if r.text != '':
            response = r.json()
            if type(response) == type({}):
                assert 'messages' not in response.keys

        assert any('commerce_name' in item for item in response)
        assert any('city' in item for item in response)
        assert any('opening_times' in item for item in response)
        assert any('zip' in item for item in response)
        assert any('country' in item for item in response)
        assert any('long' in item for item in response)
        assert any('phone' in item for item in response)
        assert any('state' in item for item in response)
        assert any('address' in item for item in response)
        assert any('lat' in item for item in response)
        assert any('type' in item for item in response)
        assert any('id' in item for item in response)


    def testGetDropoffVidedressingWithService5801(self):
        req = open('./requests/de/dropoffs/dropoffsVidedressingService5801.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}

        try:
            r = requests.get(url, headers=headers, timeout=20)
        except requests.exceptions.Timeout:
            pytest.fail("Request timeout. Request: %s" % url)


        response = {}
        if r.text != '':
            response = r.json()
            if type(response) == type({}):
                assert 'messages' not in response.keys

        assert any('commerce_name' in item for item in response)
        assert any('city' in item for item in response)
        assert any('opening_times' in item for item in response)
        assert any('zip' in item for item in response)
        assert any('country' in item for item in response)
        assert any('long' in item for item in response)
        assert any('phone' in item for item in response)
        assert any('state' in item for item in response)
        assert any('address' in item for item in response)
        assert any('lat' in item for item in response)
        assert any('type' in item for item in response)
        assert any('id' in item for item in response)



if __name__ == '__main__':
    unittest.main()
