from .reader import Reader


class Symbols(Reader):
    """
    This class is used to obtain a list of stock, index, ETF, commodity,
    FX-pair, and cryptocurrency symbols available for quotes and historical
    price queries from FMP's API.
    """


    def all_stock_symbols(self):
        """Query FMP / stock/list / API.

        Obtain a list of all traded and non-trades stocks from FMP's API.

        Data returned about each stock:
            - Symbol.
            - Name.
            - Price.
            - Exchange.
            - Exchange short name.
            - Type of equity.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-market-quote-free-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="stock/list",
            params={"apikey": self.apikey},
        )

    def tradable_stock_symbols(self):
        """Query FMP / stock/list / API.

        Obtain a list of all tradable stocks from FMP's API.

        Data returned about each stock:
            - Symbol.
            - Name.
            - Price.
            - Exchange.
            - Exchange short name.
            - Type of equity.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/tradable-list-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="available-traded/list",
            params={"apikey": self.apikey},
        )

    def etf_symbols(self):
        """Query FMP / etf/list / API.

        Obtain a list of available ETFs from FMP's API.

        Data returned about each ETF:
            - Symbol.
            - Name.
            - Price.
            - Exchange.
            - Exchange short name.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/tradable-list-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="etf/list",
            params={"apikey": self.apikey},
        )

    def tsx_symbols(self):
        """Query FMP / symbol/available-tsx / API.

        Obtain symbol of stocks trading on the Toronto Stock Exchange (TSX) from FMP's API.

        Data returned about each TSX stock:
            - Symbol.
            - Name.
            - Currency.
            - Stock exchange (Toronto Stock Exchange).
            - Exchange short name (TSX).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/tsx-prices-api/#Commodities-symbol-List

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="symbol/available-tsx",
            params={"apikey": self.apikey},
        )

    def euronext_symbols(self):
        """Query FMP / symbol/available-euronext / API.

        Obtain symbol of stocks trading on the Euronext Stock Exchange available from FMP's API.

        Data returned about each Euronext stock:
            - Symbol.
            - Name.
            - Currency.
            - Stock exchange (Euronext Stock Exchange).
            - Exchange short name (EURONEXT).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/euronext-prices-api/#Commodities-symbol-List

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="symbol/available-euronext",
            params={"apikey": self.apikey},
        )

    def index_symbols(self):
        """Query FMP / symbol/available-indexes / API.

        Obtain a list of available indexes from FMP's API.

        Data returned about each index:
            - Symbol.
            - Name.
            - Currency (USD).
            - Exchange (New York Stock Exchange).
            - Exchange short name (NYSE).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/tradable-list-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="symbol/available-indexes",
            params={"apikey": self.apikey},
        )

    def commodities_symbols(self):
        """Query FMP / symbol/available-commodities / API.

        Obtain symbol of commodities available from FMP's API.

        Data returned about each commodity:
            - Symbol.
            - Name.
            - Currency.
            - Stock exchange (Possible values include : 'NY Mercantile', 'CBOT', 'ICE Futures', etc.).
            - Exchange short name (COMMODITY).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/commodities-prices-api/#Commodities-symbol-List

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="symbol/available-commodities",
            params={"apikey": self.apikey},
        )

    def crypto_symbols(self):
        """Query FMP / symbol/available-cryptocurrencies / API.

        Obtain symbol of cryptocurrencies available from FMP's API.

        Data returned about each cryptocurrency:
            - Symbol.
            - Name.
            - Currency.
            - Stock exchange (CCC).
            - Exchange short name (CRYPTO).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/cryptocurrency-historical-data-api/#Crypto-Historical-quotes

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="symbol/available-cryptocurrencies",
            params={"apikey": self.apikey},
        )

    def fx_currency_pairs(self):
        """Query FMP / symbol/available-forex-currency-pairs / API.

        Obtain symbol of fores currency pairs available from FMP's API.

        Data returned about each currency pair:
            - Symbol.
            - Name (fx pair).
            - Currency.
            - Stock exchange (CCY).
            - Exchange short name (FOREX).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/forex-historical-data-api/#Forex-Historical-quotes

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="symbol/available-forex-currency-pairs",
            params={"apikey": self.apikey},
        )
