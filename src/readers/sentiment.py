from .reader import Reader


class Sentiment(Reader):
    def stock_social_sentiment(
        self,
        symbol: str,
        page: int = 0,
    ):
        """Query FMP / social-sentiment / API.

        Obtain social sentiment statistics for a specific stock.

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/social-sentiment-api/

        Parameters
        ----------
            type : Type of trend ('bullish' or 'bearish')
            source : Social media source ('twitter' or 'stocktwits')

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="social-sentiment",
            params={
                "symbol": symbol.upper(),
                "page": page,
                "apikey": self.apikey,
            },
        )

    def trending_social_sentiment(
        self,
        type: str,
        source: str = "twitter",
    ):
        """Query FMP / social-sentiments/trending / API.

        Obtain trending social sentiment.

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/social-sentiment-api/

        Parameters
        ----------
            type : Type of trend ('bullish' or 'bearish')
            source : Social media source ('twitter' or 'stocktwits')

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="social-sentiments/trending",
            params={
                "type": type,
                "source": source,
                "apikey": self.apikey,
            },
        )

    def change_in_social_sentiment(
        self,
        type: str,
        source: str = "twitter",
    ):
        """Query FMP / social-sentiments/change / API.

        Obtain change in social sentiment.

        Documentation
        -------------
        https://site.financialmodelingprep.com/developer/docs/social-sentiment-api/

        Parameters
        ----------
            type : Type of trend ('bullish' or 'bearish')
            source : Social media source ('twitter' or 'stocktwits')

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="social-sentiments/change",
            params={
                "type": type,
                "source": source,
                "apikey": self.apikey,
            },
        )
