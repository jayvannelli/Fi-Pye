from .reader import FmpReader


class Institutions(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    institutional investors.

    Institutions
    ------------
    - List of all institutions (with name & CIK number)
    - Institution search (by name)
    - Available dates
    - Portfolio summary
    - Portfolio composition
    - Portfolio industry summary

    Examples
    --------
    """
    @property
    def institution_list(self):
        """Query FMP / institutional-ownership/list / API.

        Returns list of all institutions with their name
        and CIK number.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> institutions = Institutions(apikey='abc123') # Initialize data source
        >>>
        >>> all_institutions = institutions.institution_list
        >>> print(all_institutions.head())
                     cik                                        name
        0     0001511144                      10-15 ASSOCIATES, INC.
        1     0001602119                           1060 CAPITAL, LLC
        2     0001580250           1060 CAPITAL OPPORTUNITY FUND, LP
        3     0001801172                      11 CAPITAL PARTNERS LP
        4     0001633703   12TH STREET ASSET MANAGEMENT COMPANY, LLC
        ...

        [9691 rows x 2 columns]
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/list",
            params={"apikey": self.apikey},
        )

    def search_for_institution(self, institution: str):
        """Query FMP / institutional-ownership/name / API.

        Search for a specific institution (by its name), if found
        it will return the given institutions name and CIK number.
        If the given institution wasn't found, whether because of
        typo or an invalid institution name, it will return None.

        Parameters
        ----------
        institution :
            Institution name

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> institutions = Institutions(apikey='abc123') # Initialize data source
        >>>
        >>> search_result = institutions.search_for_institution("Berkshire Hathaway")
        >>> print(search_result)
                  cik                    name
        0  0001067983  BERKSHIRE HATHAWAY INC
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/name",
            params={
                "name": institution,
                "apikey": self.apikey
            },
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

        Example
        --------
        >>> institutions = Institutions(apikey='abc123') # Initialize data source
        >>>
        >>> brk_dates = institutions.available_dates("0001067983") # Berkshire Hathaway Inc.
        >>> print(brk_dates.head())
                 date
        0  2022-06-30
        1  2022-03-31
        2  2021-12-31
        3  2021-09-30
        4  2021-06-30
        ...

        **Returns valid dates for use in portfolio composition, summary and summary by industry queries**

        >>> brk_portfolio_composition = institutions.portfolio_composition("0001067983", brk_dates[0])
        >>> print(brk_portfolio_composition)
                 date  ... performanceSinceInceptionRelativeToSP500Percentage
        0  2022-06-30  ...                                            37.1291

        [1 rows x 33 columns]


        >>> brk_portfolio_summary = institutions.portfolio_summary("0001067983", brk_dates[0])
        >>> print(brk_portfolio_summary)
                 date  ... performanceSinceInceptionRelativeToSP500Percentage
        0  2022-06-30  ...                                            37.1291

        [1 rows x 33 columns]

        >>> brk_portfolio_industry_summary = institutions.portfolio_industry_summary("0001067983", brk_dates[0])
        >>> print(brk_portfolio_industry_summary.head())
                 date         cik  ... lastPerformance changeInPerformance
        0  2022-06-30  0001067983  ...   -3.184817e+09       -3.057227e+10
        1  2022-06-30  0001067983  ...   -3.722444e+09       -7.779535e+09
        2  2022-06-30  0001067983  ...    1.288000e+09       -9.240000e+08
        3  2022-06-30  0001067983  ...    1.736325e+09       -4.609490e+09
        4  2022-06-30  0001067983  ...    3.462788e+09       -1.079771e+10

        [5 rows x 12 columns]
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/portfolio-date",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_summary(self, cik: str, date: str):
        """Query FMP / institutional-ownership/portfolio-holdings-summary / API.

        Returns summary of an institutions' portfolio.

        Parameters
        ----------
        cik :
            Institution CIK number
        date :
            Date to get portfolio summary from in 'YYYY-MM-DD' format

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
                "date": date,
                "apikey": self.apikey,
            },
        )

    def portfolio_composition(self, cik: str, date: str):
        """Query FMP / institutional-ownership/portfolio-holdings-summary / API.

        Returns detailed information about each position
        in an institutions' portfolio.


        Parameters
        ----------
        cik :
            Institution CIK number
        date :
            Date to get portfolio composition from in 'YYYY-MM-DD' format

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
                "date": date,
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
            Date to get portfolio industry summary from in 'YYYY-MM-DD' format

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