from .reader import NasdaqReader
from .utils import _validate_limit, _validate_timeframe


class SP500Ratios(NasdaqReader):
    """ """
    def dividend(self, timeframe: str, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_DIV_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def dividend_yield(self, timeframe: str, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_DIV_YIELD_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )