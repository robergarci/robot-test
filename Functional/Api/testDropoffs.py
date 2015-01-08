import requests, json, unittest, ConfigParser, re, conftest, pytest

class TestDropoffs():

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

    def testGetDropoffs(self):
        req = open('./requests/de/dropoffs/dropoffs.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        try:
            r = requests.get(url, headers=headers, timeout=20)
        except requests.exceptions.Timeout:
            pytest.fail("Request timeout. Request: %s" % url)

        print "test: ", r.text

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


    def testGetDropoffsWithoutServiceIdParameter(self):
        req = open('./requests/de/dropoffs/dropoffsWithoutServiceIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        try:
            r = requests.get(url, headers=headers, timeout=10)
        except requests.exceptions.Timeout:
            pytest.fail("Request timeout. Request: %s" % url)

        assert r.status_code == 404

    def testGetDropoffsWithNonExistentIdParameter(self):
        req = open('./requests/de/dropoffs/dropoffsWithNonExistentServiceIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        try:
            r = requests.get(url, headers=headers, timeout=10)
        except requests.exceptions.Timeout:
            pytest.fail("Request timeout. Request: %s" % url)

        assert r.status_code == 404
        assert r.text == ''

    def testGetDropoffsWithNotValidIdParameterSpeChars(self):
        req = open('./requests/de/dropoffs/dropoffsWithNotValidIdParameterSpeChars.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        try:
            r = requests.get(url, headers=headers, timeout=10)
        except requests.exceptions.Timeout:
            pytest.fail("Request timeout. Request: %s" % url)

        assert r.status_code == 404
        assert r.text == ''

    #request with existent id param and zip code, but not dropoff services available
    def testGetDropoffsWithExistentIdParameterAndZipCode(self):
        req = open('./requests/de/dropoffs/dropoffsWithExistentIdParameterAndZipCode.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        try:
            r = requests.get(url, headers=headers, timeout=10)
        except requests.exceptions.Timeout:
            pytest.fail("Request timeout. Request: %s" % url)

        assert r.status_code == 200
        response = None
        if r.text != '':
            response = r.json()
        assert response == type([])

    def testGetDropoffVidedressing(self):
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


if __name__ == '__main__':
    unittest.main()
