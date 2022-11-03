from .reader import FmpReader


class ExchangeTradedFunds(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related
    to Exchange traded Funds (ETFs).

    *The available dates endpoints returns a list of valid date
    values for a specific ETF, which can then be passed as the
    'date' parameter in the portfolio holdings methods.

    ETFs
    ----
    - Available dates, by symbol or CIK number
    - Portfolio holdings, by symbol or CIK number
    - ETF specific data(expense ratio & country/sector weightings)
    """

    def available_dates(self, symbol: str):
        """Query FMP / etf-holdings/portfolio-date / API.

        Returns a list of available dates for an ETF (by symbol)
        which can be used in the func 'portfolio_holdings'.

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        --------
        >>> etfs = ExchangeTradedFunds(apikey='abc123') # Initialize data source
        >>>
        >>> gdx_dates = etfs.available_dates("GDX")
        >>> print(gdx_dates.head(3))
                 date
        0   2022-07-31
        1   2022-06-30
        2   2022-04-30
        ...

        **Returns valid dates for use in portfolio holdings query**

        >>> gdx_holdings_7_31_2022 = etfs.portfolio_holdings("GDX", date=gdx_dates[0])
        >>> print(gdx_holdings_7_31_2022.head())
                  cik       acceptanceTime  ... isNonCashCollateral isLoanByFund
        0  0001137360  2022-09-27 19:18:09  ...                   N            N
        1  0001137360  2022-09-27 19:18:09  ...                   N            N
        2  0001137360  2022-09-27 19:18:09  ...                   N            N
        3  0001137360  2022-09-27 19:18:09  ...                   N            N
        4  0001137360  2022-09-27 19:18:09  ...                   N            N

        [5 rows x 23 columns]
        """
        return self.data(
            url_version="v4",
            path="etf-holdings/portfolio-date",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def available_dates_by_cik(self, cik: str):
        """Query FMP / etf-holdings/portfolio-date / API.

        Returns a list of available dates for an ETF (by CIK number)
        which can be used in the func 'portfolio_holdings'.

        Parameters
        ----------
        cik :
            Exchange Traded Fund (ETF) CIK number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        --------
        >>> etfs = ExchangeTradedFunds(apikey='abc123') # Initialize data source
        >>>
        >>> spy_dates = etfs.available_dates("SPY")
        """
        return self.data(
            url_version="v4",
            path="etf-holdings/portfolio-date",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_holdings(self, symbol: str, date: str):
        """Query FMP / etf-holdings / API.

        Returns the portfolio holdings of a specified ETF (by symbol)
        and on a given date. To get available dates for a specific
        ETF, query 'available_dates' or 'available_dates_by_cik'.

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol
        date :
            Date to get portfolio holdings from in 'YYYY-MM-DD' format

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        --------

        **When the 'date' query is already known**

        >>> etfs = ExchangeTradedFunds(apikey='abc123') # Initialize data source
        >>>
        >>> xlk_holdings_6_30_2022 = etfs.portfolio_holdings("XLK", "2022-06-30")
                  cik       acceptanceTime        date  ... isCashCollateral isNonCashCollateral isLoanByFund
        0  0001064641  2022-08-26 13:27:00  2022-06-30  ...                N                   N            Y
        1  0001064641  2022-08-26 13:27:00  2022-06-30  ...                N                   N            N
        2  0001064641  2022-08-26 13:27:00  2022-06-30  ...                N                   N            N
        3  0001064641  2022-08-26 13:27:00  2022-06-30  ...                N                   N            N
        4  0001064641  2022-08-26 13:27:00  2022-06-30  ...                N                   N            N

        **When the 'date' query is NOT known, use available dates method**

        >>> etfs = ExchangeTradedFunds(apikey='abc123') # Initialize data source
        >>>
        >>> xlk_dates = etfs.available_dates("XLK")
        >>> print(xlk_dates.head(2))
                  date
        0   2022-06-30
        1   2022-03-31

        >>> xlk_holdings_3_31_2022 = etfs.portfolio_holdings("XLK", xlk_dates[1])
        >>> print(xlk_holdings_3_31_2022.head())
                  cik       acceptanceTime        date symbol  ... fairValLevel isCashCollateral isNonCashCollateral isLoanByFund
        0  0001064641  2022-05-27 13:54:30  2022-03-31    DFS  ...            1                N                   N            N
        1  0001064641  2022-05-27 13:54:30  2022-03-31    AIZ  ...            1                N                   N            N
        2  0001064641  2022-05-27 13:54:30  2022-03-31    BLK  ...            1                N                   N            N
        3  0001064641  2022-05-27 13:54:30  2022-03-31    CMA  ...            1                N                   N            N
        4  0001064641  2022-05-27 13:54:30  2022-03-31   MSCI  ...            1                N                   N            N

        [5 rows x 23 columns]
        """
        return self.data(
            url_version="v4",
            path="etf-holdings",
            params={
                "symbol": symbol.upper(),
                "date": date,
                "apikey": self.apikey,
            },
        )

    def portfolio_holdings_by_cik(self, cik: str, date: str):
        """Query FMP / etf-holdings / API.

        Returns the portfolio holdings of a specified ETF (by CIK number)
        and on a given date. To get available dates for a specific
        ETF, query 'available_dates' or 'available_dates_by_cik'.

        Parameters
        ----------
        cik :
            Exchange Traded Fund (ETF) CIK number
        date :
            Date to get portfolio holdings from in 'YYYY-MM-DD' format

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        --------
        >>> etfs = ExchangeTradedFunds(apikey='abc123') # Initialize data source
        >>>
        >>> spy_dates = etfs.available_dates("SPY")
        """
        return self.data(
            url_version="v4",
            path="etf-holdings",
            params={
                "cik": cik,
                "date": date,
                "apikey": self.apikey,
            },
        )

    def expense_ratio(self, symbol: str):
        """Query FMP / etf-holdings / API.

        Returns information about a given ETF (by symbol).

        Some ETF info returned:
            - Assets under management (AUM)
            - CUSIP
            - Description
            - ISIN
            - Net asset value (NAV)
            - ...

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        --------
        >>> etfs = ExchangeTradedFunds(apikey='abc123') # Initialize data source
        >>>
        >>> xle_expense_ratio = etfs.expense_ratio("XLE")
        >>> print(xle_expense_ratio)
          symbol  ... holdingsCount
        0    XLE  ...             0

        [1 rows x 17 columns]
        """
        return self.data(
            url_version="v4",
            path="etf-info",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def country_weightings(self, symbol: str):
        """Query FMP / etf-country-weightings / API.

        Returns specific ETF (by symbol) portfolio exposure by country.

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        --------
        >>> etfs = ExchangeTradedFunds(apikey='abc123') # Initialize data source
        >>>
        >>> veu_countries = etfs.country_weightings("VEU")
        >>> print(veu_countries)
                             country weightPercentage
        0                  Hong Kong           10.94%
        1                  Australia            4.55%
        2                Switzerland            6.51%
        3         Korea, Republic of            3.18%
        4                     France            6.56%
        5                      Japan           18.16%
        6                    Germany            5.78%
        7             United Kingdom            9.86%
        8  Taiwan, Province of China            3.34%
        9                     Canada            5.43%
        """
        return self.data(
            url_version="v3",
            path=f"etf-country-weightings/{symbol.upper()}",
            params={"apikey": self.apikey},
        )

    def sector_weightings(self, symbol: str):
        """Query FMP / etf-sector-weightings / API.

        Returns specific ETF (by symbol) portfolio exposure by sector.

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        --------
        >>> etfs = ExchangeTradedFunds(apikey='abc123') # Initialize data source
        >>>
        >>> spy_sectors = etfs.sector_weightings("SPY")
        >>> print(spy_sectors)
                            sector weightPercentage
        0              Real Estate            2.53%
        1        Consumer Cyclical           12.43%
        2          Basic Materials            2.34%
        3       Consumer Defensive             6.4%
        4               Technology           23.44%
        5   Communication Services           11.18%
        6       Financial Services           14.41%
        7                Utilities            2.64%
        8              Industrials            9.05%
        9                   Energy            2.68%
        10              Healthcare           12.89%
        """
        return self.data(
            url_version="v3",
            path=f"etf-sector-weightings/{symbol.upper()}",
            params={"apikey": self.apikey},
        )
