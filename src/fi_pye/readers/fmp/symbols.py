from .reader import FmpReader


class Symbols(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related
    to all symbols within an asset-class/equity.

    This class is used to obtain a list of stock, index, ETF, commodity,
    FX-pair, and cryptocurrency symbols available for quotes and historical
    price queries from FMPs API.
    """
    @property
    def all_stock_symbols(self):
        """Query FMP / stock/list / API.

        Obtain list of all traded and non-trades stocks.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> all_stocks = symbols.all_stock_symbols
        >>> print(all_stocks.head())
          symbol                     name  ...  exchangeShortName   type
        0    SPY   SPDR S&P 500 ETF Trust  ...               AMEX    etf
        1  CMCSA      Comcast Corporation  ...             NASDAQ  stock
        2    KMI      Kinder Morgan, Inc.  ...               NYSE  stock
        3   INTC        Intel Corporation  ...             NASDAQ  stock
        4     MU  Micron Technology, Inc.  ...             NASDAQ  stock

        [5 rows x 6 columns]
        """
        return self.data(
            url_version="v3",
            path="stock/list",
            params={"apikey": self.apikey},
        )

    @property
    def tradable_stock_symbols(self):
        """Query FMP / stock/list / API.

        Obtain list of only tradable stocks.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> tradable_stocks = symbols.tradable_stock_symbols
        >>> print(tradable_stocks.head())
          symbol  ... exchangeShortName
        0    SPY  ...              AMEX
        1  CMCSA  ...            NASDAQ
        2    KMI  ...              NYSE
        3   INTC  ...            NASDAQ
        4     MU  ...            NASDAQ

        [5 rows x 5 columns]
        """
        return self.data(
            url_version="v3",
            path="available-traded/list",
            params={"apikey": self.apikey},
        )

    @property
    def etf_symbols(self):
        """Query FMP / etf/list / API.

        Obtain list of ETFs.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> etfs = symbols.etf_symbols
        >>> print(etfs.head())
          symbol  ... exchangeShortName
        0    SPY  ...              AMEX
        1    GDX  ...              AMEX
        2    EEM  ...              AMEX
        3    XLF  ...              AMEX
        4    EFA  ...              AMEX

        [5 rows x 5 columns]
        """
        return self.data(
            url_version="v3",
            path="etf/list",
            params={"apikey": self.apikey},
        )

    @property
    def tsx_symbols(self):
        """Query FMP / symbol/available-tsx / API.

        Obtain list of stock symbols trading on the Toronto Stock Exchange (TSX).

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> tsx_stocks = symbols.tsx_symbols
        >>> print(tsx_stocks.head())
           symbol  ... exchangeShortName
        0   NEV.V  ...               TSX
        1  FCE.TO  ...               TSX
        2  MAX.TO  ...               TSX
        3  ALB.TO  ...               TSX
        4  TGZ.TO  ...               TSX

        [5 rows x 5 columns]
        """
        return self.data(
            url_version="v3",
            path="symbol/available-tsx",
            params={"apikey": self.apikey},
        )

    @property
    def euronext_symbols(self):
        """Query FMP / symbol/available-euronext / API.

        Obtain list of stock symbols trading on the Euronext Stock Exchange.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> euronext_stocks = symbols.euronext_symbols
        >>> print(euronext_stocks.head())
             symbol  ... exchangeShortName
        0  TELB4.SA  ...          EURONEXT
        1    CIS.BR  ...          EURONEXT
        2  MROIL.BR  ...          EURONEXT
        3  PPLAB.AS  ...          EURONEXT
        4  MLLOG.PA  ...          EURONEXT

        [5 rows x 5 columns]
        """
        return self.data(
            url_version="v3",
            path="symbol/available-euronext",
            params={"apikey": self.apikey},
        )

    @property
    def index_symbols(self):
        """Query FMP / symbol/available-indexes / API.

        Obtain list of available indexes.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> indexes = symbols.index_symbols
        >>> print(indexes.head())
            symbol                             name  ... stockExchange exchangeShortName
        0     ^TYX          Treasury Yield 30 Years  ...         NYBOT             INDEX
        1     ^FVX           Treasury Yield 5 Years  ...         NYBOT             INDEX
        2     ^TNX          Treasury Yield 10 Years  ...         NYBOT             INDEX
        3    ^HSCE  HANG SENG CHINA ENTERPRISES IND  ...         INDEX             INDEX
        4  ^SPGSCI                   S&P GSCI Index  ...           SNP             INDEX

        [5 rows x 5 columns]
        """
        return self.data(
            url_version="v3",
            path="symbol/available-indexes",
            params={"apikey": self.apikey},
        )

    @property
    def commodities_symbols(self):
        """Query FMP / symbol/available-commodities / API.

        Obtain list of available commodity symbols.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> commodities = symbols.commodities_symbols
        >>> print(commodities.head())
          symbol                             name  ...  stockExchange exchangeShortName
        0  BZUSD  Brent Crude Oil Last Day Financ  ...  NY Mercantile         COMMODITY
        1  B0USD  Mont Belvieu LDH Propane (OPIS)  ...  NY Mercantile         COMMODITY
        2  LHUSX                Lean Hogs Futures  ...            CME         COMMODITY
        3  FCUSX            Feeder Cattle Futures  ...            CME         COMMODITY
        4  GCUSD                            Gold   ...      COMMODITY         COMMODITY

        [5 rows x 5 columns]
        """
        return self.data(
            url_version="v3",
            path="symbol/available-commodities",
            params={"apikey": self.apikey},
        )

    @property
    def crypto_symbols(self):
        """Query FMP / symbol/available-cryptocurrencies / API.

        Obtain list of available cryptocurrency symbols.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> cryptos = symbols.crypto_symbols
        >>> print(cryptos.head())
            symbol               name currency stockExchange exchangeShortName
        0   BIPUSD  MinterNetwork USD      USD           CCC            CRYPTO
        1   CFXUSD        Conflux USD      USD           CCC            CRYPTO
        2  OBSRUSD       Observer USD      USD           CCC            CRYPTO
        3   ECCUSD            ECC USD      USD           CCC            CRYPTO
        4   CCAUSD     CounosCoin USD      USD           CCC            CRYPTO

        [5 rows x 5 columns]
        """
        return self.data(
            url_version="v3",
            path="symbol/available-cryptocurrencies",
            params={"apikey": self.apikey},
        )

    @property
    def fx_currency_pairs(self):
        """Query FMP / symbol/available-forex-currency-pairs / API.

        Obtain list of available foreign exchange (FX) trading pairs.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe

        Example
        -------
        >>> symbols = Symbols(apikey='abc123')
        >>>
        >>> fx_pairs = symbols.fx_currency_pairs
        >>> print(fx_pairs.head())
           symbol     name currency stockExchange exchangeShortName
        0  USDMYR  USD/MYR      MYR           CCY             FOREX
        1  QARUSD  QAR/USD      USD           CCY             FOREX
        2  PLNSEK  PLN/SEK      SEK           CCY             FOREX
        3  EURNOK  EUR/NOK      NOK           CCY             FOREX
        4  GBPEUR  GBP/EUR      EUR           CCY             FOREX

        [5 rows x 5 columns]
        """
        return self.data(
            url_version="v3",
            path="symbol/available-forex-currency-pairs",
            params={"apikey": self.apikey},
        )
