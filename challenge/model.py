import pandas as pd
import numpy as np
from datetime import datetime

from typing import Tuple, Union, List
from sklearn.linear_model import LogisticRegression


class DelayModel:

    def __init__(
        self
    ):
        # model config
        class_weight = {1: 0.8161845157337302, 0: 0.18381548426626987}
        self._model = LogisticRegression(class_weight=class_weight)
        self._model.coef_ = np.array([[
            1.11179859,
            0.79358501,
            0.50121651,
            0.063798,
            0.61961298,
            0.59363468,
            -0.30059333,
            0.30639762,
            0.19189159,
            -1.46293121
        ]])
        self._model.intercept_ = np.array([[-0.58720526]])
        self._model.classes_ = np.array([[0, 1]])

    def preprocess(
        self,
        data: pd.DataFrame,
        target_column: str = None
    ) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Prepare raw data for training or predict.

        Args:
            data (pd.DataFrame): raw data.
            target_column (str, optional): if set, the target is returned.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: features and target.
            or
            pd.DataFrame: features.
        """

        # Model features
        opera_categories = pd.CategoricalDtype(["Latin American Wings", "Grupo LATAM", "Sky Airline", "Copa Air"])
        tipo_vuelo_categories = pd.CategoricalDtype(["I"])
        mes_categories = pd.CategoricalDtype([4, 7, 10, 11, 12])

        features = pd.concat([
            pd.get_dummies(
                pd.Series(data['OPERA'], dtype=opera_categories),
                prefix='OPERA'
            ),
            pd.get_dummies(
                pd.Series(data['TIPOVUELO'], dtype=tipo_vuelo_categories),
                prefix='TIPOVUELO'
            ),
            pd.get_dummies(
                pd.Series(data['MES'], dtype=mes_categories),
                prefix='MES'
            )],
            axis=1
        )

        if target_column:
            data[target_column] = self._create_target_column(data)
            target = pd.DataFrame(data[target_column])
            return features, target
        return features

    def fit(
        self,
        features: pd.DataFrame,
        target: pd.DataFrame
    ) -> None:
        """
        Fit model with preprocessed data.

        Args:
            features (pd.DataFrame): preprocessed data.
            target (pd.DataFrame): target.
        """
        self._model.fit(features, target)

    def predict(
        self,
        features: pd.DataFrame
    ) -> List[int]:
        """
        Predict delays for new flights.

        Args:
            features (pd.DataFrame): preprocessed data.
        
        Returns:
            (List[int]): predicted targets.
        """
        return [pred.item() for pred in self._model.predict(features)]

    @staticmethod
    def _create_target_column(data: pd.DataFrame):
        def get_min_diff(df):
            fecha_o = datetime.strptime(df['Fecha-O'], '%Y-%m-%d %H:%M:%S')
            fecha_i = datetime.strptime(df['Fecha-I'], '%Y-%m-%d %H:%M:%S')
            return ((fecha_o - fecha_i).total_seconds())/60

        threshold_in_minutes = 15
        min_diff = data.apply(get_min_diff, axis=1)
        return np.where(min_diff > threshold_in_minutes, 1, 0)


