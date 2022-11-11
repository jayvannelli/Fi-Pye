from .reader import NasdaqReader
from .utils import (
    _validate_limit,
    _validate_timeframe,
)


class SP500Ratios(NasdaqReader):
    """
    Query Nasdaq Data Link API endpoints related to the
    SP500 Ratios dataset published by Quandl.
    """
    def shiller_pe(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SHILLER_PE_RATIO / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SHILLER_PE_RATIO_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def dividend(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_DIV / API.

        Return SP5000 12-month real dividend per share (inflation adjusted).

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_DIV_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def earnings(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_EARNINGS / API.

        Return SP5000 12-month real dividend per share (inflation adjusted).

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_EARNINGS_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def inflation_adjusted(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_INFLADJ / API.

        Return SP5000 12-month real dividend per share (inflation adjusted).

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_INFLADJ_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def dividend_yield(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_DIV_YIELD / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_DIV_YIELD_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def earnings_yield(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_EARNINGS_YIELD / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_EARNINGS_YIELD_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def dividend_growth(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_DIV_YIELD / API.

        Return SP5000 dividend growth rate (not inflation adjusted).

        Parameters
        ----------
        timeframe :
            Either 'quarter' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_DIV_GROWTH_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def earnings_growth(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_EARNINGS_GROWTH / API.

        Return SP5000 dividend growth rate (not inflation adjusted).

        Parameters
        ----------
        timeframe :
            Either 'quarter' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_EARNINGS_GROWTH_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def book_value_per_share(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_BVPS / API.

        Parameters
        ----------
        timeframe :
            Either 'quarter' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_BVPS_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def price_to_book_value(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_PBV_RATIO / API.

        Parameters
        ----------
        timeframe :
            Either 'quarter' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_PBV_RATIO_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def price_to_earnings(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_PE_RATIO / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_PE_RATIO_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def price_to_sales(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_PSR_RATIO / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_PSR_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def real_earnings_growth(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_REAL_EARNINGS_GROWTH / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_REAL_EARNINGS_GROWTH_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def sales(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_SALES / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_SALES_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def real_sales(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_REAL_SALES / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_REAL_SALES_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def sales_growth(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_SALES_GROWTH / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_SALES_GROWTH_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def real_sales_growth(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_REAL_SALES_GROWTH / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_REAL_SALES_GROWTH_{_validate_timeframe(timeframe, True).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def real_price(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SP500_REAL_PRICE / API.

        Parameters
        ----------
        timeframe :
            Either 'month' or 'year'.
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path=f"MULTPL/SP500_REAL_PRICE_{_validate_timeframe(timeframe).upper()}",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )
