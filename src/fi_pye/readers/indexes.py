from .reader import Reader


class Indexes(Reader):
    """
    Obtain current and historical constituents within
    a given market indexes.

    Market indexes available:
        - S&P 500
        - Nasdaq
        - Dow Jones
    """
    @property
    def sp500_companies(self):
        """Query FMP / sp500_constituent / API.

        Obtain a list of companies within the S&P 500 (either current or historical).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> indexes = Indexes(apikey='abc123')
        >>>
        >>> sp_500 = indexes.sp500_companies
        >>> print(sp_500.head())
          symbol         name       sector  ... dateFirstAdded         cik founded
        0    MMM           3M  Industrials  ...     1976-08-09  0000066740    1902
        1    AOS  A. O. Smith  Industrials  ...     2017-07-26  0000091142    1916
        2    ABT       Abbott  Health Care  ...     1964-03-31  0000001800    1888
        3   ABBV       AbbVie  Health Care  ...     2012-12-31  0001551152    2013
        4   ABMD      Abiomed  Health Care  ...     2018-05-31  0000815094    1981

        [5 rows x 8 columns]
        """
        return self.data(
            url_version="v3",
            path="sp500_constituent",
            params={"apikey": self.apikey},
        )

    @property
    def historical_sp500_companies(self):
        """Query FMP / sp500_constituent / API.

        Obtain most recent securities that have been
        either removed or added to the S&P 500.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> indexes = Indexes(apikey='abc123')
        >>>
        >>> historical_sp_500 = indexes.historical_sp500_companies
        >>> print(historical_sp_500.head())
                  dateAdded  ...                                             reason
        0  October 12, 2022  ...  Elliot Management Corp acquired Nielsen Holdings.
        1  October 12, 2022  ...  Elliot Management Corp acquired Nielsen Holdings.
        2   October 3, 2022  ...     Vista Equity Partners acquired Citrix Systems.
        3   October 3, 2022  ...     Vista Equity Partners acquired Citrix Systems.
        4   October 3, 2022  ...  S&P 500 constituent Prologis Inc. acquired Duk...

        [5 rows x 7 columns]
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

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> indexes = Indexes(apikey='abc123')
        >>>
        >>> nasdaq = indexes.nasdaq_companies
        >>> print(nasdaq.head())
          symbol                 name  ...         cik     founded
        0   ATVI  Activision Blizzard  ...  0000718877  1983-06-10
        1   ADBE           Adobe Inc.  ...  0000796343  1986-01-08
        2    ADP                  ADP  ...  0000008670  1961-09-01
        3   ABNB               Airbnb  ...  0001559720  2020-12-10
        4   ALGN     Align Technology  ...  0001097149  2001-01-26

        [5 rows x 8 columns]
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

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> indexes = Indexes(apikey='abc123')
        >>>
        >>> historical_nasdaq = indexes.historical_nasdaq_companies
        >>> print(historical_nasdaq.head())
                   dateAdded addedSecurity  ... symbol                        reason
        0  December 21, 2020      Okta Inc  ...   OKTA  Market capitalization change
        1  December 21, 2020          None  ...   BMRN  Market capitalization change
        2  December 21, 2020          None  ...   EXPE  Market capitalization change
        3  December 21, 2020          None  ...  LBTYA  Market capitalization change
        4  December 21, 2020          None  ...  LBTYK  Market capitalization change

        [5 rows x 7 columns]
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

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> indexes = Indexes(apikey='abc123')
        >>>
        >>> dow_jones = indexes.dow_jones_companies
        >>> print(dow_jones.head())
          symbol                          name  ...         cik     founded
        0    CRM            Salesforce.Com Inc  ...  0001108524  2004-06-23
        1    WBA  Walgreens Boots Alliance Inc  ...  0001618921  2014-12-31
        2      V                      Visa Inc  ...  0001403161  2008-03-19
        3    NKE                      Nike Inc  ...  0000320187  1990-10-17
        4    UNH        UnitedHealth Group Inc  ...  0000731766  1984-10-17

        [5 rows x 8 columns]
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

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> indexes = Indexes(apikey='abc123')
        >>>
        >>> historical_dow_jones = indexes.historical_dow_jones_companies
        >>> print(historical_dow_jones.head())
                 dateAdded  ...                         reason
        0  August 31, 2020  ...  Market capitalization change.
        1  August 31, 2020  ...   Market capitalization change
        2  August 31, 2020  ...   Market capitalization change
        3  August 31, 2020  ...  Market capitalization change.
        4  August 31, 2020  ...   Market capitalization change

        [5 rows x 7 columns]
        """
        return self.data(
            url_version="v3",
            path="historical/dowjones_constituent",
            params={"apikey": self.apikey},
        )
