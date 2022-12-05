from .reader import FmpReader


class News(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    news.

    News
    ----
    - General news (general = news across all industries)
    - Industry specific news (stocks, cryptos & forex)
    - Single symbol news (symbol = one stock, crypto or forex ticker symbol)
    """
    def general(self, limit: int = 25):
        """Query FMP / general_news /  API.

        Obtain most recent general news.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="general_news",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def stocks(self, limit: int = 25):
        """Query FMP / stock_news /  API.

        Obtain most recent stocks news (all stocks).

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path="stock_news",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def cryptos(self, limit: int = 25):
        """Query FMP / crypto_news /  API.

        Obtain most recent cryptocurrency news (all cryptos).

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="crypto_news",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def forex(self, limit: int = 25):
        """Query FMP / forex_news /  API.

        Obtain most recent forex news (all forexes).

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="forex_news",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def single_stock(self, symbol: str, limit: int = 25):
        """Query FMP / stock_news /  API.

        Obtain most recent news for a specific stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path="stock_news",
            params={
                "tickers": symbol.upper(),
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def stock_press_releases(self, symbol: str, limit: int = 25):
        """Query FMP / press-releases /  API.

        Obtain most recent press releases for a specific stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"press-releases/{symbol.upper()}",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def single_crypto(self, symbol: str, limit: int = 25):
        """Query FMP / crypto_news /  API.

        Obtain most recent news for a specific cryptocurrency (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="crypto_news",
            params={
                "symbol": symbol.upper(),
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def single_forex(self, symbol: str, limit: int = 25):
        """Query FMP / forex_news /  API.

        Obtain most recent news for a specific forex (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="forex_news",
            params={
                "symbol": symbol.upper(),
                "limit": limit,
                "apikey": self.apikey,
            },
        )
