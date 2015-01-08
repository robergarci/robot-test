import requests, json, unittest, ConfigParser, re, conftest, pytest

class TestCustoms():

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

    def testGetCustomsWithNonExistentIdParameter(self):
        req = open('./requests/de/getCustoms/getCustomsWithNonExistentIdParameter.request')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404
        assert r.text == ''

    def testGetCustomsWithEmptyIdParameter(self):
        req = open('./requests/de/getCustoms/getCustomsWithEmptyIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404
        assert r.text == ''

    def testGetCustomsWithNotValidIdParameter(self):
        req = open('./requests/de/getCustoms/getCustomsWithNotValidIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404
        assert r.text == ''

    def testGetCustomsWithEmptyIdParameterSpeChars(self):
        req = open('./requests/de/getCustoms/getCustomsWithNotValidIdParameterSpeChars.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404
        assert r.text == ''

    def testGetCustomsWithoutIdParameter(self):
        req = open('./requests/de/getCustoms/getCustomsWithoutIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404
        assert r.text == ''

    #happy path - id and customs are available
    def testGetLabelWithExistentIdParameter(self):
        req = open('./requests/de/getCustoms/getCustomsWithExistentIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 200
        label_url = r.json()[0]
        r2 = requests.get(label_url)
        res_headers = r2.headers
        assert r2.status_code == 200
        assert res_headers['content-length'] > 0
        regex = re.compile("(\w*.pdf)")
        regex_result = regex.findall(res_headers['content-disposition'])[0]
        assert regex_result != ''

if __name__ == '__main__':
    unittest.main()
