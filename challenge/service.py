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
        for sample in data:
            features["OPERA"].append(sample.OPERA)
            features["TIPOVUELO"].append(sample.TIPOVUELO)
            features["MES"].append(sample.MES)

        features = pd.DataFrame(features)
        features = self._model.preprocess(features)
        return self._model.predict(features)

