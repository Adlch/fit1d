from common.fit1d import Fit1D
from models.gaussianModel import GaussianModel


class GaussianFit(Fit1D):

    """
    usage:

    GF = GaussianFit()
    GF.fit(x, y)

    """

    def _calc_fit(self):
        self._fit_data.model = GaussianModel()

    def _calc_eval(self):
        pass











