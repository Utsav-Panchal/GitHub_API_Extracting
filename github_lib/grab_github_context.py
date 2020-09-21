import requests
class AllContextData:

    def __init__(self, BASE_URL):
        self.BASE_URL = BASE_URL

    @property
    def grab_context_by_request(self):
        self.data = requests.get(self.BASE_URL)
        return self.data.json()
