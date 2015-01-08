import requests, json, unittest, ConfigParser, re, conftest, pytest

class TestLabels():

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



    def testGetLabelWithNonExistentIdParameter(self):
        req = open('./requests/de/getLabels/getLabelWithNonExistentIdParameter.request')
        path = req.readline()
        print 'Testing in %s environment' % self.baseUrl
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404

    def testGetLabelWithEmptyIdParameter(self):
        req = open('./requests/de/getLabels/getLabelWithEmptyIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        print url
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404

    def testGetLabelWithNotValidIdParameter(self):
        req = open('./requests/de/getLabels/getLabelWithNotValidIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404

    def testGetLabelWithWithNotValidIdParameterSpeChars(self):
        req = open('./requests/de/getLabels/getLabelWithNotValidIdParameterSpeChars.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404

    def testGetLabelWithoutIdParameter(self):
        req = open('./requests/de/getLabels/getLabelWithoutIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404

    #happy path - id and labels are available
    def testGetLabelWithExistentIdParameter(self):
        req = open('./requests/de/getLabels/getLabelWithExistentIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        print url
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

    #sad path - id exists, but labels are not available
    def testGetLabelWithExistentIdParameterAndLabelsNotAvailable(self):
        req = open('./requests/de/getLabels/getLabelWithExistentIdParameterAndLabelsNotAvailable.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetLabelVidedressing(self):
        req = open('./requests/de/getLabels/getLabelVidedressing.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        print url
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 200
        label_url = r.json()[0]
        label_url = 'http://%s' % label_url
        print label_url
        r2 = requests.get(label_url)
        res_headers = r2.headers
        assert r2.status_code == 200
        assert res_headers['content-length'] > 0
        regex = re.compile("(\w*.pdf)")
        regex_result = regex.findall(res_headers['content-disposition'])[0]
        assert regex_result != ''


if __name__ == '__main__':
   unittest.main()
