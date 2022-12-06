from .reader import FmpReader


class Senators(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    senators and their activity with specific stocks.

    Senators
    --------
    - Senate trading (by symbol)
    - Senate disclosures (by symbol)

    Examples
    --------
    >>> senators = Senators(apikey="abc123") # Initialize data source
    >>>
    >>> tesla_senate_trading = senators.senate_trading("TSLA")
    """

    def senate_trading(self, symbol: str):
        """Query FMP / senate-trading / API.

        Obtain company senate trades.

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
            url_version="v4",
            path="senate-trading",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def senate_disclosures(self, symbol: str):
        """Query FMP / senate-disclosure / API.

        Obtain company senate disclosures.

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
            url_version="v4",
            path="senate-disclosure",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )
