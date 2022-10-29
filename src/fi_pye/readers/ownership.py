from .reader import Reader


class Ownership(Reader):
    """Stock institutional ownership. """
    def institutional_ownership(
            self,
            symbol: str,
    ):
        """Stock institutional ownership stats."""
        return self.data(
            url_version="v4",
            path="institutional-ownership/symbol-ownership",
            params={
                "symbol": symbol.upper(),
                "includeCurrentQuarter": "true",
                "apikey": self.apikey,
            },
        )

    def ownership_by_holders(
            self,
            symbol: str,
            report_date: str = "2021-09-30",
            page: int = 0,
    ):
        """Stock ownership by holders (largest to smallest) for a given report date."""
        return self.data(
            url_version="v4",
            path="institutional-ownership/institutional-holders/symbol-ownership-percent",
            params={
                "symbol": symbol.upper(),
                "date": report_date,
                "page": page,
                "apikey": self.apikey,
            },
        )

    def ownership_by_portfolio_weight(
            self,
            symbol: str,
            report_date: str = "2021-09-30",
            page: int = 0,
    ):
        """Stock ownership by portfolio weight (largest to smallest) for a given report date."""
        return self.data(
            url_version="v4",
            path="institutional-ownership/institutional-holders/symbol-ownership",
            params={
                "symbol": symbol.upper(),
                "date": report_date,
                "page": page,
                "apikey": self.apikey,
            },
        )
