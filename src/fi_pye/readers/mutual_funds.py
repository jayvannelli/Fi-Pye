from .reader import Reader


class MutualFunds(Reader):
    """Mutual Funds. """

    def available_dates(
            self,
            symbol: str,
    ):
        """List of available dates for fund (by symbol).


        Parameters
        ----------
            symbol : Mutual fund symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="mutual-fund-holdings/portfolio-date",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def available_dates_by_cik(
            self,
            cik: str,
    ):
        """List of available dates for fund (by CIK number).


        Parameters
        ----------
            cik : Mutual fund CIK number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="mutual-fund-holdings/portfolio-date",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_holdings(
            self,
            symbol: str,
            date: str,
    ):
        """Summary of a given fund's portfolio (by symbol).


        Parameters
        ----------
            symbol : Mutual fund symbol.
            date : Reporting date.

        ------
        Return : pandas DataFrame
        """
        return self.data(
            url_version="v4",
            path="mutual-fund-holdings",
            params={
                "symbol": symbol.upper(),
                "date": date,
                "apikey": self.apikey,
            },
        )

    def portfolio_holdings_by_cik(
            self,
            cik: str,
            date: str,
    ):
        """Summary of a given fund's portfolio (by CIK number).


        Parameters
        ----------
            cik : Mutual fund CIK number.
            date : Reporting date.

        ------
        Return : pandas DataFrame
        """
        return self.data(
            url_version="v4",
            path="mutual-fund-holdings",
            params={
                "cik": cik,
                "date": date,
                "apikey": self.apikey,
            },
        )
