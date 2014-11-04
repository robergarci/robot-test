import json, requests

class GetServiceLibrary(object):
	def compare_response(self, expected_services_list, response):
		results_list = []
		expected_services_list = expected_services_list.split(",")
		services = []
		if response != "":
			results_list = json.loads(response)
			if not type(results_list) == type([]):
				raise AssertionError("The expected response and the received response does not match.")

			for service in results_list:
				services.append(str(service['id']))

			diff = set(expected_services_list) - set(services)
			diff2 = set(services) - set(expected_services_list)
			
			if len(diff) != 0 or len(diff2) != 0:
				raise AssertionError("The expected response and the received response does not match.")








