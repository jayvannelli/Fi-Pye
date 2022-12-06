from .reader import FmpReader


class SIC(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related
    to Standard Industrial Codes (SIC).

    'Standard Industrial Classification (SIC) codes are four-digit
    numerical codes that categorize the industries that companies
    belong to based on their business activities.' ~ Investopedia
    """

    def by_symbol(self, symbol: str):
        """Query FMP / standard_industrial_classification / API.

        Obtain Standard Industrial Classification (SIC) for
        a specific stock (by symbol).

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
            path="standard_industrial_classification",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )
