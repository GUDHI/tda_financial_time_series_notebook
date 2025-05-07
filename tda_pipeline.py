# This file is part of the Gudhi Library - https://gudhi.inria.fr/ - which is released under MIT.
# See file LICENSE or go to https://gudhi.inria.fr/licensing/ for full license details.
# Author(s):       Vincent Rouvreau
#
# Copyright (C) 2021 Inria
#
# Modification(s):
#   - 2025/05 Vincent Rouvreau: Use RipsPersistence sklearn interface
#   - YYYY/MM Author: Description of the modification

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from joblib import Parallel, delayed


class DataSelector(BaseEstimator, TransformerMixin):
    """
    This is a class to select data from a data frame and set it with the correct format.
    """

    def __init__(self, start=0, end=250, w=80, n_jobs=None):
        """
        Constructor for the DataSelector class.

        Parameters:
            start (date): The date index in the data frame to start the data analysis. Default value is `0`.
            end (date): The date index in the data frame to end the data analysis. Default value is `250`.
            w (int): The window size in days. Default value is `80`.
            n_jobs (int): cf. https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html
        """
        self.start = start
        self.end = end
        self.w = w
        self.n_jobs = n_jobs

    def fit(self, X, Y=None):
        """
        Nothing to be done, but useful when included in a scikit-learn Pipeline.
        """
        return self

    def transform(self, X, Y=None):
        """
        Select persistence diagrams from its dimension.

        Parameters:
            X (Pandas DataFrame): Indexed by date, time series of indices

        Returns:
            For each day of the DataFrame, returns `w` points.
        """


        return[X.iloc[(idx - self.w):idx].values for idx in range(self.start+self.w, self.end)]


class LPNorm(BaseEstimator, TransformerMixin):
    """
    This is a class to compute Landscape Lp Norm L1 and L2.
    """

    def __init__(self, n_jobs=None):
        """
        Constructor for the LPNorm class.

        Parameters:
            n_jobs (int): cf. https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html
        """
        self.n_jobs = n_jobs

    def fit(self, X, Y=None):
        """
        Nothing to be done, but useful when included in a scikit-learn Pipeline.
        """
        return self

    def __transform(self, landscape):
        return [np.linalg.norm(landscape, ord=1), np.linalg.norm(landscape, ord=2)]

    def transform(self, X, Y=None):
        """
        Computes Landscape Lp Norm L1 and L2.

        Parameters:
            X (numpy array): Landscape

        Returns:
            Lp Norm L1 and L2.
        """
        return [[np.linalg.norm(landscape, ord=1), np.linalg.norm(landscape, ord=2)] for landscape in X]
        #return Parallel(n_jobs=self.n_jobs)(delayed(self.__transform)(landscape) for landscape in X)
