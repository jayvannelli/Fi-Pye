from typing import List

from .utils import _format_multiple_symbols
from .reader import Reader


class Price(Reader):
    """ """

    def price(self, symbol: str,):
        """Query FMP / quote /  API.

        Returns the latest price for a given symbol.
        The 'symbol' parameter can be for any equity type,
        meaning it can be a stock, crypto, fx, etf, etc.

        Parameters
        ----------
        symbol :
            Equity ticker symbol.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"quote/{symbol.upper()}",
            params={
                "apikey": self.apikey,
            },
        )

    def multiple_prices(self, symbols: List[str]):
        """Query FMP / quote /  API.

        Returns the latest prices for a list of symbols.
        The 'symbol' parameter can be for any equity type,
        meaning it can be a stock, crypto, fx, etf, etc.

        *If you get a 'DataFrame conversion exception: If using all scalar
        values, you must pass an index' logging error, it means one of the symbols
        in your symbols list was invalid. To get lists of available symbols, use
        the Symbols class.

        Parameters
        ----------
        symbols :
            List of ticker symbols (Ex. symbols = ['AMD', 'TSLA', 'SHOP', 'AAPL']).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"quote/{_format_multiple_symbols(symbols)}",
            params={
                "apikey": self.apikey,
            },
        )
