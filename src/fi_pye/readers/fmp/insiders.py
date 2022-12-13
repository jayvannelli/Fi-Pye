from .reader import FmpReader


class Insiders(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related
    to stock insiders.

    "Insiders" are people who may have valuable private information
    about a company according to their states. In terms of securities
    trading, any director, officer or person who owns more than 10%
    of a company is an insider.

    Insiders
    --------
    - Insider trading (by symbol)
    - Insider roster (by symbol)
    - Insider roster trading stats (by symbol)

    Examples
    --------
    >>> insiders = Insiders(apikey="abc123") # Initialize data source
    >>>
    >>> TICKER = "TSLA"
    >>>
    >>> tsla_insider_trades = insiders.insider_trading(TICKER)
    >>> tsla_insider_roster = insiders.insider_roster(TICKER)
    >>> tsla_roster_trading_stats = insiders.insider_roster_stats(TICKER)
    """

    def insider_trading(self, symbol: str, page: int = 0):
        """Query FMP / insider-trading / API.

        Obtain stock insider trading.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        page : default = 0
            Response page number.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> insiders = Insiders(apikey="abc123") # Initialize data source
        >>>
        >>> amd_insider_trades = insiders.insider_trading("AMD")
        """
        return self.data(
            url_version="v4",
            path="insider-trading",
            params={
                "symbol": symbol.upper(),
                "page": page
            }
        )

    def insider_roster(self, symbol: str):
        """Query FMP / insider-roaster / API.

        Obtain stock insider roster.

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
        >>> insiders = Insiders(apikey="abc123") # Initialize data source
        >>>
        >>> wfc_insider_roster = insiders.insider_roster("WFC")
        """
        return self.data(
            url_version="v4",
            path="insider-roaster",
            params={"symbol": symbol.upper()}
        )

    def insider_roster_stats(self, symbol: str):
        """Query FMP / insider-roaster-statistic / API.

        Obtain stock insider roster trading statistics.

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
        >>> insiders = Insiders(apikey="abc123") # Initialize data source
        >>>
        >>> abt_insider_roster_stats = insiders.insider_roster_stats("ABT")
        """
        return self.data(
            url_version="v4",
            path="insider-roaster-statistic",
            params={"symbol": symbol.upper()}
        )
