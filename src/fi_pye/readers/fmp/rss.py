from .reader import FmpReader


class RSS(FmpReader):
    """
    This class is used to obtain data from the RSS feeds available from
    FMPs API.

    Available RSS feeds include:
        - Price targets.
        - Mergers and acquisitions.
        - Insider trading.
        - Senate trading.
        - Senate disclosures.
        - Form 8-K's.
        - Latest SEC documents.
    """

    def institutional_holder_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def price_target_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def mergers_and_acquisition_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def insider_trading_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def senate_trading_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def senate_disclosure_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def eightk_rss(self, page: int = 0, with_financials: bool = True):
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

    def sec_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def crowdfunding_offerings_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def equity_fundraising_offerings_rss(self, page: int = 0):
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
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )
