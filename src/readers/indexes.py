from .reader import Reader


class Indexes(Reader):
    @property
    def sp500_companies(self):
        """Query FMP / sp500_constituent / API.

        Obtain a list of companies within the S&P 500 (either current or historical).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/list-of-sp-500-companies-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="sp500_constituent",
            params={"apikey": self.apikey},
        )

    @property
    def historical_sp500_companies(self):
        """Query FMP / sp500_constituent / API.

        Obtain a list of companies within the S&P 500 (either current or historical).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/list-of-sp-500-companies-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="historical/sp500_constituent",
            params={"apikey": self.apikey},
        )

    @property
    def nasdaq_companies(self):
        """Query FMP / nasdaq_constituent / API.

        Obtain a list of companies within the Nasdaq (either current or historical).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/list-of-nasdaq-companies-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="nasdaq_constituent",
            params={"apikey": self.apikey},
        )

    @property
    def historical_nasdaq_companies(self):
        """Query FMP / nasdaq_constituent / API.

        Obtain a list of companies within the Nasdaq (either current or historical).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/list-of-nasdaq-companies-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="historical/nasdaq_constituent",
            params={"apikey": self.apikey},
        )

    @property
    def dow_jones_companies(self):
        """Query FMP / dowjones_constituent / API.

        Obtain a list of companies within the Dow Jones (either current or historical).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/list-of-dow-companies-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="dowjones_constituent",
            params={"apikey": self.apikey},
        )

    @property
    def historical_dow_jones_companies(self):
        """Query FMP / dowjones_constituent / API.

        Obtain a list of companies within the Dow Jones (either current or historical).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/list-of-dow-companies-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="historical/dowjones_constituent",
            params={"apikey": self.apikey},
        )
