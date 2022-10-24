from .reader import Reader


class Insiders(Reader):
    """
    "Insiders" are people who may have valuable private information
    about a company according to their states. In terms of securities
    trading, any director, officer or person who owns more than 10%
    of a company is an insider.

    FMP's API provides information collected from fulfillments by
    insiders SEC Forms 3, 4 and 5.
    """

    def insider_trading(
        self,
        symbol: str,
        page: int = 0,
    ):
        """Query FMP / insider-trading / API.

        Obtain stock insider trading.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-insider-trading-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
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

    def insider_roster(
        self,
        symbol: str,
    ):
        """Query FMP / insider-roaster / API.

        Obtain stock insider roster.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-insider-trading-api/#Insider-Roaster

        Parameters
        ----------
            symbol : Stock ticker symbol.

        ------
        Return : pandas DataFrame
        ------
        """

        return self.data(
            url_version="v4",
            path="insider-roaster",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def insider_roster_stats(
        self,
        symbol: str,
    ):
        """Query FMP / insider-roaster-statistic / API.

        Obtain stock insider roster trading statistics.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-insider-trading-api/#Insider-Roaster

        Parameters
        ----------
            symbol : Stock ticker symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="insider-roaster-statistic",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )
