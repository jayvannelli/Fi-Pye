from .reader import NasdaqReader
from .utils import (
    _validate_dates,
    _validate_limit,
)


class Treasuries(NasdaqReader):

    def real_long_term_avg_rate(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/REALLONGTERM / API.

        Returns daily Treasury Real Average Long-Term (10> Yrs) Rate.
        """
        return self.data(
            path="USTREASURY/REALLONGTERM",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def long_term_rates(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/LONGTERMRATES / API.

        Returns daily Treasury Long-Term Average Rates (10yr & 20yr)
        and Extrapolation Factors.
        """
        return self.data(
            path="USTREASURY/LONGTERMRATES",
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
            path="USTREASURY/REALYIELD",
            params={
                "column_index": valid_values.index(treasury)+1,
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def yield_curve(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.

        Real Yield Curve
        ----------------
            Bonds with duration < 1 YR
        - 1 MO
        - 2 MO
        - 3 MO
        - 6 MO

            Bonds with duration > 1 YR
        - 1 YR
        - 2 YR
        - 3 YR
        - 5 YR
        - 7YR
        - 10YR
        - 20YR
        - 30YR
        """
        return self.data(
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
            path="USTREASURY/REALYIELD",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def treasury_real_yield_curve_rate(self, treasury: str, limit: int = 25):
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
        valid_values = ["5yr", "7yr", "10yr", "20yr", "30yr"]
        return self.data(
            path="USTREASURY/REALYIELD",
            params={
                "column_index": valid_values.index(treasury)+1,
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def marketable_borrowing(self, type: str, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        valid_values = ["bills", "2-5", "5-10", ">10", "5-10 tips", ">10 tips", "buybacks"]
        return self.data(
            path="USTREASURY/TMBOR",
            params={
                "column_index": valid_values.index(type)+1,
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def net_marketable_borrowing(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        return self.data(
            path="USTREASURY/TMBOR",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def net_non_marketable_borrowing(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/TNMBOR / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        return self.data(
            path="USTREASURY/TNMBOR",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def non_marketable_borrowing(self, type: str, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        valid_values = ["foreign series", "slgs", "savings bond", "total"]
        return self.data(
            path="USTREASURY/TNMBOR",
            params={
                "column_index": valid_values.index(type)+1,
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def custom_yield_curve(self, from_date: str, to_date: str):
        """Return full treasury yield curve rates between a specified timeframe. """
        start, end = _validate_dates(from_date, to_date)
        return self.data(
            path="USTREASURY/YIELD",
            params={
                "start_date": start,
                "end_date": end,
                "api_key": self.api_key,
            },
        )

    def custom_real_yield_curve(self, from_date: str, to_date: str):
        """Return full treasury yield curve rates between a specified timeframe. """
        start, end = _validate_dates(from_date, to_date)
        return self.data(
            path="USTREASURY/YIELD",
            params={
                "start_date": start,
                "end_date": end,
                "api_key": self.api_key,
            },
        )

    def marketable_issuance_breakdown(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        return self.data(
            path="USTREASURY/BRDNM",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def hqm(self, limit: int = 25):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        return self.data(
            path="USTREASURY/HQMYC",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )


class TBill(NasdaqReader):
    """ """
    def tbill_rates(self, limit: int = 25):
        """ """
        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def tbill_discount_rate(self, duration: str, limit: int = 25):
        """Query a specific duration discount rate.

        """
        valid_values = ["4wk", "8wk", "13wk", "26wk", "52wk"]

        if duration not in valid_values or not isinstance(duration, str):
            raise ValueError(f"Invalid duration: {duration}. Valid durations include: {valid_values}. ")

        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "column_index": valid_values.index(duration),
                "rows": _validate_limit(limit),
                "api_key": self.api_key
            },
        )

    def tbill_coupon_rate(self, duration: str, limit: int = 25):
        """Query a specific duration coupon rate.


        """
        valid_values = ["4wk", "8wk", "13wk", "26wk", "52wk"]

        if duration not in valid_values or not isinstance(duration, str):
            raise ValueError(f"Invalid duration: {duration}. Valid durations include: {valid_values}. ")

        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "column_index": valid_values.index(duration)+1,
                "rows": _validate_limit(limit),
                "api_key": self.api_key,
            },
        )