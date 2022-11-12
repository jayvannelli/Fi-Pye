from .reader import NasdaqReader
from .utils import (
    _validate_limit,
    _validate_timeframe,
)


class SP500Ratios(NasdaqReader):
    """
    Query Nasdaq Data Link API endpoints related to the
    SP500 Ratios dataset published by Quandl.

    Method descriptions are taken from the csv provided by
    Nasdaq under the 'usage' section of this dataset.
    """
    def shiller_pe(self, timeframe: str, limit: int = 25):
        """Query Nasdaq / MULTPL/SHILLER_PE_RATIO / API.

        Shiller PE ratio for the S&P 500. Price earnings ratio is based on average
        inflation-adjusted earnings from the previous 10 years, known as the
        Cyclically Adjusted PE Ratio (CAPE Ratio), Shiller PE Ratio, or PE 10 FAQ.
        Data courtesy of Robert Shiller from his book, Irrational Exuberance.

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

        12-month real dividend per share (inflation adjusted).
        Data courtesy Standard & Poor's and Robert Shiller.

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

        S&P 500 Earnings Per Share. 12-month real earnings per share (inflation adjusted).
        Sources: Standard & Poor's for current S&P 500 Earnings. Robert Shiller and his
        book Irrational Exuberance for historic S&P 500 Earnings.

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

        Inflation adjusted, constant September, 2022 dollars. Other than the current price,
        all prices are monthly average closing prices. Sources: Standard & Poor's Robert
        Shiller and his book Irrational Exuberance for historic S&P 500 prices, and historic CPIs.

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

        S&P 500 dividend yield (12 month dividend per share)/price. Yields are
        estimated based on 12 month dividends through the datasets' latest refresh
        date, as reported by S&P. Sources: Standard & Poor's for current S&P 500
        Dividend Yield. Robert Shiller and his book Irrational Exuberance for
        historic S&P 500 Dividend Yields.

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

        S&P 500 Earnings Yield. Earnings Yield = trailing 12 month earnings divided
        by index price (or inverse PE) Yields are estimated based on 12 month
        earnings through June, 2022 the latest reported by S&P. Source: Standard & Poor's

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

        S&P 500 dividend growth rate per year. Annual current dollars percentage
        change in 12 month dividend per share (not inflation adjusted).
        Source: Standard & Poor's

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

        S&P 500 earnings growth rate per year. Annual current dollars percentage change
        in 12 month earnings per share, (not inflation adjusted). Source: Standard & Poor's

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

        S&P 500 book value per share non-inflation adjusted current dollars.
        Source: Standard & Poor's

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

        S&P 500 price to book value ratio. Current price to book ratio is estimated
        based on current market price and S&P 500 book value as of the latest report
        by S&P. Source: Standard & Poor's

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

        Price to earnings ratio, based on trailing twelve month as reported earnings.
        Current PE is estimated from the latest reported earnings and current market
        price. Source: Robert Shiller and his book Irrational Exuberance for historic
        S&P 500 PE Ratio.

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

        S&P 500 Price to Sales Ratio (P/S or Price to Revenue). Current price to
        sales ratio is estimated based on current market price and 12 month sales ending
        on the datasets' latest refresh date. Source: Standard & Poor's

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

        S&P 500 real earnings growth rate per year. Annual percentage change in 12 month
        S&P 500 Real Earnings Per Share (inflation adjusted). Source: Standard & Poor's

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

        Trailing twelve month S&P 500 Sales Per Share (S&P 500 Revenue Per Share)
        non-inflation adjusted current dollars. Source: Standard & Poor's

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

        Trailing twelve month S&P 500 Sales Per Share (S&P 500 Revenue Per Share)
        inflation-adjusted to the datasets' latest refresh date. Source: Standard & Poor's

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

        S&P 500 sales growth rate per year. Annual percentage change in
        12 month S&P 500 Sales (not-inflation adjusted). Source: Standard & Poor's

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

        S&P 500 real sales growth rate per year. Annual percentage change in 12 month
        S&P 500 Real Sales (inflation adjusted). Source: Standard & Poor's

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

        S&P 500 historical prices. Prices are not inflation-adjusted. For inflation-adjusted
        comparison, see Inflation Adjusted S&P 500. Other than the current price, all prices
        are monthly average closing prices. Sources: Standard & Poor's Robert Shiller and
        his book Irrational Exuberance for historic S&P 500 prices, and historic CPIs.

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
