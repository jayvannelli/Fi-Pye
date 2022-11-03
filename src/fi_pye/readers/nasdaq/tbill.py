from .reader import NasdaqReader
from .utils import (
    _validate_tbills_duration,
    _validate_tbill_duration,
    _validate_yield_duration,
    _validate_dates,
)


class Treasuries(NasdaqReader):
    """ """
    def tbill_rates(self, limit: int = 25):
        """ """
        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "rows": limit,
                "api_key": self.api_key
            },
        )

    def tbill_discount_rate(self, duration: str, limit: int = 25):
        """Query a specific duration discount rate.


        """
        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "column_index": _validate_tbills_duration(duration, "discount-rate"),
                "rows": limit,
                "api_key": self.api_key
            },
        )

    def tbill_coupon_rate(self, duration: str, limit: int = 25):
        """Query a specific duration coupon rate.


        """
        return self.data(
            path="USTREASURY/BILLRATES",
            params={
                "column_index": _validate_tbills_duration(duration, "coupon-rate"),
                "rows": limit,
                "api_key": self.api_key,
            },
        )

    def real_yield(self, duration: str, limit: int = 25):
        """Get all historical real Constant Maturity Treasury (CMT) rates.
        """
        valid_durations = ["5yr", "7yr", "10yr", "20yr", "30yr"]
        if duration not in valid_durations:
            raise ValueError(f"invalid duration: {duration}. Valid durations include: {valid_durations}. ")

        return self.data(
            path="USTREASURY/REALYIELD",
            params={
                "column_index": _validate_yield_duration(duration),
                "rows": limit,
                "api_key": self.api_key
            },
        )