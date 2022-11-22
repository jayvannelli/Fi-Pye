from .reader import NasdaqReader
from .utils import _validate_limit


class Blockchain(NasdaqReader):
    """Blockchain. """

    def btc_difficulty(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="BCHAIN/DIFF",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )

    def btc_avg_block_size(self, limit: int = 25):
        """ """
        return self.data(
            base="datasets",
            path="BCHAIN/AVBLS",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey,
            },
        )


