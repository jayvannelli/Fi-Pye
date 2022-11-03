from .reader import NasdaqReader
from .utils import _validate_limit


class MarketableIssuance(NasdaqReader):
    """ """
    def marketable_issuance_breakdown(self, limit=None):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        return self.data(
            path="USTREASURY/BRDNM",
            params={
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )