from .reader import NasdaqReader
from .utils import _validate_limit


class MarketableBorrowing(NasdaqReader):
    """ """
    def net_marketable(self, limit=None):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        return self.data(
            path="USTREASURY/TMBOR",
            params={
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )

    def net_non_marketable(self, limit=None):
        """Query Nasdaq / USTREASURY/TNMBOR / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        return self.data(
            path="USTREASURY/TNMBOR",
            params={
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )