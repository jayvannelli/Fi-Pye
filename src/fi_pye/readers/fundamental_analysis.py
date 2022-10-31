from .reader import Reader


class FundamentalAnalysis(Reader):
    """
    Query Financial Modeling Prep API endpoints related to
    stock 'fundamental analysis'.

    Fundamental Analysis
    -------------------
    - Financial ratios
    - Enterprise value
    - Financial scores
    - Owner earnings
    - Trailing twelve month (TTM) ratios
    - Key metrics
    - Key metrics TTM
    - Financial growth
    - Discounted cash flow (DCF) valuation
    - Advanced DCF valuation
    - Advanced levered DCF valuation
    - Historical DCF (daily/quarterly/annual) valuation
    """
    def financial_ratios(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / ratios / API.

        Obtain stock financial ratios.

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
            path=f"ratios/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def enterprise_value(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / enterprise-values / API.

        Obtain stock enterprise value.

        The enterprise value is a proportion of an organization's absolute worth
        defined in terms of financing and is calculated using the following formula :
            Enterprise Value = Market Cap - Cash and Cash Equivalents + Total Debt.

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
            path=f"enterprise-values/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def financial_score(self, symbol: str):
        """Query FMP / score / API.

        Obtain stock financial score.

        Financial scores returned from this endpoint are
        based on the Altman Z-Score and Piotroski Score.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="score",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def owner_earnings(self, symbol: str):
        """Query FMP / owner_earnings / API.

        Obtain stock owners earnings.

        The owners earnings is a valuation method detailed by
        Warren Buffet that states the value of a company is the
        total of new cash flows expected to occur over the life
        of the business, minus any reinvestment of earnings.

        Owners earnings is calculated with the following formula :
            Owners Earnings = Operating Cash Flow + Maintenance Capex

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="owner_earnings",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def ttm_ratios(self, symbol: str):
        """Query FMP / ratios-ttm / API.

        Obtain stock trailing twelve months (TTM) ratios.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path=f"ratios-ttm/{symbol.upper()}",
            params={
                "apikey": self.apikey,
            },
        )

    def key_metrics(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / key-metrics / API.

        Obtain stock key metrics.

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
            path=f"key-metrics/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def key_metrics_ttm(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / key-metrics-ttm / API.

        Obtain stock trailing twelve months (TTM) key metrics.

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
            path=f"key-metrics-ttm/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def financial_growth(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / financial-growth / API.

        Obtain stock financial statement growth.

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
            path=f"financial-growth/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period,
                "apikey": self.apikey,
            },
        )

    def discounted_cash_flow(self, symbol: str):
        """Query FMP / discounted-cash-flow / API.

        Obtain current stock discounted cash flow (DCF) valuation.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"discounted-cash-flow/{symbol.upper()}",
            params={"apikey": self.apikey},
        )

    def historical_daily_dcf(self, symbol: str, limit: int = 25):
        """Query FMP / historical-discounted-cash-flow-statement / API.

        Obtain historical stock discounted cash flow (DCF) valuations on a daily basis.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"historical-daily-discounted-cash-flow/{symbol.upper()}",
            params={
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def historical_dcf(self, symbol: str, period: str = "annual", limit: int = 25):
        """Query FMP / historical-discounted-cash-flow-statement / API.

        Obtain historical stock discounted cash flow (DCF)
        valuations on a quarterly or annual basis.

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
            path=f"historical-discounted-cash-flow-statement/{symbol.upper()}",
            params={
                "period": period,
                "limit": limit,
                "apikey": self.apikey,
            },
        )

    def advanced_dcf(self, symbol: str):
        """
        Query FMP / advanced_discounted_cash_flow / API.

        Obtain stock advanced discounted cash flow (DCF) projection.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="advanced_discounted_cash_flow",
            params={"symbol": symbol.upper(), "apikey": self.apikey},
        )

    def advanced_levered_dcf(self, symbol: str):
        """Query FMP / advanced_levered_discounted_cash_flow / API.

        Obtain stock advanced discounted cash flow (DCF) projection including WACC.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="advanced_levered_discounted_cash_flow",
            params={"symbol": symbol.upper(), "apikey": self.apikey},
        )
