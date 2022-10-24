from .reader import Reader


class RSS(Reader):
    """
    This class is used to obtain data from the RSS feeds available from
    FMP's API.

    Currenlty available RSS feeds include:
        - Price targets.
        - Mergers and acquisitions.
        - Insider trading.
        - Senate trading.
        - Senate disclosures.
        - Form 8-K's.
        - Latest SEC documents.
    """

    def price_target_rss(self, page: int = 0):
        """Query FMP / price-target-rss-feed / API.

        Obtain price targets live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/price-target-rss-feed-api/

        Parameters
        ----------
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="price-target-rss-feed",
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def mergers_and_acquisition_rss(
        self,
        page: int = 0,
    ):
        """Query FMP / mergers-acquisitions-rss-feed / API.

        Obtain mergers and acquisitions live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/merger-and-acquisition-api/

        Parameters
        ----------
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="mergers-acquisitions-rss-feed",
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def insider_trading_rss(
        self,
        page: int = 0,
    ):
        """Query FMP / insider-trading-rss-feed / API.

        Obtain insider trading live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/insider-trading-rss-feed-api/

        Parameters
        ----------
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="insider-trading-rss-feed",
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def senate_trading_rss(
        self,
        page: int = 0,
    ):
        """Query FMP / senate-trading-rss-feed / API.

        Obtain senate trading live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/senate-trading-api/

        Parameters
        ----------
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="senate-trading-rss-feed",
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def senate_disclosure_rss(
        self,
        page: int = 0,
    ):
        """Query FMP / senate-disclosure-rss-feed / API.

        Obtain senate disclosure live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/senate-disclosure-api/

        Parameters
        ----------
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="senate-disclosure-rss-feed",
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def eightk_rss(
        self,
        page: int = 0,
        with_financials: bool = True,
    ):
        """Query FMP / rss_feed_8k / API.

        Obtain 8K (Important Events) live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/rss-feed-8k-api/

        Parameters
        ----------
            page : Response page number.
            with_financials : Return 8K filing with financial's included.

        ------
        Return : pandas DataFrame
        ------
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

    def sec_rss(
        self,
        page: int = 0,
    ):
        """Query FMP / rss_feed_8k / API.

        Obtain 8K (Important Events) live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/rss-feed-8k-api/

        Parameters
        ----------
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="rss_feed",
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def crowdfunding_offerings_rss(
        self,
        page: int = 0,
    ):
        """Query FMP / crowdfunding-offerings-rss-feed / API.

        Obtain private company crowdfunding offerings live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/crowdfunding-offerings-rss-feed-api/

        Parameters
        ----------
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="crowdfunding-offerings-rss-feed",
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )

    def equity_fundraising_offerings_rss(
        self,
        page: int = 0,
    ):
        """Query FMP / fundraising-rss-feed / API.

        Obtain private company equity fundraising offerings live rss feed.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/equity-offerings-fundraising-rss-feed-api/

        Parameters
        ----------
            page : Response page number.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="fundraising-rss-feed",
            params={
                "page": page,
                "apikey": self.apikey,
            },
        )
