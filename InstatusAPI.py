from pydantic import BaseModel, NonNegativeInt
import requests
import json

from MetricsParser import MetricsParserModel

class InstatusMetricsRequestBodyModel(BaseModel):
    timestamp: NonNegativeInt
    value: NonNegativeInt


class InstatusAPI:
    def __init__(self, token: str, endpoint: str = "https://api.instatus.com/v1/"):
        self._ENDPOINT = endpoint
        self.__TOKEN = token
    def sendMetrics(self, metrics: InstatusMetricsRequestBodyModel, pm: MetricsParserModel):
        print(metrics, pm)
        response = requests.post(
            url=f"{self._ENDPOINT}{pm.isa.orgid}/metrics/{pm.isa.compid}",
            headers={
                "Authorization": f"Bearer {self.__TOKEN}",
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps(metrics.dict())
        )
        print(response.text)