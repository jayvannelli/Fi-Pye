from .reader import NasdaqReader
from .utils import _validate_limit


class USTreasury(NasdaqReader):
    """
    Query Nasdaq Data Link API endpoints related to the
    US Treasury dataset published by Quandl.

    US Treasury
    -----------
    - Treasury Bill (TBILL) Rates
    - Treasury Yield Curve Rates
    - Treasury Real Yield Curve Rates

    """
    def tbill_rates(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/BILLRATES / API.

        Return daily Treasury Bill (TBILL) rates for the last x days.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="USTREASURY/BILLRATES",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def yield_curve(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return daily Treasury Yield Curve Rates for the last x days.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="USTREASURY/YIELD",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def real_yield_curve(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/REALYIELD / API.

        Return daily Treasury Par Real Yield Curve Rates for the last x days.

        Real Yield Curve
        ----------------
        - 5 YR
        - 7YR
        - 10YR
        - 20YR
        - 30YR

        Parameters
        ----------
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            base="datasets",
            path="USTREASURY/REALYIELD",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def treasury_yield(self, duration: str, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return daily Treasury Yield Curve Rates for the last x days (by duration).

        Parameters
        ----------
        duration : str
            Duration of Treasury (
                '1mo', '2mo', '3mo', '1yr', '3yr',
                '5yr', '7yr', '10yr', '20yr', '30yr'
            )
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        valid_values = [
            "1mo", "2mo", "3mo", "6mo", "1yr", "3yr",
            "5yr", "7yr", "10yr", "20yr", "30yr"
        ]
        if duration not in valid_values or not isinstance(duration, str):
            raise ValueError(
                f"Invalid duration: {duration}. "
                f"Valid treasury yield durations include: {valid_values}."
            )

        return self.data(
            base="datasets",
            path="USTREASURY/YIELD",
            params={
                "column_index": valid_values.index(duration)+1,
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )

    def treasury_real_yield(self, duration: str, limit: int = 25):
        """Query Nasdaq / USTREASURY/REALYIELD / API.

        Return daily Treasury Real Yield Curve Rates for the last x days (by duration).

        Parameters
        ----------
        duration : str
            Duration of Treasury ('5yr', '7yr', '10yr', '20yr' or '30yr')
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        valid_values = ["5yr", "7yr", "10yr", "20yr", "30yr"]
        if duration not in valid_values or not isinstance(duration, str):
            raise ValueError(
                f"Invalid duration: {duration}. "
                f"Valid treasury real yield durations include: {valid_values}."
            )

        return self.data(
            base="datasets",
            path="USTREASURY/REALYIELD",
            params={
                "column_index": valid_values.index(duration)+1,
                "rows": _validate_limit(limit),
                "api_key": self.apikey
            },
        )