from .reader import FmpReader


class Quotes(FmpReader):
    """
     Query Financial Modeling Prep API endpoints related
    to quotes.

    This class is used to obtain the latest real-time prices from stocks
    within the New York Stock Exchange (NYSE), Toronto Stock Exchange (TSX),
    and Euronext Exchange (EURONEXT), as well as from equities within
    indexes, commodities, foreign exchanges, and cryptocurrencies available
    from FMPs API.

    If you are trying to get specific equity prices, use the Prices class.
    """
    @property
    def indexes(self):
        """Query FMP / quotes/index / API.

        Returns the latest real-time price (and more) for available indexes.
        *To get a list of all supported indexes, use the Symbols class.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> quotes = Quotes(apikey="abc123")
        >>>
        >>> indexes_quotes = quotes.indexes
        >>> print(indexes_quotes.head())
             symbol                            name  ...  sharesOutstanding   timestamp
        0  XU100.IS                        BIST 100  ...               None  1667138843
        1     ^IBEX                         IBEX 35  ...               None  1667138843
        2     ^SSMI                          SMI PR  ...               None  1667138843
        3  DX-Y.NYB  US Dollar/USDX - Index - Cash   ...               None  1667138843
        4     ^VVIX       CBOE VIX VOLATILITY INDEX  ...               None  1667138843

        [5 rows x 22 columns]
        """
        return self.data(
            url_version="v3",
            path="quotes/index",
            params=None,
        )

    @property
    def commodities(self):
        """Query FMP / quotes/commodity / API.

        Returns the latest real-time price (and more) for available commodities.
        *To get a list of all supported commodities, use the Symbols class.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> quotes = Quotes(apikey="abc123")
        >>>
        >>> commodities_quotes = quotes.commodities
        >>> print(commodities_quotes.head())
          symbol             name  ...  sharesOutstanding   timestamp
        0  PLUSD        Platinum   ...               None  1667138769
        1   NQ=F      Nasdaq 100   ...               None  1667138769
        2  OJUSX    Orange Juice   ...               None  1667138769
        3  KCUSX          Coffee   ...               None  1667138769
        4   ZI=F  Silver 5000 oz.  ...               None  1667138769

        [5 rows x 22 columns]
        """
        return self.data(
            url_version="v3",
            path="quotes/commodity",
            params=None,
        )

    @property
    def forex(self):
        """Query FMP / quotes/forex / API.

        Returns the latest real-time price (and more) for available forexes.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> quotes = Quotes(apikey="abc123")
        >>>
        >>> forex_quotes = quotes.forex
        >>> print(forex_quotes.head())
           symbol     name     price  ...  earningsAnnouncement  sharesOutstanding   timestamp
        0  GBPTND  GBP/TND    3.7220  ...                  None               None  1667138349
        1  KRWGBP  KRW/GBP    0.0006  ...                  None               None  1667138349
        2  USDUSD  USD/USD    1.0000  ...                  None               None  1667138349
        3  USDSOS  USD/SOS  566.0000  ...                  None               None  1667138349
        4  USDNOK  USD/NOK   10.3247  ...                  None               None  1667138349

        [5 rows x 22 columns]
        """
        return self.data(
            url_version="v3",
            path="quotes/forex",
            params=None,
        )

    @property
    def currency_exchange_rates(self):
        """Query FMP / fx / API.

        Returns the latest real-time price (and more) for available currency pairs.
        *To get a list of all supported currency pairs, use the Symbols class.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
         >>> quotes = Quotes(apikey="abc123")
        >>>
        >>> currency_exchange_rates_quotes = quotes.currency_exchange_rates
        >>> print(currency_exchange_rates_quotes.head())
            ticker      bid      ask  ...     high   changes                 date
        0  EUR/USD  0.99660  0.99660  ...  0.99983  0.000050  2022-10-30 10:07:39
        1  USD/JPY  147.481  147.481  ...  147.862  0.008100  2022-10-30 10:07:39
        2  GBP/USD  1.16135  1.16135  ...  1.16239  0.003925  2022-10-30 10:07:39
        3  EUR/GBP  0.85806  0.85806  ...  0.86520 -0.003843  2022-10-30 10:07:39
        4  USD/CHF  0.99600  0.99600  ...  0.99802  0.004985  2022-10-30 10:07:39

        [5 rows x 8 columns]
        """
        return self.data(
            url_version="v3",
            path="fx",
            params=None,
        )

    @property
    def cryptos(self):
        """Query FMP / quotes/crypto / API.

        Returns the latest real-time price (and more) for available cryptocurrencies.
        *To get a list of all supported cryptos, use the Symbols class.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> quotes = Quotes(apikey="abc123")
        >>>
        >>> crypto_quotes = quotes.cryptos
        >>> print(crypto_quotes.head())
             symbol           name  ...  sharesOutstanding   timestamp
        0    TTTUSD    Tapcoin USD  ...                NaN  1667138358
        1   VBNBUSD  Venus BNB USD  ...       8.432710e+07  1667138358
        2  CHESSUSD  ChessCoin USD  ...       5.403276e+07  1667138358
        3    BHDUSD  BitcoinHD USD  ...       6.083017e+06  1667138358
        4    DAIUSD        Dai USD  ...       9.422326e+09  1667138358

        [5 rows x 22 columns]
        """
        return self.data(
            url_version="v3",
            path="quotes/crypto",
            params=None,
        )

    @property
    def nyse(self):
        """Query FMP / quotes/nyse / API.

        Returns the latest real-time price (and more) for stocks
        within the New York Stock Exchange (NYSE).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> quotes = Quotes(apikey="abc123")
        >>>
        >>> nyse_quotes = quotes.nyse
        >>> print(nyse_quotes.head())
           symbol                                  name  ...  sharesOutstanding   timestamp
        0    FUSE              Fusion Acquisition Corp.  ...         43750000.0  1667138358
        1    CELP  Cypress Environmental Partners, L.P.  ...         12341801.0  1667138358
        2    SNPR         Tortoise Acquisition Corp. II  ...         43125000.0  1667138358
        3  IVR-PA         Invesco Mortgage Capital Inc.  ...         81159105.0  1667138358
        4     WPF     Foley Trasimene Acquisition Corp.  ...        129374996.0  1667138358

        [5 rows x 22 columns]
        """
        return self.data(
            url_version="v3",
            path="quotes/nyse",
            params=None,
        )

    @property
    def tsx(self):
        """Query FMP / quotes/tsx / API.

        Returns the latest real-time price (and more) for stocks
        within the Toronto Stock Exchange (TSX).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> quotes = Quotes(apikey="abc123")
        >>>
        >>> tsx_quotes = quotes.tsx
        >>> print(tsx_quotes.head())
            symbol  ...   timestamp
        0   PBI.TO  ...  1667138367
        1  PFMN.TO  ...  1667138367
        2  LEAD.TO  ...  1667138367
        3   SVR.TO  ...  1667138367
        4   BSX.TO  ...  1667138367

        [5 rows x 22 columns]
        """
        return self.data(
            url_version="v3",
            path="quotes/tsx",
            params=None,
        )

    @property
    def euronext(self):
        """Query FMP / quotes/euronext / API.

        Returns the latest real-time price (and more) for stocks
        within the Euronext Exchange (EURONEXT).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> quotes = Quotes(apikey="abc123")
        >>>
        >>> euronext_quotes = quotes.euronext
        >>> print(euronext_quotes.head())
             symbol  ...   timestamp
        0   IBMA.BR  ...  1667138769
        1  BEES4.SA  ...  1667138769
        2  CIEL3.SA  ...  1667138769
        3  ALLEX.PA  ...  1667138769
        4    SAN.MC  ...  1667138769

        [5 rows x 22 columns]
        """
        return self.data(
            url_version="v3",
            path="quotes/euronext",
            params=None,
        )
