from .reader import Reader


class Analysts(Reader):
    """
    This can be used to access FMPs endpoints related to analyst
    actions on a specific stock.
    """
    def price_target(self, symbol: str):
        """Query FMP / price-target / API.

        A price target is an analyst's projection of a stock's
        future performance.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="price-target",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def price_target_summary(self, symbol: str):
        """Query FMP / price-target-summary / API.

        Rather than Returnsing a list of all price targets for a
        stock, this endpoint will return a summary of all targets.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="price-target-summary",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def price_target_consensus(self, symbol: str):
        """Query FMP / price-target-consensus / API.

        Returns price target consensus.

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="price-target-consensus",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def price_target_by_analyst(self, analyst_name: str):
        """Query FMP / price-target-analyst-name / API.

        Returns price targets for a specific analyst (by name).

        Parameters
        ----------
        analyst_name :
            Full name of analyst (Example='Tim Anderson')

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="price-target-analyst-name",
            params={
                "name": analyst_name,
                "apikey": self.apikey,
            },
        )

    def price_target_by_company(self, company: str):
        """Query FMP / price-target-analyst-company / API.

        Returns price targets for a specific analyst (by company name).

        Parameters
        ----------
        company :
            Name of grading company (Example='Barclays').

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="price-target-analyst-company",
            params={
                "name": company,
                "apikey": self.apikey,
            },
        )

    def upgrades_and_downgrades(self, symbol: str):
        """Query FMP / price-target / API.

        Returns upgrades and downgrades for a given stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def upgrades_and_downgrades_consensus(self, symbol: str):
        """Query FMP / price-target / API.

        Returns the upgrades and downgrades, with consensus,
        for a given stock (by symbol).

        Parameters
        ----------
        symbol :
            Stock ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades-consensus",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def upgrades_and_downgrades_by_company(self, company: str):
        """Query FMP / upgrades-downgrades-grading-company / API.

        Returns only upgrades and downgrades from a specific
        grading company (by company name).

        Parameters
        ----------
        company :
            Name of grading company (Example='Barclays').

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades-grading-company",
            params={
                "company": company,
                "apikey": self.apikey,
            },
        )
