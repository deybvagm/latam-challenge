from typing import List
import pandas as pd

from challenge.model import DelayModel
from challenge.types import Flight


class DelayService:
    def __init__(self, model: DelayModel):
        self._model = model

    def predict(self, data: List[Flight]) -> List[int]:

        features = {
            "OPERA": [],
            "TIPOVUELO": [],
            "MES": []
        }
        for flight in data:
            features["OPERA"].append(flight.OPERA)
            features["TIPOVUELO"].append(flight.TIPOVUELO)
            features["MES"].append(flight.MES)

        features = pd.DataFrame(features)
        features = self._model.preprocess(features)
        return self._model.predict(features)

