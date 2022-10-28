from .reader import Reader


class Holders(Reader):
    """Holders of a given stock. """

    def institutional_holders(
            self,
            symbol: str,
    ):
        """Institutional holders of a given stock (by symbol). """
        return self.data(
            url_version="v3",
            path=f"institutional-holder/{symbol.upper()}",
            params={"apikey": self.apikey},
        )

    def mutual_fund_holders(
            self,
            symbol: str,
    ):
        """Mutual fund holders of a given stock (by symbol). """
        return self.data(
            url_version="v3",
            path=f"mutual-fund-holder/{symbol.upper()}",
            params={"apikey": self.apikey},
        )

    def etf_holders(
            self,
            symbol: str,
    ):
        """Exchange traded fund (ETF) holders of a given stock (by symbol). """
        return self.data(
            url_version="v3",
            path=f"etf-stock-exposure/{symbol.upper()}",
            params={"apikey": self.apikey},
        )