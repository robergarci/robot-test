import requests


class Transaction(object):
    def __init__(self):
        self.url = "http://api.integration.packitos.com/v1/services?from[country]=DE&from[zip]=24103&to[country]=DE&to[zip]=24103&packages[0][width]=15&packages[0][height]=\
        15&packages[0][length]=15&packages[0][weight]=2"
        self.headers = {'Authorization': '202f7e24338b4cfa2413a4e0439e99e2bc5bbb3e2313c12852e8814efa55cd0b'}

    def run(self):
        r = requests.get(self.url, headers=self.headers)
        r.raw.read()
        assert (r.status_code == 200)



if __name__ == '__main__':
    trans = Transaction()
    trans.run()

