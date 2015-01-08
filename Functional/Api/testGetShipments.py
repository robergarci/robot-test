import requests, json, unittest, ConfigParser, re, conftest, pytest

class TestGetShipments():

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


    def testGetShipmentWithExistentIdParameter(self):
        url = "%s%s" % (self.baseUrl, "/v1/shipments/DE006U00D5414AA")
        url = "%s%s" % (self.baseUrl, "/v1/shipments")
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        print r.text
        #self.assertEqual(r.status_code, 404, 'response HTTP code should be 404, but was %s.\nRequest: %s' % (str(r.status_code), url))
        #self.assertEqual(r.text, '', 'response body should be empty in 404 errors raised by our api')


if __name__ == '__main__':
    unittest.main()
