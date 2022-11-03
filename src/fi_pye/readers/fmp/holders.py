from .reader import FmpReader


class Holders(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    the 'holders' of a specific stock (by symbol).

    Holders
    -------
    - Institutions
    - Mutual funds
    - Exchange traded funds (ETFs)

    Examples
    --------
    """
    def institutional_holders(self, symbol: str):
        """Query FMP / institutional-holder / API.

        Receive list of institutions holding a given stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"institutional-holder/{symbol.upper()}",
            params={"apikey": self.apikey},
        )

    def mutual_fund_holders(self, symbol: str):
        """Query FMP / mutual-fund-holder / API.

        Receive list of mutual funds holding a given stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe"""
        return self.data(
            url_version="v3",
            path=f"mutual-fund-holder/{symbol.upper()}",
            params={"apikey": self.apikey},
        )

    def etf_holders(self, symbol: str):
        """Query FMP / etf-stock-exposure / API.

        Receive list of exchange traded funds (ETFs) holding a given stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"etf-stock-exposure/{symbol.upper()}",
            params={"apikey": self.apikey},
        )