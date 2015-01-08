class PackLinkUtils(object):
	def cookies_to_dict(self, cookie_str):
		cookie_list = cookie_str.split(";")
		cookie_dict = {}
		for cookie in cookie_list:
			cookie = cookie.replace("=",":",1)
			cookie = cookie.split(":")
			cookie_dict[cookie[0]] = cookie[1]
		return cookie_dict