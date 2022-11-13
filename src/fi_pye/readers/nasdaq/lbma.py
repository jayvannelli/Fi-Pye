from .reader import NasdaqReader
from .utils import _validate_limit


class LBMA(NasdaqReader):
    """
    Query Nasdaq Data Link API endpoints related to the
    London bullion Market Association dataset published by Quandl.

    Method descriptions are taken from the csv provided by
    Nasdaq under the 'usage' section of this dataset.

    LBMA
    ----
    - Gold price
    - Silver price
    - Gold forward offered rates (No longer updated by Quandl)
    - London gold fixings (No longer updated by Quandl)
    """
    def gold_price(self, limit: int = 25):
        """Query Nasdaq / LBMA/GOLD / API.

        Gold Price: London Fixings, London Bullion Market Association (LBMA). Fixing levels
        are set per troy ounce. The London Gold Fixing Companies set the prices for gold
        that are globally considered as the international standard for pricing of gold.
        The Gold price in London is set twice a day by five LBMA Market Makers who comprise
        the London Gold Market Fixing Limited (LGMFL). The process starts with the
        announcement from the Chairman of the LGMFL to the other members of the LBMA Market
        Makers, then relayed to the dealing rooms where customers can express their interest
        as buyers or sellers and also the quantity they wish to trade. The gold fixing price
        is then set by collating bids and offers until the supply and demand are matched.
        At this point the price is announced as the 'Fixed' price for gold and all business
        is conducted on the basis of that price.
        """
        return self.data(
            base="datasets",
            path="LBMA/GOLD",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def silver_price(self, limit: int = 25):
        """Query Nasdaq / LBMA/SILVER / API.

        Silver Price: London Fixing. London Bullion Market Association (LBMA). Fixing levels
        are set per troy ounce. The London Silver Fixing Companies set the prices for gold
        that are globally considered as the international standard for pricing of silver.
        The Silver price in London is set once a day by three LBMA Market Makers who comprise
        the London Silver Market Fixing Limited (LSMFL). The process starts with the
        announcement from the Chairman of the LSMFL to the other members of the LBMA Market
        Makers, then relayed to the dealing rooms where customers can express their interest
        as buyers or sellers and also the quantity they wish to trade. The silver fixing price
        is then set by collating bids and offers until the supply and demand are matched.
        At this point the price is announced as the 'Fixed' price for silver and all business
        is conducted on the basis of that price.
        """
        return self.data(
            base="datasets",
            path="LBMA/SILVER",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def gold_forward_offered_rates(self, limit: int = 25):
        """Query Nasdaq / LBMA/GOFO / API.

        *NO LONGER UPDATED BY QUANDL AS OF 2015-01-30

        Gold forward rates (GOFO), in percentages; London Bullion Market Association (LBMA).
        LIBOR difference included. The Gold Forward Offered Rate is an international standard rate
        at which dealers will lend gold on a swap basis against US dollars, providing the
        foundation for the pricing of gold swaps, forwards and leases.
        """
        return self.data(
            base="datasets",
            path="LBMA/GOFO",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def london_gold_fixings(self, limit: int = 25):
        """Query Nasdaq / LBMA/DAILY / API.

        *NO LONGER UPDATED BY QUANDL AS OF 2000

        The Fixings are an open process at which market participants can transact business on the
        basis of a single quoted price. Orders can be changed throughout the proceedings as the
        price is moved higher and lower until such time as buyers` and sellers` orders are satisfied
        and the price is said to be `fixed`. Orders executed at the fixings are conducted as
        principal-to-principal transactions between the client and the dealer through whom the order
        is placed.
        """
        return self.data(
            base="datasets",
            path="LBMA/DAILY",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )