from ipaddress import IPv4Address
import json
from pathlib import Path
from typing import List
from pydantic import BaseModel, PositiveFloat, PositiveInt

class MetricsInformationServerModel(BaseModel):
    ip: IPv4Address
    pps: PositiveFloat
    psz: PositiveInt
    tmt: PositiveInt

class MetricsInformationInstatusModel(BaseModel):
    sea: PositiveInt
    orgid: str
    compid: str

class MetricsParserModel(BaseModel):
    servd: MetricsInformationServerModel
    isa: MetricsInformationInstatusModel

def getAllMetrics(file: Path) -> List[MetricsParserModel]:
    with open(file, mode="rb") as f:
        data = json.loads(f.read())
        return [MetricsParserModel(**x) for x in data]
