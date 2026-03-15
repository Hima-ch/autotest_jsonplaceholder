import os
import requests
#import allure
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

class BaseApi:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        #self.token = os.getenv("TOKEN")
        self.session = requests.Session()
        #if self.token:
            #self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"Sending {method} request to {url}")
        if kwargs.get("json"):
            logger.debug(f"Payload: {kwargs['json']}")

        response = self.session.request(method, url, **kwargs)
        response.seconds = response.elapsed.total_seconds()
        logger.info(f"Response status: {response.status_code}")
        return response
        #allure

    def get(self, endpoint, params=None):
        return self._make_request("GET", endpoint, params=params)
    def post(self, endpoint, payload):
        return self._make_request("POST", endpoint, json=payload)
    def put(self, endpoint, payload):
        return self._make_request("PUT", endpoint, json=payload)
    def delete(self, endpoint):
        return self._make_request("DELETE", endpoint)