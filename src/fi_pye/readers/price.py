from typing import List

from .utils import (
    _format_multiple_symbols,
    _clean_historical_daily_price,
    _validate_price_dates,
)
from .reader import Reader


class Price(Reader):
    """ """

    def price(self, symbol: str):
        """Query FMP / quote /  API.

        Return the latest price (quote) for a given symbol.
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

        Return list of the latest prices (quotes) for a list of symbols.
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

    def historical_price(self, symbol: str, timeframe: str):
        """Query FMP / quote /  API.

        Return historical price data for a given symbol.
        The 'symbol' parameter can be for any equity type,
        meaning it can be a stock, crypto, fx, etf, etc.

        Parameters
        ----------
        symbol :
            Equity ticker symbol.
        timeframe :
            Time frame for price history (1m, 5m, 15m, 30m, 1h, 4h).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        valid_timeframes = ["1m", "5m", "15m", "30m", "1h", "4h"]
        if timeframe not in valid_timeframes:
            raise ValueError(f"Invalid timeframe: {timeframe}. Valid timeframes are as follow: {valid_timeframes}. ")

        return self.data(
            url_version="v3",
            path=f"historical-chart/{timeframe}/{symbol.upper()}",
            params={
                "apikey": self.apikey,
            },
        )

    def historical_daily_price(self, symbol: str, limit: int = 100):
        """Query FMP / quote /  API.

        Return historical price data for a given symbol.
        The 'symbol' parameter can be for any equity type,
        meaning it can be a stock, crypto, fx, etf, etc.

        Parameters
        ----------
        symbol :
            Equity ticker symbol
        limit :
            Get daily price data for the last x number of days

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return _clean_historical_daily_price(
            self.data(
                url_version="v3",
                path=f"historical-price-full/{symbol.upper()}",
                params={
                    "timeseries": limit,
                    "serietype": "bar",
                    "apikey": self.apikey,
                },
            )
        )

    def historical_daily_price_by_date(self, symbol: str, from_date: str, to_date: str):
        """Query FMP / quote /  API.

        Return historical price data for a given symbol.
        The 'symbol' parameter can be for any equity type,
        meaning it can be a stock, crypto, fx, etf, etc.

        Parameters
        ----------
        symbol :
            Equity ticker symbol
        from_date :
            Starting date for historical price data in 'YYYY-MM-DD' format
        to_date :
            Ending date for historical price data in 'YYYY-MM-DD' format

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        start, end = _validate_price_dates(from_date, to_date)
        return _clean_historical_daily_price(
            self.data(
                url_version="v3",
                path=f"historical-price-full/{symbol.upper()}",
                params={
                    "from": start,
                    "to": end,
                    "serietype": "bar",
                    "apikey": self.apikey,
                },
            )
        )

    def batch_historical_daily_price(self, symbols: list[str], limit: int = 100):
        """Query FMP / quote /  API.

        Return historical price data for a given symbol.
        The 'symbol' parameter can be for any equity type,
        meaning it can be a stock, crypto, fx, etf, etc.

        Parameters
        ----------
        symbols :
            List of equity ticker symbols
        limit :
            Get daily price data for the last x number of days

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"historical-price-full/{_format_multiple_symbols(symbols)}",
            params={
                "timeseries": limit,
                "serietype": "bar",
                "apikey": self.apikey,
            },
        )


