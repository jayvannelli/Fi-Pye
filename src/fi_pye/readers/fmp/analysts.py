from .reader import FmpReader


class Analysts(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related
    to analysts & analyst actions on stocks.

    Analysts
    --------
    - Price target
    - Price target with summary
    - Price target with consensus
    - Upgrades & downgrades
    - Upgrades & downgrades consensus
    - Price target by analyst name
    - Price target by grading company
    - Upgrades & downgrades by grading company

    Examples
    --------
    >>> analysts = Analysts(apikey="abc123") # Initialize data source
    >>>
    >>> # Stock price targets.
    >>> tsla_pt = analysts.price_target("TSLA")
    >>> amd_pt_summary = analysts.price_target_summary("AMD")
    >>> aapl_pt_consensus = analysts.price_target_consensus("AAPL")
    >>>
    >>> # Stock upgrades & downgrades.
    >>> nvda_up_n_down = analysts.upgrades_and_downgrades("NVDA")
    >>> msft_up_n_down_consensus = analysts.upgrades_and_downgrades_consensus("MSFT")
    >>>
    >>> # Price targets and upgrades & downgrades by analyst/grading company.
    >>> tim_anderson_targets = analysts.price_target_by_analyst("Tim Anderson")
    >>> barclays_targets = analysts.price_target_by_company("Barclays")
    >>> barclays_up_n_down = analysts.price_target_by_company("Barclays")
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

        Examples
        --------
        >>> analysts = Analysts(apikey="abc123") # Initialize data source
        >>>
        >>> tsla_pt = analysts.price_target("TSLA")
        """
        return self.data(
            url_version="v4",
            path="price-target",
            params={
                "symbol": symbol.upper(),
            },
        )

    def price_target_summary(self, symbol: str):
        """Query FMP / price-target-summary / API.

        Rather than returning a list of all price targets for a
        stock, this endpoint will return a summary of all targets.

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
        >>> analysts = Analysts(apikey="abc123") # Initialize data source
        >>>
        >>> amd_pt_summary = analysts.price_target_summary("AMD")
        """
        return self.data(
            url_version="v4",
            path="price-target-summary",
            params={
                "symbol": symbol.upper(),
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

        Examples
        --------
        >>> analysts = Analysts(apikey="abc123") # Initialize data source
        >>>
        >>> aapl_pt_consensus = analysts.price_target_consensus("AAPL")
        """
        return self.data(
            url_version="v4",
            path="price-target-consensus",
            params={"symbol": symbol.upper()}
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

        Examples
        --------
        >>> analysts = Analysts(apikey="abc123") # Initialize data source
        >>>
        >>> tim_anderson_targets = analysts.price_target_by_analyst("Tim Anderson")
        """
        return self.data(
            url_version="v4",
            path="price-target-analyst-name",
            params={"name": analyst_name}
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

        Examples
        --------
        >>> analysts = Analysts(apikey="abc123") # Initialize data source
        >>>
        >>> barclays_targets = analysts.price_target_by_company("Barclays")
        """
        return self.data(
            url_version="v4",
            path="price-target-analyst-company",
            params={"company": company}
        )

    def upgrades_and_downgrades(self, symbol: str):
        """Query FMP / price-target / API.

        Return upgrades and downgrades for a given stock (by symbol).

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
        >>> analysts = Analysts(apikey="abc123") # Initialize data source
        >>>
        >>> nvda_up_n_down = analysts.upgrades_and_downgrades("NVDA")
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades",
            params={"symbol": symbol.upper()}
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

        Examples
        --------
        >>> analysts = Analysts(apikey="abc123") # Initialize data source
        >>>
        >>> msft_up_n_down_consensus = analysts.upgrades_and_downgrades_consensus("MSFT")
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades-consensus",
            params={"symbol": symbol.upper()}
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

        Examples
        --------
        >>> analysts = Analysts(apikey="abc123") # Initialize data source
        >>>
        >>> barclays_up_n_down = analysts.price_target_by_company("Barclays")
        """
        return self.data(
            url_version="v4",
            path="upgrades-downgrades-grading-company",
            params={"company": company}
        )
