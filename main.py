from pathlib import Path
import os
from InstatusAPI import InstatusAPI
from MetricsAgent import processPings
from MetricsParser import getAllMetrics
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s")

_API = InstatusAPI(token=os.environ["INSTATUS_TOKEN"])

_METRICS = getAllMetrics(Path("./metrics.json"))
logging.debug("Fetched metrics: " + str(_METRICS))

processPings(_METRICS, _API)
