from typing import List
from pythonping import ping
from InstatusAPI import InstatusAPI, InstatusMetricsRequestBodyModel
from MetricsParser import MetricsParserModel
from threading import Thread
import time

def makePing(server: MetricsParserModel) -> int:
    return int(ping(server.servd.ip.__str__(), size=server.servd.psz, timeout=server.servd.tmt, interval=server.servd.pps, count=server.isa.sea).rtt_avg * 1000)

def executePing(server: MetricsParserModel, api: InstatusAPI) -> None:
    while True:
        pp = InstatusMetricsRequestBodyModel(timestamp=int(round(time.time())), value=makePing(server))
        api.sendMetrics(pp, server)

def processPings(servers: List[MetricsParserModel], api: InstatusAPI) -> None:
    for server in servers:
        Thread(target=executePing, args=(server, api)).start()
