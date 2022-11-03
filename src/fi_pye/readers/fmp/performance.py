from .reader import FmpReader


class Performance(FmpReader):
    """ """
    @property
    def biggest_gainers(self):
        """Query FMP / stock_market/gainers / API.

        Returns current list of the largest one day gainers (increase in %).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        """
        return self.data(
            url_version="v3",
            path="stock_market/gainers",
            params={"apikey": self.apikey},
        )

    @property
    def biggest_losers(self):
        """Query FMP / stock_market/losers / API.

        Returns current list of the largest one day losers (decrease in %).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        """
        return self.data(
            url_version="v3",
            path="stock_market/losers",
            params={"apikey": self.apikey},
        )

    @property
    def most_active(self):
        """Query FMP / stock_market/actives / API.

        Returns current list of the most active stocks (in volume).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        """
        return self.data(
            url_version="v3",
            path="stock_market/actives",
            params={"apikey": self.apikey},
        )

    @property
    def sector_performance(self):
        """Query FMP / sector-performance / API.

        Returns list of daily sector performance (intraday % change).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        """
        return self.data(
            url_version="v3",
            path="sector-performance",
            params={"apikey": self.apikey},
        )

    def historical_sector_performance(self, limit: int):
        """Query FMP / historical-sectors-performance / API.

        Returns list of historical sector performance.

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
        """
        return self.data(
            url_version="v3",
            path="historical-sectors-performance",
            params={
                "limit": limit,
                "apikey": self.apikey
            },
        )

    def sectors_pe_ratio(self, date: str, exchange: str = "NYSE"):
        """ Query FMP / sector_price_earning_ratio / API.

        Returns list of sector price-to-earnings (P/E) ratios on a specific date.

        Parameters
        ----------
        date :
            Date to get P/E ratio from in 'YYYY-MM-DD' format
        exchange : default = 'NYSE'
            Stock exchange

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        """
        return self.data(
            url_version="v4",
            path="sector_price_earning_ratio",
            params={
                "date": date,
                "exchange": exchange,
                "apikey": self.apikey,
            }
        )

    def industries_pe_ratio(self, date: str, exchange: str = "NYSE"):
        """Query FMP / industry_price_earning_ratio / API.

        Returns list of industry price-to-earnings (P/E) ratios on a specific date.

        Parameters
        ----------
        date :
            Date to get P/E ratio from in 'YYYY-MM-DD' format
        exchange : default = 'NYSE'
            Stock exchange

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        """
        return self.data(
            url_version="v4",
            path="industry_price_earning_ratio",
            params={
                "date": date,
                "exchange": exchange,
                "apikey": self.apikey,
            }
        )