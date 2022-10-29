from .reader import Reader


class Quote(Reader):
    """
    This class is used to obtain the latest real-time prices from stocks
    within the New York Stock Exchange (NYSE), Toronto Stock Exchange (TSX),
    and Euronext Exchange (EURONEXT), as well as from equities within
    indexes, commodities, foreign exchanges, and cryptocurrencies available
    from FMP's API.

    If you are trying to get specific equity prices, use the Prices class.
    """

    @property
    def indexes_quote(self):
        """Query FMP / quotes/index / API.

        Obtain the latest real-time price (and much more) for all indexes
        available through FMP.

        *To get a list of all supported indexes, use the Symbols class.

        Data returned about each index:
            - Symbol.
            - Name.
            - Current price.
            - Daily change (% and $).
            - Daily open, high & low price.
            - Previous close price.
            - Yearly high and low price.
            - Market cap.
            - Average price (50-day and 200-day).
            - Daily volume & Average volume.
            - Exchange (INDEX).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/indexes-in-stock-market-free-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="quotes/index",
            params={"apikey": self.apikey},
        )

    @property
    def commodities_quote(self):
        """Query FMP / quotes/commodity / API.

        Obtain the latest real-time price (and much more) for all commodities
        available through FMP.

        *To get a list of all supported commodities, use the Symbols class.

        Data returned about each commodity:
            - Symbol.
            - Name.
            - Current price.
            - Daily change (% and $).
            - Daily open, high & low price.
            - Previous close price.
            - Yearly high and low price.
            - Market cap.
            - Average price (50-day and 200-day).
            - Daily volume & Average volume.
            - Exchange (COMMODITY).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/stock-market-quote-free-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="quotes/commodity",
            params={"apikey": self.apikey},
        )

    @property
    def forex_quote(self):
        """Query FMP / quotes/forex / API.

        Obtain the latest real-time price (and much more) for all forex
        available through FMP.

        Data returned about each FX pair:
            - Symbol.
            - Name of currency pair.
            - Current price.
            - Change (% and $).
            - Daily open, high & low price.
            - Previous close price.
            - Yearly high and low price.
            - Market cap.
            - Average price (50-day and 200-day).
            - Daily volume & Average volume.
            - Daily open & Previous close price.
            - Exchange (FOREX).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/currency-exchange-rate-free-api/#Forex-Currency-Exchange-Rate-(FX)

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="quotes/forex",
            params={"apikey": self.apikey},
        )

    @property
    def currency_exchange_rates(self):
        """Query FMP / fx / API.

        Obtain the latest real-time currency exchange rates for currency-pairs
        available through FMP.

        *To get a list of all supported currency pairs, use the Symbols class.

        Data returned about each currency pair:
            - Ticker of currency pair (Example = 'EUR/USD').
            - Current bid & ask.
            - Daily open, high & low price.
            - Daily changes ($).
            - Date (as datetime).

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/currency-exchange-rate-free-api/#Forex-Currency-Exchange-Rate-(FX)

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="fx",
            params={"apikey": self.apikey},
        )

    @property
    def cryptos_quote(self):
        """Query FMP / quotes/crypto / API.

        Obtain the latest real-time price (and much more) for all
        cryptocurrencies available through FMP.

        *To get a list of all supported cryptos, use the Symbols class.

        Data returned about each cryptocurrency:
            - Symbol.
            - Name.
            - Current price.
            - Daily change (% and $).
            - Daily open, high & low price.
            - Previous close price.
            - Yearly high and low price.
            - Market cap.
            - Average price (50-day and 200-day).
            - Daily volume & Average volume.
            - Exchange (CRYPTO).
            - Shares outstanding.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/crypto-currency-free-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="quotes/crypto",
            params={"apikey": self.apikey},
        )

    @property
    def nyse_quote(self):
        """Query FMP / quotes/nyse / API.

        Obtain the latest real-time price (and much more) for all stocks in
        the New York Stock Exchange (NYSE).

        Data returned about each NYSE stock:
            - Symbol.
            - Name.
            - Current price.
            - Daily change (% and $).
            - Daily open, high & low price.
            - Previous close price.
            - Yearly high and low price.
            - Market cap.
            - Average price (50-day and 200-day).
            - Daily volume & Average volume.
            - Exchange (NYSE).
            - Earnings per share (EPS), price/earnings (P/E) ratio & earnings announcement (Not available for all).
            - Shares outstanding.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/realtime-stock-quote-api/#Stock-Price-list

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="quotes/nyse",
            params={"apikey": self.apikey},
        )

    @property
    def tsx_quote(self):
        """Query FMP / quotes/tsx / API.

        Obtain the latest real-time price (and much more) for all stocks in
        the Toronto Stock Exchange (TSX).

        Data returned about each TSX stock:
            - Symbol.
            - Name.
            - Current price.
            - Daily change (% and $).
            - Daily open, high & low price.
            - Previous close price.
            - Yearly high and low price.
            - Market cap.
            - Average price (50-day and 200-day).
            - Daily volume & Average volume.
            - Exchange (TSX).
            - Earnings per share (EPS), price/earnings (P/E) ratio & earnings announcement (Not available for all).
            - Shares outstanding.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/crypto-currency-free-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="quotes/tsx",
            params={"apikey": self.apikey},
        )

    @property
    def euronext_quote(self):
        """Query FMP / quotes/euronext / API.

        Obtain the latest real-time price (and much more) for all stocks in
        the Euronext Exchange (EURONEXT).

        Data returned about each Euronext stock:
            - Symbol.
            - Name.
            - Current price.
            - Daily change (% and $).
            - Daily open, high & low price.
            - Previous close price.
            - Yearly high and low price.
            - Market cap.
            - Average price (50-day and 200-day).
            - Daily volume & Average volume.
            - Exchange (EURONEXT).
            - Earnings per share (EPS), price/earnings (P/E) ratio & earnings announcement (Not available for all).
            - Shares outstanding.

        Documentation
        -------------
            - https://site.financialmodelingprep.com/developer/docs/euronext-prices-api/

        ------
        Return : pandas DataFrame
        ------
        """
        return self.data(
            url_version="v3",
            path="quotes/euronext",
            params={"apikey": self.apikey},
        )
