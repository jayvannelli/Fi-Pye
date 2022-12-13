from .reader import FmpReader


class Sentiment(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    sentiment.
    """

    def stock_social_sentiment(self, symbol: str, page: int = 0):
        """Query FMP / social-sentiment / API.

        Obtain social sentiment statistics for a specific stock.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="social-sentiment",
            params={
                "symbol": symbol.upper(),
                "page": page
            }
        )

    def trending_social_sentiment(self, type: str, source: str = "twitter"):
        """Query FMP / social-sentiments/trending / API.

        Obtain trending social sentiment.

        Parameters
        ----------
        type :
            Type of trend ('bullish' or 'bearish')
        source :
            Social media source ('twitter' or 'stocktwits')

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="social-sentiments/trending",
            params={
                "type": type,
                "source": source
            }
        )

    def change_in_social_sentiment(self, type: str, source: str = "twitter"):
        """Query FMP / social-sentiments/change / API.

        Obtain change in social sentiment.

        Parameters
        ----------
        type :
            Type of trend ('bullish' or 'bearish')
        source :
            Social media source ('twitter' or 'stocktwits')

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="social-sentiments/change",
            params={
                "type": type,
                "source": source
            }
        )
