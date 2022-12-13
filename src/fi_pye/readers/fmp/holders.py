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
    >>> holders = Holders(apikey="abc123") # Initialize data source
    >>>
    >>> TICKER = "MCD"
    >>>
    >>> mcd_institutional_holders = holders.institutional_holders(TICKER)
    >>> mcd_mutual_fund_holders = holders.mutual_fund_holders(TICKER)
    >>> mcd_etf_holders = holders.etf_holders(TICKER)
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

        Examples
        --------
        >>> holders = Holders(apikey="abc123") # Initialize data source
        >>>
        >>> aapl_institutional_holders = holders.institutional_holders("AAPL")
        """
        return self.data(
            url_version="v3",
            path=f"institutional-holder/{symbol.upper()}",
            params=None,
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
            pandas.Dataframe

        Examples
        --------
        >>> holders = Holders(apikey="abc123") # Initialize data source
        >>>
        >>> msft_mutual_fund_holders = holders.mutual_fund_holders("MSFT")
        """
        return self.data(
            url_version="v3",
            path=f"mutual-fund-holder/{symbol.upper()}",
            params=None,
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

        Examples
        --------
        >>> holders = Holders(apikey="abc123") # Initialize data source
        >>>
        >>> amzn_etf_holders = holders.etf_holders("AMZN")
        """
        return self.data(
            url_version="v3",
            path=f"etf-stock-exposure/{symbol.upper()}",
            params=None,
        )
