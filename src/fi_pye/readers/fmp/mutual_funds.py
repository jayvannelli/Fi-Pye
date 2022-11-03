from .reader import FmpReader


class MutualFunds(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    Mutual funds.

    Mutual funds
    ------------
    - Available dates, by symbol or CIK number
    - Portfolio holdings, by symbol or CIK number
    """

    def available_dates(self, symbol: str):
        """Query FMP / mutual-fund-holdings/portfolio-date / API.

        Returns a list of available dates for a Mutual fund (by symbol)
        which can be used in the func 'portfolio_holdings'.

        Parameters
        ----------
        symbol :
            Mutual fund ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="mutual-fund-holdings/portfolio-date",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def available_dates_by_cik(self, cik: str):
        """Query FMP / mutual-fund-holdings/portfolio-date / API.

        Returns a list of available dates for a Mutual fund (by CIK number)
        which can be used in the func 'portfolio_holdings'.

        Parameters
        ----------
        cik :
            Mutual fund CIK number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="mutual-fund-holdings/portfolio-date",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_holdings(self, symbol: str, date: str):
        """Query FMP / mutual-fund-holdings / API.

        Returns the portfolio holdings of a specified Mutual fund (by symbol)
        and on a given date. To get available dates for a specific
        ETF, query 'available_dates' or 'available_dates_by_cik'.

        Parameters
        ----------
        symbol :
            Mutual fund ticker symbol
        date :
            Date to get portfolio holdings from in 'YYYY-MM-DD' format

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
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

    def portfolio_holdings_by_cik(self, cik: str, date: str):
        """Query FMP / mutual-fund-holdings / API.

        Returns the portfolio holdings of a specified Mutual fund (by CIK number)
        and on a given date. To get available dates for a specific
        ETF, query 'available_dates' or 'available_dates_by_cik'.

        Parameters
        ----------
        cik :
            Mutual fund CIK number
        date :
            Date to get portfolio holdings from in 'YYYY-MM-DD' format

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
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
