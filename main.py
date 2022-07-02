from pathlib import Path
import os
from InstatusAPI import InstatusAPI
from MetricsAgent import processPings
from MetricsParser import getAllMetrics

_API = InstatusAPI(token=os.environ["INSTATUS_TOKEN"])
_METRICS = getAllMetrics(Path("./metrics.json"))
processPings(_METRICS, _API)
