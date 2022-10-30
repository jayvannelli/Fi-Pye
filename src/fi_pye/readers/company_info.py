from .reader import Reader


class CompanyInformation(Reader):
    """ """
    def company_profile(self, symbol: str):
        """Query FMP / profile / API.

        Obtain company profile.

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
            url_version="v3",
            path=f"profile/{symbol.upper()}",
            params={
                "apikey": self.apikey,
            },
        )

    def key_executives(self, symbol: str):
        """Query FMP / key-executives / API.

        Obtain stock key executives.

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
            url_version="v3",
            path=f"key-executives/{symbol.upper()}",
            params={
                "apikey": self.apikey,
            },
        )

    def shares_float(self, symbol: str):
        """Query FMP / shares_float / API.

        Obtain shares float for a given company.

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
            path="shares_float",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def company_outlook(self, symbol: str):
        """Query FMP / company-outlook / API.

        Obtain outlook for a given company.

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
            path="company-outlook",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def executive_compensation(self, symbol: str):
        """Query FMP / governance/executive_compensation / API.

        Obtain executive compensation.

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
            path="governance/executive_compensation",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def individual_beneficial_ownership(self, symbol: str):
        """Query FMP / insider/ownership/acquisition_of_beneficial_ownership / API.

        Obtain company individual beneficial ownership.

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
            path="insider/ownership/acquisition_of_beneficial_ownership",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def stock_peers(self, symbol: str):
        """Query FMP / stock_peers / API.

        Obtain company stock peers.

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
            path="stock_peers",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def core_information(self, symbol: str):
        """Query FMP / company-core-information / API.

        Obtain company core information.

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
            path="company-core-information",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def company_rating(self, symbol: str):
        """Query FMP / rating / API.

        Obtain company rating.

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
        """
        return self.data(
            url_version="v3",
            path=f"rating/{symbol.upper()}",
            params={
                "apikey": self.apikey,
            },
        )

    def notes_due(self, symbol: str):
        """Query FMP / rating / API.

        Obtain company rating.

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
            path="company-notes",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def esg_score(self, symbol: str):
        """Query FMP / esg-environmental-social-governance-data / API.

        Obtain company esg score.

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
            path="esg-environmental-social-governance-data",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def esg_risk_rating(self, symbol: str):
        """Query FMP / esg-environmental-social-governance-data-ratings / API.

        Obtain company esg risk ratings.

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
            path="esg-environmental-social-governance-data-ratings",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )
