from .reader import Reader


class News(Reader):
    def general_news(
        self,
        limit: int = 50,
    ):
        """Query FMP / general_news /  API.

        Obtain latest general news.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/general-news-api/

        Parameters
        ----------
            limit : Number of rows to return.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="general_news",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def stock_news(
        self,
        symbol: str,
        limit: int = 50,
    ):
        """Query FMP / stock_news /  API.

        Obtain news for a specific stock.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-news-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.
            limit : Number of rows to return.

        ------
        Return : pandas DataFrame
        ------
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

    def stock_press_releases(
        self,
        symbol: str,
        limit: int = 50,
    ):
        """Query FMP / press-releases /  API.

        Obtain stock press releases.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/press-releases-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.
            limit : Number of rows to return.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path=f"press-releases/{symbol.upper()}",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def latest_stock_news(
        self,
        limit: int = 50,
    ):
        """Query FMP / stock_news /  API.

        Obtain latest stock news.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-news-api/

        Parameters
        ----------
            limit : Number of rows to return.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="stock_news",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def crypto_news(
        self,
        symbol: str,
        limit: int = 50,
    ):
        """Query FMP / crypto_news /  API.

        Obtain news for a specific cryptocurrency.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/crypto-news-api/

        Parameters
        ----------
            symbol : Crypto ticker symbol (Example='BTCUSD').
            limit : Number of rows to return.

        ------
        Return : pandas DataFrame
        ------
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

    def latest_crypto_news(
        self,
        limit: int = 50,
    ):
        """Query FMP / crypto_news /  API.

        Obtain latest crypto news.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/crypto-news-api/

        Parameters
        ----------
            limit : Number of rows to return.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="crypto_news",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def forex_news(
        self,
        symbol: str,
        limit: int = 50,
    ):
        """Query FMP / forex_news /  API.

        Obtain news for a specific fx symbol.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/forex-news-api/

        Parameters
        ----------
            symbol : FX symbol (Example='EURUSD').
            limit : Number of rows to return.

        ------
        Return : pandas DataFrame
        ------
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

    def latest_forex_news(
        self,
        limit: int = 50,
    ):
        """Query FMP / forex_news /  API.

        Obtain latest forex news.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/forex-news-api/

        Parameters
        ----------
            limit : Number of rows to return.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="forex_news",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )
