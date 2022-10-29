from .reader import Reader


class Analysts(Reader):
    """
    This can be used to access FMP's endpoints related to analyst
    actions on a specific stock.
    """

    def price_target(
        self,
        symbol: str,
    ):
        """Query FMP / price-target / API.

        A price target is an analyst's projection of a stock's
        future performance.

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/price-target-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="price-target",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def price_target_summary(
        self,
        symbol: str,
    ):
        """Query FMP / price-target-summary / API.

        Rather than obtaining a list of all price targets for a
        stock, this endpoint will return a summary of all targets.

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/price-target-summary-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="price-target-summary",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def price_target_consensus(
        self,
        symbol: str,
    ):
        """Query FMP / price-target-consensus / API.

        Obtain price target consensus.

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/price-target-consensus-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="price-target-consensus",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def price_target_by_analyst(
        self,
        analyst_name: str,
    ):
        """Query FMP / price-target-analyst-name / API.

        Obtain price targets for a specific analyst (by name).

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/price-target-by-analyst-name-api/

        Parameters
        ----------
            analyst_name : Full name of analyst (Example='Tim Anderson').

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="price-target-analyst-name",
            params={
                "name": analyst_name,
                "apikey": self.apikey,
            },
        )

    def price_target_by_company(
        self,
        company: str,
    ):
        """Query FMP / price-target-analyst-company / API.

        Obtain price targets for a specific analyst (by company name).

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/price-target-by-analyst-company-api/

        Parameters
        ----------
            company : Name of analyst compnay (Example='Barclays').

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="price-target-analyst-company",
            params={
                "name": company,
                "apikey": self.apikey,
            },
        )

    def upgrades_and_downgrades(
        self,
        symbol: str,
    ):
        """Query FMP / price-target / API.

        Obtain upgrades and downgrades.

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/upgrades-and-downgrades-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def upgrades_and_downgrades_consensus(
        self,
        symbol: str,
    ):
        """Query FMP / price-target / API.

        Obtain upgrades and downgrades.

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/upgrades-and-downgrades-consensus-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades-consensus",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def upgrades_and_downgrades_by_company(
        self,
        company: str,
    ):
        """Query FMP / upgrades-downgrades-grading-company / API.

        Obtain upgrades and downgrades for a specific
        grading company (by company name).

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/upgrades-and-downgrades-by-company-api/

        Parameters
        ----------
            company : Grading company name (Example='Barclays').

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades-grading-company",
            params={
                "company": company,
                "apikey": self.apikey,
            },
        )
