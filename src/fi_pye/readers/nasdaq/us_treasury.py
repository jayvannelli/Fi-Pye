from .reader import NasdaqReader
from .utils import _validate_limit


class USTreasury(NasdaqReader):
    """
    Query Nasdaq Data Link API endpoints related to the
    US Treasury dataset published by Quandl.

    US Treasury
    -----------

    """
    def tbill_rates(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/BILLRATES / API.

        Return Treasury Bill (TBILL) rates for the last x days.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return
        """
        return self.data(
            base="datasets",
            path="USTREASURY/BILLRATES",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def yield_curve(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.

        Parameters
        ----------
        limit : default = 25
            Number of rows to return
        """
        return self.data(
            base="datasets",
            path="USTREASURY/YIELD",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def real_yield_curve(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/REALYIELD / API.

        Return daily Treasury Par Real Yield Curve Rates.

        Real Yield Curve
        ----------------
        - 5 YR
        - 7YR
        - 10YR
        - 20YR
        - 30YR
        """
        return self.data(
            base="datasets",
            path="USTREASURY/REALYIELD",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def treasury_yield(self, treasury: str, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return treasury yield curve rate (by duration).
        """
        valid_values = [
            "1mo", "2mo", "3mo", "6mo", "1yr", "3yr",
            "5yr", "7yr", "10yr", "20yr", "30yr"
        ]
        if treasury not in valid_values or not isinstance(treasury, str):
            raise ValueError(f"Invalid treasury: {treasury}. Valid treasury values include: {valid_values}. ")

        return self.data(
            base="datasets",
            path="USTREASURY/YIELD",
            params={
                "column_index": valid_values.index(treasury)+1,
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def treasury_real_yield(self, treasury: str, limit: int = 25):
        """Query Nasdaq / USTREASURY/REALYIELD / API.

        """
        valid_values = [
            "5yr", "7yr", "10yr", "20yr", "30yr"
        ]
        if treasury not in valid_values or not isinstance(treasury, str):
            raise ValueError(f"Invalid treasury: {treasury}. Valid treasury values include: {valid_values}. ")

        return self.data(
            base="datasets",
            path="USTREASURY/REALYIELD",
            params={
                "column_index": valid_values.index(treasury)+1,
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )