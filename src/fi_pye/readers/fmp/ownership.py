from .reader import FmpReader


class Ownership(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    stock ownership.

    Ownership
    ---------
    - Institutional
    - By holders
    - By position size (in %) of portfolio

    Examples
    --------
    >>> ownership = Ownership(apikey="abc123")
    """

    def institutional_ownership_stats(self, symbol: str):
        """Query FMP / institutional-ownership/symbol-ownership / API.

        Returns institutional ownership stats for a given stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> ownership = Ownership(apikey="abc123")
        >>>
        >>> aapl_institutional_ownership_stats = ownership.institutional_ownership_stats("AAPL")
        >>> print(aapl_institutional_ownership_stats.head())
          symbol         cik  ... lastPutCallRatio  putCallRatioChange
        0   AAPL  0000320193  ...           0.0122              0.9614
        1   AAPL  0000320193  ...         448.3858           -448.3736
        2   AAPL  0000320193  ...           2.4155            445.9703
        3   AAPL  0000320193  ...         429.5140           -427.0985
        4   AAPL  0000320193  ...          22.3370            407.1769

        [5 rows x 36 columns]
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/symbol-ownership",
            params={
                "symbol": symbol.upper(),
                "includeCurrentQuarter": "true",
            }
        )

    def ownership_by_holders(self, symbol: str, report_date: str, page: int = 0):
        """Query FMP / institutional-ownership/institutional-holders/symbol-ownership-percent / API.

        Returns list of the largest institutional holders of a
        given stock (by symbol) in descending order.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        report_date :
            Date to get the largest holders from in 'YYYY-MM-DD' format
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> ownership = Ownership(apikey="abc123")
        >>>
        >>> aapl_largest_holders = ownership.ownership_by_holders("AAPL", "2021-09-30")
        >>> print(aapl_largest_holders.head())
                 date         cik  ... changeInPerformance isCountedForPerformance
        0  2021-09-30  0000102909  ...       -1.256115e+10                    True
        1  2021-09-30  0001364742  ...       -1.092024e+10                    True
        2  2021-09-30  0001067983  ...       -9.077802e+09                    True
        3  2021-09-30  0000093751  ...       -6.376883e+09                    True
        4  2021-09-30  0000315066  ...       -3.503680e+09                    True

        [5 rows x 39 columns]
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/institutional-holders/symbol-ownership-percent",
            params={
                "symbol": symbol.upper(),
                "date": report_date,
                "page": page,
            }
        )

    def ownership_by_portfolio_weight(self, symbol: str, report_date: str, page: int = 0):
        """Query FMP / institutional-ownership/institutional-holders/symbol-ownership / API.

        Returns list of institutions with the largest amount of their
        portfolio weight of a given stock (by symbol) in descending order.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        report_date :
            Date to get the largest holders from in 'YYYY-MM-DD' format
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> ownership = Ownership(apikey="abc123")
        >>>
        >>> aapl_holders_by_weight = ownership.ownership_by_portfolio_weight("AAPL", "2021-09-30")
        >>> print(aapl_holders_by_weight.head())
                 date         cik  ... changeInPerformance isCountedForPerformance
        0  2021-09-30  0001308668  ...       -6.024222e+06                    True
        1  2021-09-30  0001545545  ...        2.345794e+04                    True
        2  2021-09-30  0001720350  ...       -7.162898e+06                    True
        3  2021-09-30  0001759760  ...       -3.415419e+08                    True
        4  2021-09-30  0001004244  ...       -2.094993e+08                    True

        [5 rows x 39 columns]
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/institutional-holders/symbol-ownership",
            params={
                "symbol": symbol.upper(),
                "date": report_date,
                "page": page,
            }
        )
