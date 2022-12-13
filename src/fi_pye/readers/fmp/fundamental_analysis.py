from .reader import FmpReader


class FundamentalAnalysis(FmpReader):
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
    - Historical DCF (daily/quarterly/annual) valuation
    - Advanced DCF valuation
    - Advanced levered DCF valuation

    Examples
    --------
    >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> crm_financial_ratios = fundamental_analysis.financial_ratios("CRM")
        """
        return self.data(
            url_version="v3",
            path=f"ratios/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period
            }
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> amd_enterprise_value = fundamental_analysis.enterprise_value("AMD")
        """
        return self.data(
            url_version="v3",
            path=f"enterprise-values/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period
            }
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> mmm_financial_score = fundamental_analysis.financial_score("MMM")
        """
        return self.data(
            url_version="v4",
            path="score",
            params={"symbol": symbol.upper()}
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> acn_owner_earnings = fundamental_analysis.owner_earnings("ACN")
        """
        return self.data(
            url_version="v4",
            path="owner_earnings",
            params={"symbol": symbol.upper()}
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> msft_ttm_ratios = fundamental_analysis.ttm_ratios("MSFT")
        """
        return self.data(
            url_version="v4",
            path=f"ratios-ttm/{symbol.upper()}",
            params=None,
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> aapl_key_metrics = fundamental_analysis.key_metrics("AAPL")
        """
        return self.data(
            url_version="v3",
            path=f"key-metrics/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period
            }
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> bynd_key_metrics_ttm = fundamental_analysis.key_metrics_ttm("BYND")
        """
        return self.data(
            url_version="v3",
            path=f"key-metrics-ttm/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period
            }
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> nike_financial_growth = fundamental_analysis.financial_growth("NKE")
        """
        return self.data(
            url_version="v3",
            path=f"financial-growth/{symbol.upper()}",
            params={
                "limit": limit,
                "period": period
            }
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> dis_dcf = fundamental_analysis.discounted_cash_flow("DIS")
        """
        return self.data(
            url_version="v3",
            path=f"discounted-cash-flow/{symbol.upper()}",
            params=None,
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> tmo_historical_daily_dcf = fundamental_analysis.historical_daily_dcf("TMO")
        """
        return self.data(
            url_version="v3",
            path=f"historical-daily-discounted-cash-flow/{symbol.upper()}",
            params={"limit": limit}
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> pep_historical_dcf = fundamental_analysis.historical_dcf("PEP", period="quarter")
        """
        return self.data(
            url_version="v3",
            path=f"historical-discounted-cash-flow-statement/{symbol.upper()}",
            params={
                "period": period,
                "limit": limit
            }
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> meta_advanced_dcf = fundamental_analysis.advanced_dcf("META")
        """
        return self.data(
            url_version="v4",
            path="advanced_discounted_cash_flow",
            params={"symbol": symbol.upper()}
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

        Examples
        --------
        >>> fundamental_analysis = FundamentalAnalysis(apikey="abc123") # Initialize data source
        >>>
        >>> ko_advanced_levered_dcf = fundamental_analysis.advanced_levered_dcf("KO")
        """
        return self.data(
            url_version="v4",
            path="advanced_levered_discounted_cash_flow",
            params={"symbol": symbol.upper()}
        )
