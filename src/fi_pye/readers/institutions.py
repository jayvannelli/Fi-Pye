from .reader import Reader


class Institutions(Reader):
    """ """
    @property
    def institution_list(self):
        """List of institutions with CIK & name."""
        return self.data(
            url_version="v4",
            path="institutional-ownership/list",
            params={"apikey": self.apikey},
        )

    def available_dates(self, cik: str):
        """Query FMP / institutional-ownership/portfolio-date / API.

        Returns a list of available dates for an institution (by CIK number)
        which can be used in the func 'portfolio_holdings'.

        Parameters
        ----------
        cik :
            Institution CIK number
            (Ex. Berkshire Hathaway Inc = '0001067983')

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/portfolio-date",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_summary(self, cik: str):
        """Query FMP / institutional-ownership/portfolio-holdings-summary / API.

        Returns summary of an institutions' portfolio.

        Parameters
        ----------
        cik :
            Institution CIK number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/portfolio-holdings-summary",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_composition(self, cik: str):
        """Query FMP / institutional-ownership/portfolio-holdings-summary / API.

        Returns detailed information about each position
        in an institutions' portfolio.


        Parameters
        ----------
        cik :
            Institution CIK number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/portfolio-holdings-summary",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_industry_summary(self, cik: str, date: str):
        """Query FMP / institutional-ownership/industry/portfolio-holdings-summary / API.

        Returns a summary for each industry within an institutions portfolio

        Parameters
        ----------
        cik :
            Institution CIK number
        date :
            Date to get portfolio holdings from in 'YYYY-MM-DD' format

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/industry/portfolio-holdings-summary",
            params={
                "cik": cik,
                "date": date,
                "apikey": self.apikey,
            },
        )