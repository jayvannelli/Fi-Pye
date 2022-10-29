from typing import List

from .utils import _format_multiple_symbols
from .reader import Reader


class Price(Reader):
    """ """

    def price(
        self,
        symbol: str,
    ):
        """Query FMP / quote /  API.

        Obtain latest price for a given symbol.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-news-api/

        Parameters
        ----------
            symbol : Symbol of ONE stock, etf, crypto, commodity, etc.

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path=f"quote/{symbol.upper()}",
            params={
                "apikey": self.apikey,
            },
        )

    def multiple_prices(
        self,
        symbols: List[str],
    ):
        """Query FMP / quote /  API.

        Obtain latest price for multiple symbols.

        *If you get a 'DataFrame conversion exception: If using all scalar
        values, you must pass an index' logging error, it means one of the symbols
        in your symbols list was invalid. To get lists of available symbols, use
        the Symbols class.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-news-api/

        Parameters
        ----------
            symbols : List of MULTIPLE stock, etf, crypto, commodity, etc., symbols
                seperated by a comma (Example=['aapl','amzn','tsla','amd']).

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path=f"quote/{_format_multiple_symbols(symbols)}",
            params={
                "apikey": self.apikey,
            },
        )
