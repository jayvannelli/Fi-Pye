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

    Example
    -------
    >>> news = News(apikey="abc123") # Initialize data source
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

        Example
        -------
        >>> news = News(apikey="abc123") # Initialize data source
        >>>
        >>> general_news = news.general(limit=50)
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

        Example
        -------
        >>> news = News(apikey="abc123") # Initialize data source
        >>>
        >>> all_stock_news = news.stocks(limit=5)
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

        Example
        -------
        >>> news = News(apikey="abc123") # Initialize data source
        >>>
        >>> all_crypto_news = news.cryptos(limit=50)
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

        Example
        -------
        >>> news = News(apikey="abc123") # Initialize data source
        >>>
        >>> all_forex_news = news.forex(limit=50)
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

        Example
        -------
        >>> news = News(apikey="abc123") # Initialize data source
        >>>
        >>> msft_news = news.single_stock("MSFT")
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

        Example
        -------
        >>> news = News(apikey="abc123") # Initialize data source
        >>>
        >>> amd_press_releases = news.stock_press_releases("AMD")
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

        Example
        -------
        >>> news = News(apikey="abc123") # Initialize data source
        >>>
        >>> btc_news = news.single_crypto("BTCUSD")
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

        Example
        -------
        >>> news = News(apikey="abc123") # Initialize data source
        >>>
        >>> usd_myr_news = news.single_crypto("USDMYR") # USD / MYR trading pair
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
