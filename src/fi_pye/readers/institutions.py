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

    def available_dates(
            self,
            cik: str,
    ):
        """List of available dates for a specific institution (by CIK).


        Parameters
        ----------
            cik : Institution CIK number.
                    EXAMPLE: Berkshire Hathaway Inc. = '0001067983'

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/portfolio-date",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_summary(
            self,
            cik: str,
    ):
        """Summary of a given institution's portfolio.


        Parameters
        ----------
            cik : Institution CIK number.
                    EXAMPLE: Berkshire Hathaway Inc. = '0001067983'

        ------
        Return : pandas DataFrame
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/portfolio-holdings-summary",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_composition(
            self,
            cik: str,
    ):
        """Detailed information about each position in an institutions' portfolio.


        Parameters
        ----------
            cik : Institution CIK number.
                    EXAMPLE: Berkshire Hathaway Inc. = '0001067983'

        ------
        Return : pandas DataFrame
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/portfolio-holdings-summary",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_industry_summary(
            self,
            cik: str,
            date: str,
    ):
        """Summary of a given institution's portfolio (broken down by industry).


        Parameters
        ----------
            cik : Institution CIK number.
                    EXAMPLE: Berkshire Hathaway Inc. = '0001067983'
            date: Filing date.

        ------
        Return : pandas DataFrame
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