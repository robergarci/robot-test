import ConfigParser
import unittest
import pytest
import requests
import conftest
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


    def testGetServiceEmptyFromZipCode(self):
        req = open('./requests/de/getService/getServiceEmptyFromZipCode.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    def testGetServiceNoFromZipCode(self):
        req = open('./requests/de/getService/getServiceNoFromZipCode.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceEmptyToZipCode(self):
        req = open('./requests/de/getService/getServiceEmptyToZipCode.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceNoToZipCode(self):
        req = open('./requests/de/getService/getServiceNoToZipCode.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceEmptyFromCountryCode(self):
        req = open('./requests/de/getService/getServiceEmptyFromCountryCode.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceNoFromCountryCode(self):
        req = open('./requests/de/getService/getServiceNoFromCountryCode.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceNoPackageInfo(self):
        req = open('./requests/de/getService/getServiceNoPackageInfo.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceNoPackageWidth(self):
        req = open('./requests/de/getService/getServiceNoPackageWidth.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceNoPackageHeight(self):
        req = open('./requests/de/getService/getServiceNoPackageHeight.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceNoPackageLength(self):
        req = open('./requests/de/getService/getServiceNoPackageLength.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    def testGetServiceNoPackageWeight(self):
        req = open('./requests/de/getService/getServiceNoPackageWeight.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceNotValidPackageProperty(self):
        req = open('./requests/de/getService/getServiceNotValidPackageProperty.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict

    def testGetServiceNotValidPackagePropertySpeChars(self):
        req = open('./requests/de/getService/getServiceNotValidPackagePropertySpeChars.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    #NOT VALID ZIP CODE WITHOUT SPECIAL CHARACTERS
    def testGetServiceNotValidZipCode(self):
        req = open('./requests/de/getService/getServiceNotValidZipCode.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        error_dict = {}

        if r.text != "[]":
            pytest.fail("Empty list should be returned")

        assert r.status_code == 200


    #NOT VALID ZIP CODE WITH SPECIAL CHARACTERS
    def testGetServiceNotValidZipCodeSpeChars(self):
        req = open('./requests/de/getService/getServiceNotValidZipCodeSpeChars.request', 'r')
        path = req.readline()
        url = "%s%s" % (self.baseUrl, path)
        headers = {'Authorization': '%s' % self.key}
        r = requests.get(url, headers=headers)
        assert r.status_code == 400
        error_dict = {}

        if r.text != '':
            error_dict = r.json()

        assert 'messages' in error_dict


    #HAPPY PATH - Tests all services for germany
    def testGetService(self):
        headers = {'Authorization': '%s' % self.key }
        req = open('./requests/de/getService/getService.request', 'r')
        res = open('./responses/de/getService/getService.response', 'r')
        requests_lines = req.readlines()
        responses_lines = res.readlines()
        for i in range(0, len(requests_lines)):
            url = "%s%s" % (self.baseUrl, requests_lines[i].rstrip())
            expected_services_list = responses_lines[i].rstrip().split(',')
            r = requests.get(url, headers=headers)
            assert r.status_code == 200
            results_list = {}
            if r.text != '':
                results_list = r.json()
                if type(results_list) == type({}):
                    assert 'messages' not in results_list.keys()
                services = []
                for service in results_list:
                    services.append(service['id'])
                results_list = services

            #cheack that the number of services in the response is the same as in the expected list of services
            #self.failIf(len(results_list) != len(expected_services_list), "The number of results in the results list is not the expected.\
            #This is the expected services list: %s. \n This is the returned services list: %s. \nThis is the request %s" % (str(expected_services_list), str(results_list), url))
            #cheack that all expected services are in the response
            fail_services = []
            for service in results_list:
                if not str(service) in expected_services_list:
                    fail_services.append(service)

            assert len(fail_services) == 0


    def testGetServiceVidedressing(self):
        headers = {'Authorization': '%s' % self.key }
        req = open('./requests/de/getService/getServiceVidedressing.request', 'r')
        res = open('./responses/de/getService/getServiceVidedressing.response', 'r')
        requests_lines = req.readlines()
        responses_lines = res.readlines()
        for i in range(0, len(requests_lines)):
            url = "%s%s" % (self.baseUrl, requests_lines[i].rstrip())
            expected_services_list = responses_lines[i].rstrip().split(',')
            r = requests.get(url, headers=headers)
            assert r.status_code == 200
            results_list = {}
            if r.text != '':
                results_list = r.json()
                if type(results_list) == type({}):
                    assert 'messages' not in results_list.keys()
                services = []
                for service in results_list:
                    services.append(service['id'])
                results_list = services

            #cheack that the number of services in the response is the same as in the expected list of services
            #self.failIf(len(results_list) != len(expected_services_list), "The number of results in the results list is not the expected.\
            #This is the expected services list: %s. \n This is the returned services list: %s. \nThis is the request %s" % (str(expected_services_list), str(results_list), url))
            #cheack that all expected services are in the response
            fail_services = []
            for service in results_list:
                if not str(service) in expected_services_list:
                    fail_services.append(service)

            assert len(fail_services) == 0
            print services

if __name__ == '__main__':
    unittest.main(failfast=True)
