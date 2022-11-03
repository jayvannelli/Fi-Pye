from .reader import NasdaqReader
from .utils import (
    _validate_tbill_duration,
    _validate_yield_duration,
    _validate_treasury,
    _validate_dates,
    _validate_limit,
)


class Treasuries(NasdaqReader):

    def real_long_term_average_rate(self, limit=None):
        """ """
        return self.data(
            path="USTREASURY/REALLONGTERM",
            params={
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )

    def long_term_rates(self, limit=None):
        """ """
        return self.data(
            path="USTREASURY/LONGTERMRATES",
            params={
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )

    def tbill_rates(self, limit=None):
        """ """
        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )

    def treasury_yield(self, treasury: str, limit=None):
        """ """
        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "column_index": _validate_treasury(treasury),
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )

    def tbill_discount_rate(self, duration: str, limit=None):
        """Query a specific duration discount rate.

        """
        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "column_index": _validate_tbill_duration(duration, "discount-rate"),
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )

    def tbill_coupon_rate(self, duration: str, limit=None):
        """Query a specific duration coupon rate.


        """
        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "column_index": _validate_tbill_duration(duration, "coupon-rate"),
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key,
            },
        )

    def yield_curve(self, limit=None):
        """Query Nasdaq / USTREASURY/YIELD / API.

        Return Treasury Yield Curve Rates for the last x days.
        """
        return self.data(
            path="USTREASURY/YIELD",
            params={
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )

    def real_yield_curve(self, limit=None):
        """Get all historical real Constant Maturity Treasury (CMT) rates.
        """
        return self.data(
            path="USTREASURY/REALYIELD",
            params={
                "rows": _validate_limit(limit) or self.limit,
                "api_key": self.api_key
            },
        )

    def yield_curve_by_dates(self, from_date: str, to_date: str):
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

    def real_yield_curve_by_dates(self, from_date: str, to_date: str):
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