from .reader import Reader


class PrivateCompanies(Reader):
    """ """

    def search_crowdfunding_offerings(
        self,
        company_name: str,
    ):
        """Query FMP / crowdfunding-offerings/search / API.

        Search crowdfunding offerings by company name.

        Search for a specific private company (by name) undergoing a crowdfunding offering

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/crowdfunding-offerings-company-search-api/

        Parameters
        ----------
            company_name : Company name to search for(
                                Example='Enotap'
                            ).

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="crowdfunding-offerings/search",
            params={
                "name": company_name,
                "apikey": self.apikey,
            },
        )

    def search_crowdfunding_offerings_by_cik(
        self,
        cik: str,
    ):
        """Query FMP / crowdfunding-offerings / API.

        Search crowdfunding offerings by company CIK number.

        Search for a specific private company (by CIK) undergoing a crowdfunding offering

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/crowdfunding-offerings-by-cik-api/

        Parameters
        ----------
            company_name : Company name to search for(
                                Example='0001916078'    <- CIK number for OYO Fitness, Inc.
                            ).

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="crowdfunding-offerings",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def search_equity_offerings(
        self,
        company_name: str,
    ):
        """Query FMP / fundraising/search / API.

        Search equity offerings by company name.

        Search for a specific private company (by name) undergoing an equity offering
        *If the company name is 2 words, combine them like the example below.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/equity-offerings-fundraising-company-search-api/

        Parameters
        ----------
            company_name : Company name to search for(
                                Example='marinalife'
                            ).

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="fundraising/search",
            params={
                "name": company_name,
                "apikey": self.apikey,
            },
        )

    def search_equity_offerings_by_cik(
        self,
        cik: str,
    ):
        """Query FMP / fundraising / API.

        Search equity offerings by company CIK number.

        Search for a specific private company (by CIK) undergoing an equity offering

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/equity-offerings-fundraising-by-cik-api/

        Parameters
        ----------
            company_name : Company name to search for(
                                Example='0001870523'    <- CIK number for Marinalife, Inc.
                            ).

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="fundraising",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )
