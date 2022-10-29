from .reader import Reader


class Performance(Reader):
    """ """

    @property
    def biggest_gainers(self):
        """List of current biggest one day gainers (intraday gain in %). """
        return self.data(
            url_version="v3",
            path="stock_market/gainers",
            params={"apikey": self.apikey},
        )

    @property
    def biggest_losers(self):
        """List of current biggest one day losers (intraday drop in %). """
        return self.data(
            url_version="v3",
            path="stock_market/losers",
            params={"apikey": self.apikey},
        )

    @property
    def most_active(self):
        """List of most active stocks (by intraday volume). """
        return self.data(
            url_version="v3",
            path="stock_market/actives",
            params={"apikey": self.apikey},
        )

    @property
    def sector_performance(self):
        """Current market performance (in % change) by sector. """
        return self.data(
            url_version="v3",
            path="sector-performance",
            params={"apikey": self.apikey},
        )

    def historical_sector_performance(
            self,
            limit: int,
    ):
        """Historical market performance (in % change) by sector. """
        return self.data(
            url_version="v3",
            path="historical-sectors-performance",
            params={
                "limit": limit,
                "apikey": self.apikey
            },
        )

    def sectors_pe_ratio(
            self,
            date: str,
            exchange: str = "NYSE",
    ):
        """ """
        return self.data(
            url_version="v4",
            path="sector_price_earning_ratio",
            params={
                "date": date,
                "exchange": exchange,
                "apikey": self.apikey,
            }
        )

    def industries_pe_ratio(
            self,
            date: str,
            exchange: str = "NYSE",
    ):
        """ """
        return self.data(
            url_version="v4",
            path="industry_price_earning_ratio",
            params={
                "date": date,
                "exchange": exchange,
                "apikey": self.apikey,
            }
        )