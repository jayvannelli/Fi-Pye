from .reader import Reader


class ExchangeTradedFunds(Reader):
    """Exchange Traded Funds (ETF). """

    def available_dates(
            self,
            symbol: str = None,
    ):
        """List of available dates for fund (by symbol).


        Parameters
        ----------
            symbol : ETF symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="etf-holdings/portfolio-date",
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
            cik : ETF CIK number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="etf-holdings/portfolio-date",
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
            symbol : ETF symbol.
            date : Reporting date.

        ------
        Return : pandas DataFrame
        """
        return self.data(
            url_version="v4",
            path="etf-holdings",
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
            cik : ETF CIK number.
            date : Reporting date.

        ------
        Return : pandas DataFrame
        """
        return self.data(
            url_version="v4",
            path="etf-holdings",
            params={
                "cik": cik,
                "date": date,
                "apikey": self.apikey,
            },
        )

    def expense_ratio(
            self,
            symbol: str,
    ):
        """Obtain expense ratio info for fund (by symbol).


        Parameters
        ----------
            symbol : ETF symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="etf-info",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def country_weightings(
            self,
            symbol: str,
    ):
        """Obtain country exposure for fund (by symbol).


        Parameters
        ----------
            symbol : ETF symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path=f"etf-country-weightings/{symbol.upper()}",
            params={"apikey": self.apikey},
        )

    def sector_weightings(
            self,
            symbol: str,
    ):
        """Obtain sector exposure for fund (by symbol).


        Parameters
        ----------
            symbol : ETF symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path=f"etf-sector-weightings/{symbol.upper()}",
            params={"apikey": self.apikey},
        )
