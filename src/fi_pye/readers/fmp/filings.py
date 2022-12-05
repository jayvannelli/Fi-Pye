from .reader import FmpReader
from .utils import (
    _validate_sec_filing_type,
    VALID_SEC_FILING_TYPES,
)


class Filings(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related to
    stock SEC filings.

    Filings
    -------
    - List of all types of SEC filings
    - All SEC filings for stock (by symbol)
    - Specific SEC filing for stock (by symbol)
    """
    @property
    def filing_types(self):
        """Get filings types accepted by method 'specific_sec_filing'.

        This returns a list of valid 'type' values (type of SEC form)
        that can be passed to the method 'specific_sec_filing'.
        ------
        Return : list of strings
        ------
        """
        return VALID_SEC_FILING_TYPES

    def all_stock_filings(self, symbol: str, page: int = 0):
        """Query FMP / sec_filings / API.

        Return all types of SEC filing for the given company.

        Parameters
        ----------
        symbol :
            Stock ticker symbol.
        page : default = 0
            Response page number.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"sec_filings/{symbol.upper()}",
            params={
                "page": page,
                "apikey": self.apikey,
            }
        )

    def specific_stock_filing(self, symbol: str, type: str, page: int = 0):
        """Query FMP / sec_filings / API.

        Return a specific type of SEC filing for the given company.


        Parameters
        ----------
        symbol :
            Stock ticker symbol.
        type :
            Type of SEC form to return (Query 'sec_filing_types' for all types).
        page : default = 0
            Response page number.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"sec_filings/{symbol.upper()}",
            params={
                "type": _validate_sec_filing_type(type),
                "page": page,
                "apikey": self.apikey,
            }
        )
