from .reader import Reader


class Fundamentals(Reader):
    """
    This can be used to access FMP's endpoints related to stock fundamentals,
    such as to get financial statements (cleaned or as reported) and financial
    statement growth on both a quarterly and/or annual basis.

    The apikey set during instantiation will be used as the default apikey
    for all methods within this class. To use a different api during a method
    call, simply pass one as an argument instead of leaving apikey = None.

    Examples
    --------
    >>> fundamentals = Fundamentals(apikey='abc123')
    >>>
    >>> TICKER = "AAPL"
    >>> PERIOD = "quarter"
    >>> LIMIT = 25
    >>>
    >>> inc_stmt = fundamentals.income_statement(TICKER, PERIOD, LIMIT)
    >>> bal_sheet = fundamentals.balance_sheet(TICKER, PERIOD, LIMIT)
    >>> cash_flow = fundamentals.cash_flow(TICKER, PERIOD, LIMIT)
    """
    def income_statement(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / income-statement / API.

        Obtain stock income statement(s).

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"income-statement/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def income_statement_growth(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / income-statement-growth / API.

        Obtain stock income statement(s) growth.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"income-statement-growth/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def income_statement_as_reported(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / income-statement / API.

        Obtain stock income statement(s) as reported.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"income-statement-as-reported/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def balance_sheet(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / balance-sheet-statement / API.

        Obtain stock balance sheet statement(s).

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"balance-sheet-statement/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def balance_sheet_growth(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / balance-sheet-statement-growth / API.

        Obtain stock balance sheet statement(s) growth.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"balance-sheet-statement-growth/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def balance_sheet_as_reported(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / balance-sheet-statement / API.

        Obtain stock balance sheet statement(s) as reported.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"balance-sheet-statement-as-reported/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def cash_flow(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / cash-flow-statement / API.

        Obtain stock cash flow sheet statement(s).

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"cash-flow-statement/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def cash_flow_growth(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / cash-flow-statement-growth / API.

        Obtain stock cash flow statement(s) growth.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"cash-flow-statement-growth/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def cash_flow_as_reported(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / cash-flow-statement / API.

        Obtain stock cash flow statement(s) as reported.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        period : default = 'annual'
            'quarter' or 'annual'
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"cash-flow-statement-as-reported/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )