from .reader import FmpReader


class Senators(FmpReader):
    """ """
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