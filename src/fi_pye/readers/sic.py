from .reader import Reader


class SIC(Reader):
    """
    'Standard Industrial Classification (SIC) codes are four-digit
    numerical codes that categorize the industries that companies
    belong to based on their business activities.' ~ Investopedia
    """

    def cik_by_symbol(
        self,
        symbol: str,
    ):
        """Query FMP / standard_industrial_classification / API.

        Obtain Standard Industrial Classification (SIC) for
        stock (by symbol).

        Documentation
        -------------
            https://site.financialmodelingprep.com/developer/docs/standard-industrial-classification-api/

        Parameters
        ----------
            symbol : Stock ticker symbol.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v4",
            path="standard_industrial_classification",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )
