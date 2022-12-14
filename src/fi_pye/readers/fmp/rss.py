from .reader import FmpReader


class RSS(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    RSS feeds.

    RSS
    ---
    - Institutional ownership
    - Price targets
    - Mergers and acquisitions
    - Insider trading
    - Senate trading
    - Senate disclosures
    - Form 8-K's
    - SEC filings
    """

    def institutional_ownership(self, page: int = 0):
        """Query FMP / institutional-ownership/rss_feed / API.

        Obtain institutional ownership live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="institutional-ownership/rss_feed",
            params={"page": page}
        )

    def price_targets(self, page: int = 0):
        """Query FMP / price-target-rss-feed / API.

        Obtain price targets live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="price-target-rss-feed",
            params={"page": page}
        )

    def mergers_and_acquisitions(self, page: int = 0):
        """Query FMP / mergers-acquisitions-rss-feed / API.

        Obtain mergers and acquisitions live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="mergers-acquisitions-rss-feed",
            params={"page": page}
        )

    def insider_trades(self, page: int = 0):
        """Query FMP / insider-trading-rss-feed / API.

        Obtain insider trading live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="insider-trading-rss-feed",
            params={"page": page}
        )

    def senate_trades(self, page: int = 0):
        """Query FMP / senate-trading-rss-feed / API.

        Obtain senate trading live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="senate-trading-rss-feed",
            params={"page": page}
        )

    def senate_disclosures(self, page: int = 0):
        """Query FMP / senate-disclosure-rss-feed / API.

        Obtain senate disclosure live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="senate-disclosure-rss-feed",
            params={"page": page}
        )

    def eightk_filings(self, page: int = 0, with_financials: bool = True):
        """Query FMP / rss_feed_8k / API.

        Obtain 8K (Important Events) live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number
        with_financials : default = True
            Return only 8-K filings that contain financials

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(with_financials, bool):
            raise TypeError(
                f"Invalid with_financials type passed: {with_financials} = {type(with_financials)}. "
                "with_financials must be of type boolean (bool). "
            )
        return self.data(
            url_version="v4",
            path="rss_feed_8k",
            params={
                "hasFinancial": str(with_financials).lower(),
                "page": page,
                "apikey": self.apikey,
            },
        )

    def all_sec_filings(self, page: int = 0):
        """Query FMP / rss_feed_8k / API.

        Obtain 8K (Important Events) live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path="rss_feed",
            params={"page": page}
        )

    def crowdfunding_offerings(self, page: int = 0):
        """Query FMP / crowdfunding-offerings-rss-feed / API.

        Obtain private company crowdfunding offerings live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path="crowdfunding-offerings-rss-feed",
            params={"page": page}
        )

    def equity_fundraising_offerings(self, page: int = 0):
        """Query FMP / fundraising-rss-feed / API.

        Obtain private company equity fundraising offerings live rss feed.

        Parameters
        ----------
        page : default = 0
            Response page number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path="fundraising-rss-feed",
            params={"page": page}
        )
