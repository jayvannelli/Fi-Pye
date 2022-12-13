from .reader import FmpReader


class PrivateCompanies(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    private companies.

    Private Companies
    -----------------
    - Crowdfunding offerings (by company name or CIK number)
    - Equity offerings (by company name or CIK number)

    Examples
    --------
    >>> private_companies = PrivateCompanies(apikey="abc123") # Initialize data source
    """

    def crowdfunding_offerings(self, company: str):
        """Query FMP / crowdfunding-offerings/search / API.

        Search for a specific private company (by name) undergoing a crowdfunding offering

        Parameters
        ----------
        company :
            Full company name.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        -------
        >>> private_companies = PrivateCompanies(apikey="abc123") # Initialize data source
        >>>
        >>> search_result = private_companies.crowdfunding_offerings('Enotap')
        >>> print(search_result)
                  cik        name                 date
        0  0001912939  Enotap LLC  2022-07-20 17:06:10
        1  0001912939  Enotap LLC  2022-04-19 10:21:38
        2  0001912939  Enotap LLC  2022-03-30 16:56:08
        3  0001912939  Enotap LLC  2022-03-09 14:58:03
        """
        return self.data(
            url_version="v4",
            path="crowdfunding-offerings/search",
            params={"name": company}
        )

    def crowdfunding_offerings_by_cik(self, cik: str):
        """Query FMP / crowdfunding-offerings / API.

        Search for a specific private company (by CIK) undergoing a crowdfunding offering

        Parameters
        ----------
        cik :
            Company CIK number.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        -------
        >>> private_companies = PrivateCompanies(apikey="abc123") # Initialize data source
        >>>
        >>> search_result = private_companies.crowdfunding_offerings_by_cik('0001916078')
        >>> print(search_result)
          formType  ... netIncomePriorFiscalYear
        0      C-U  ...                 -10860.0
        1     C-AR  ...                 -10860.0
        2        C  ...                 -10860.0

        [3 rows x 45 columns]
        """
        return self.data(
            url_version="v4",
            path="crowdfunding-offerings",
            params={"cik": cik}
        )

    def equity_offerings(self, company: str):
        """Query FMP / fundraising/search / API.

        Search for a specific private company (by name) undergoing an equity offering

        Parameters
        ----------
        company :
            Full company name.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        -------
        >>> private_companies = PrivateCompanies(apikey="abc123") # Initialize data source
        >>>
        >>> search_result = private_companies.equity_offerings('marinalife')
        >>> print(search_result)
                  cik              name                 date
        0  0001870523  Marinalife, Inc.  2022-07-25 14:13:21
        """
        return self.data(
            url_version="v4",
            path="fundraising/search",
            params={"name": company}
        )

    def equity_offerings_by_cik(self, cik: str):
        """Query FMP / fundraising / API.

        Search for a specific private company (by CIK) undergoing an equity offering

        Parameters
        ----------
        cik :
            Company CIK number.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        -------
        >>> private_companies = PrivateCompanies(apikey="abc123") # Initialize data source
        >>>
        >>> search_result = private_companies.equity_offerings_by_cik('0001870523')
        >>> print(search_result)
          formType  ... grossProceedsUsed
        0        D  ...               0.0
        1        D  ...               0.0

        [2 rows x 40 columns]
        """
        return self.data(
            url_version="v4",
            path="fundraising",
            params={"cik": cik}
        )
