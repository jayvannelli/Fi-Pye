from .reader import FmpReader


class CompanyInformation(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    basic company information about a stock (given its symbol).

    Company Information
    -------------------
    - Profile
    - Key executives
    - Shares float
    - Outlook
    - Executive compensation
    - Individual beneficial ownership
    - Stock peers
    - Core info
    - Rating
    - Notes due
    - Environmental, social and governance (ESG) score
    - ESG risk ratings

    Examples
    --------
    >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
    >>>
    >>> SYMBOL = "AMD"
    >>>
    >>> amd_profile = company_information.profile(SYMBOL)
    >>> amd_key_execs = company_information.key_executives(SYMBOL)
    >>> amd_esg_score = company_information.esg_score(SYMBOL)
    >>> amd_esc_risk_ratings = company_information.esg_risk_rating(SYMBOL)
    """

    def profile(self, symbol: str):
        """Query FMP / profile / API.

        Return company profile for a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> aapl_profile = company_information.profile("AAPL")
        >>> print(aapl_profile)
          symbol   price      beta    volAvg  ...  isEtf  isActivelyTrading  isAdr  isFund
        0   AAPL  155.74  1.249815  83817726  ...  False               True  False   False

        [1 rows x 36 columns]
        """
        return self.data(
            url_version="v3",
            path=f"profile/{symbol.upper()}",
            params=None
        )

    def key_executives(self, symbol: str):
        """Query FMP / key-executives / API.

        Return key executives of a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> jpm_key_execs = company_information.key_executives("JPM")
        >>> print(jpm_key_execs)
                                                       title  ... titleSince
        0                         Head of Investor Relations  ...       None
        1                   Global Chief Information Officer  ...       None
        2  Corporation Controller & Principal Accounting ...  ...       None
        3  Chief Financial Officer & Head of Strategy for...  ...       None
        4                            Chief Financial Officer  ...       None
        5            Co-Head of Consumer & Community Banking  ...       None
        6                                     Senior Advisor  ...       None
        7  Chief Executive Officer of Asset & Wealth Mana...  ...       None
        8                     Pres & Chief Operating Officer  ...       None
        9                 Chairman & Chief Executive Officer  ...       None

        [10 rows x 7 columns]
        """
        return self.data(
            url_version="v3",
            path=f"key-executives/{symbol.upper()}",
            params=None
        )

    def shares_float(self, symbol: str):
        """Query FMP / shares_float / API.

        Return share float for a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> ko_float = company_information.shares_float("KO")
        >>> print(ko_float)
          symbol  ...                                             source
        0     KO  ...  https://www.sec.gov/Archives/edgar/data/21344/...

        [1 rows x 6 columns]
        """
        return self.data(
            url_version="v4",
            path="shares_float",
            params={"symbol": symbol.upper()}
        )

    def executive_compensation(self, symbol: str):
        """Query FMP / governance/executive_compensation / API.

        Return executive compensation for a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> crm_executive_comp = company_information.executive_compensation("CRM")
        >>> print(crm_executive_comp.head())
                    cik  ...                                                url
        0    0001108524  ...  https://www.sec.gov/Archives/edgar/data/110852...
        1    0001108524  ...  https://www.sec.gov/Archives/edgar/data/110852...
        2    0001108524  ...  https://www.sec.gov/Archives/edgar/data/110852...
        3    0001108524  ...  https://www.sec.gov/Archives/edgar/data/110852...
        4    0001108524  ...  https://www.sec.gov/Archives/edgar/data/110852...
        ...
        [213 rows x 15 columns]
        """
        return self.data(
            url_version="v4",
            path="governance/executive_compensation",
            params={"symbol": symbol.upper()}
        )

    def individual_beneficial_ownership(self, symbol: str):
        """Query FMP / insider/ownership/acquisition_of_beneficial_ownership / API.

        Return individual beneficial ownership of a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> intc_ibo = company_information.individual_beneficial_ownership("INTC")
        >>> print(intc_ibo.head())
                   cik  ...                                                url
        0   0000050863  ...  https://www.sec.gov/Archives/edgar/data/50863/...
        1   0000050863  ...  https://www.sec.gov/Archives/edgar/data/50863/...
        2   0000050863  ...  https://www.sec.gov/Archives/edgar/data/50863/...
        3   0000050863  ...  https://www.sec.gov/Archives/edgar/data/50863/...
        4   0000050863  ...  https://www.sec.gov/Archives/edgar/data/50863/...
        5   0000050863  ...  https://www.sec.gov/Archives/edgar/data/50863/...
        ...
        [25 rows x 15 columns]
        """
        return self.data(
            url_version="v4",
            path="insider/ownership/acquisition_of_beneficial_ownership",
            params={"symbol": symbol.upper()}
        )

    def stock_peers(self, symbol: str):
        """Query FMP / stock_peers / API.

        Return stock-market-peers for a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> lulu_stock_peers = company_information.stock_peers("LULU")
        >>> print(lulu_stock_peers)
          symbol                                          peersList
        0   LULU  [MELI, LCID, ROST, ORLY, CPRT, EBAY, RIVN, TSC...
        """
        return self.data(
            url_version="v4",
            path="stock_peers",
            params={"symbol": symbol.upper()}
        )

    def core_information(self, symbol: str):
        """Query FMP / company-core-information / API.

        Return core information about a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> amd_core_info = company_information.core_information("AMD")
        >>> print(amd_core_info)
                  cik symbol  ... taxIdentificationNumber                registrantName
        0  0000002488    AMD  ...              94-1692300  ADVANCED MICRO DEVICES, INC.

        [1 rows x 13 columns]
        """
        return self.data(
            url_version="v4",
            path="company-core-information",
            params={"symbol": symbol.upper()}
        )

    def rating(self, symbol: str):
        """Query FMP / rating / API.

        Return company rating for a stock (by symbol).

        Company ratings are based on their financial statement, Discounted
        cash flow analysis, financial ratios and its intrinsic value.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> mmm_rating = company_information.rating("MMM")
        >>> print(mmm_rating)
          symbol        date  ... ratingDetailsPBScore  ratingDetailsPBRecommendation
        0    MMM  2022-10-28  ...                    5                     Strong Buy

        [1 rows x 17 columns]
        """
        return self.data(
            url_version="v3",
            path=f"rating/{symbol.upper()}",
            params=None
        )

    def notes_due(self, symbol: str):
        """Query FMP / rating / API.

        Return notes due for a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> aapl_notes_due = company_information.notes_due("AAPL")
        >>> print(aapl_notes_due)
                  cik symbol                  title exchange
        0  0000320193   AAPL  1.375% Notes due 2024   NASDAQ
        1  0000320193   AAPL  1.375% Notes due 2029   NASDAQ
        2  0000320193   AAPL  1.625% Notes due 2026   NASDAQ
        3  0000320193   AAPL  0.000% Notes due 2025   NASDAQ
        4  0000320193   AAPL  3.050% Notes due 2029   NASDAQ
        5  0000320193   AAPL  1.000% Notes due 2022   NASDAQ
        6  0000320193   AAPL  0.500% Notes due 2031   NASDAQ
        7  0000320193   AAPL  3.600% Notes due 2042   NASDAQ
        8  0000320193   AAPL  0.875% Notes due 2025   NASDAQ
        9  0000320193   AAPL  2.000% Notes due 2027   NASDAQ

        **Stocks with no notes due will throw an error***

        >>> ba_notes_due = company_information.notes_due("BA")
        >>> print(ba_notes_due)
        ERROR   root: DataFrame appear... ... {'symbol': 'BA', 'apikey': ' secret token '}. Returning None.
        """
        return self.data(
            url_version="v4",
            path="company-notes",
            params={"symbol": symbol.upper()}
        )

    def esg_score(self, symbol: str):
        """Query FMP / esg-environmental-social-governance-data / API.

        Return esg score for a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> amzn_esg_score = company_information.esg_score("AMZN")
        >>> print(amzn_esg_score.head())
          symbol  ...                                                url
        0   AMZN  ...  https://www.sec.gov/Archives/edgar/data/101872...
        1   AMZN  ...  https://www.sec.gov/Archives/edgar/data/101872...
        2   AMZN  ...  https://www.sec.gov/Archives/edgar/data/101872...
        3   AMZN  ...  https://www.sec.gov/Archives/edgar/data/101872...
        4   AMZN  ...  https://www.sec.gov/Archives/edgar/data/101872...

        [5 rows x 11 columns]
        """
        return self.data(
            url_version="v4",
            path="esg-environmental-social-governance-data",
            params={"symbol": symbol.upper()}
        )

    def esg_risk_rating(self, symbol: str):
        """Query FMP / esg-environmental-social-governance-data-ratings / API.

        Return esg risk ratings for a stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Examples
        --------
        >>> company_information = CompanyInformation(apikey="abc123") # Initialize data source
        >>>
        >>> hd_esg_risk_ratings = company_information.esg_risk_rating("HD")
        >>> print(hd_esg_risk_ratings.head())
          symbol         cik       companyName  ...  year  ESGRiskRating industryRank
        0     HD  0000354950  HOME DEPOT, INC.  ...  2022             B+   2 out of 6
        1     HD  0000354950  HOME DEPOT, INC.  ...  2021             B+   2 out of 6
        2     HD  0000354950  HOME DEPOT, INC.  ...  2020             B+   2 out of 6
        3     HD  0000354950  HOME DEPOT, INC.  ...  2019             B+   1 out of 6
        4     HD  0000354950  HOME DEPOT, INC.  ...  2018             B+   1 out of 6

        [5 rows x 7 columns]
        """
        return self.data(
            url_version="v4",
            path="esg-environmental-social-governance-data-ratings",
            params={"symbol": symbol.upper()}
        )
