import requests, json, unittest, ConfigParser, re, conftest, pytest

class TestTracking():

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


    def testTrackShipmentsWithNonExistentIdParameter(self):
        req = open('./requests/de/trackShipments/trackShipmentsWithNonExistentIdParameter.request')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        print "t ", r.text
        assert r.status_code == 404
        assert r.text == ''

    def testTrackShipmentsWithEmptyIdParameter(self):
        req = open('./requests/de/trackShipments/trackShipmentsWithEmptyIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404
        assert r.text == ''

    def testTrackShipmentsWithNotValidIdParameter(self):
        req = open('./requests/de/trackShipments/trackShipmentsWithNotValidIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404
        assert r.text == ''

    def testTrackShipmentsWithEmptyIdParameterSpeChars(self):
        req = open('./requests/de/trackShipments/trackShipmentsWithNotValidIdParameterSpeChars.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        self.assertEqual(r.status_code, 404, 'response HTTP code should be 404, but was %s.\nRequest: %s' % (str(r.status_code), url))
        self.assertEqual(r.text, '', 'response body should be empty in 404 errors raised by our api')

    def testTrackShipmentsWithoutIdParameter(self):
        req = open('./requests/de/trackShipments/trackShipmentsWithoutIdParameter.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 404
        assert r.text == ''

    #happy path - id and track info are available
    def testTrackWithExistentIdParameterAndNotTrackingAvailable(self):
        req = open('./requests/de/trackShipments/trackShipmentsWithExistentIdParameterAndNotTrackingAvailable.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 200
        trackingList = {}
        if r.text != "":
            trackingList = r.json()

        assert type([]) == type(trackingList)
        assert len(trackingList) == 0

    def testTrackWithExistentIdParameterAndTrackingAvailable(self):
        req = open('./requests/de/trackShipments/trackShipmentsWithExistentIdParameterAndTrackingAvailable.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 200
        trackingList = None
        print r.text
        if r.text != "":
            trackingList = r.json()
        else:
            pytest.fail("Empty response for valid tracking request: %s" % url)

        assert type([]) == type(trackingList)
        assert len(trackingList) != 0

if __name__ == '__main__':
    unittest.main()
