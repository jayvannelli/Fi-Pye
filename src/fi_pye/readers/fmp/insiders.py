from .reader import FmpReader


class Insiders(FmpReader):
    """
    "Insiders" are people who may have valuable private information
    about a company according to their states. In terms of securities
    trading, any director, officer or person who owns more than 10%
    of a company is an insider.
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
        """
        return self.data(
            url_version="v4",
            path="insider-trading",
            params={
                "symbol": symbol.upper(),
                "page": page,
                "apikey": self.apikey,
            },
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
        """
        return self.data(
            url_version="v4",
            path="insider-roaster",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
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
        """
        return self.data(
            url_version="v4",
            path="insider-roaster-statistic",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )
