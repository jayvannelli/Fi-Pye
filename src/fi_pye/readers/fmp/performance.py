from .reader import FmpReader


class Performance(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    performance.

    Performance
    -----------
    - Biggest gainers & losers
    - Most active
    - Sector performance
    - Historical sector performance
    - Sector P/E ratio (by date)
    - Industry P/E ratio (by date)

    Example
    -------
    >>> performance = Performance(apikey="abc123") # Initialize data source
    """

    @property
    def biggest_gainers(self):
        """Query FMP / stock_market/gainers / API.

        Obtain a list of the largest one-day gainers (increase in %).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> performance = Performance(apikey="abc123") # Initialize data source
        >>>
        >>> intraday_gainers = performance.biggest_gainers
        """
        return self.data(
            url_version="v3",
            path="stock_market/gainers",
            params=None,
        )

    @property
    def biggest_losers(self):
        """Query FMP / stock_market/losers / API.

        Obtain a list of the largest one-day losers (decrease in %).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> performance = Performance(apikey="abc123") # Initialize data source
        >>>
        >>> intraday_losers = performance.biggest_losers
        """
        return self.data(
            url_version="v3",
            path="stock_market/losers",
            params=None,
        )

    @property
    def most_active(self):
        """Query FMP / stock_market/actives / API.

        Obtain a list of the most active stocks (by volume).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> performance = Performance(apikey="abc123") # Initialize data source
        >>>
        >>> most_active_stocks = performance.most_active
        """
        return self.data(
            url_version="v3",
            path="stock_market/actives",
            params=None,
        )

    @property
    def sector_performance(self):
        """Query FMP / sector-performance / API.

        Obtain a list of daily sector performance (intraday % change).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        """
        return self.data(
            url_version="v3",
            path="sector-performance",
            params=None,
        )

    def historical_sector_performance(self, limit: int):
        """Query FMP / historical-sectors-performance / API.

        Obtain a list of historical sector performance.

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
        >>> performance = Performance(apikey="abc123") # Initialize data source
        >>>
        >>> intraday_losers = performance.biggest_losers
        """
        return self.data(
            url_version="v3",
            path="historical-sectors-performance",
            params={"limit": limit}
        )

    def sectors_pe_ratio(self, date: str, exchange: str = "NYSE"):
        """ Query FMP / sector_price_earning_ratio / API.

        Obtain a list of sector price-to-earnings (P/E) ratios for a specific date.

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
        >>> performance = Performance(apikey="abc123") # Initialize data source
        """
        return self.data(
            url_version="v4",
            path="sector_price_earning_ratio",
            params={
                "date": date,
                "exchange": exchange,
            }
        )

    def industries_pe_ratio(self, date: str, exchange: str = "NYSE"):
        """Query FMP / industry_price_earning_ratio / API.

        Obtain a list of industry price-to-earnings (P/E) ratios for a specific date.

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
        >>> performance = Performance(apikey="abc123") # Initialize data source
        """
        return self.data(
            url_version="v4",
            path="industry_price_earning_ratio",
            params={
                "date": date,
                "exchange": exchange,
            }
        )
