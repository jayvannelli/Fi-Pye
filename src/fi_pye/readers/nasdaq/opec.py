from .reader import NasdaqReader
from .utils import _validate_limit


class OPEC(NasdaqReader):
    """Organization of the Petroleum Exporting Countries. """

    def crude_oil_price(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="OPEC/ORB",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

