from .reader import Reader


class ExchangeTradedFunds(Reader):
    """Exchange Traded Funds (ETF). """

    def available_dates(self, symbol: str):
        """Query FMP / etf-holdings/portfolio-date / API.

        Returns a list of available dates for an ETF (by symbol)
        which can be used in the func 'portfolio_holdings'.

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="etf-holdings/portfolio-date",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def available_dates_by_cik(self, cik: str):
        """Query FMP / etf-holdings/portfolio-date / API.

        Returns a list of available dates for an ETF (by CIK number)
        which can be used in the func 'portfolio_holdings'.

        Parameters
        ----------
        cik :
            Exchange Traded Fund (ETF) CIK number

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="etf-holdings/portfolio-date",
            params={
                "cik": cik,
                "apikey": self.apikey,
            },
        )

    def portfolio_holdings(self, symbol: str, date: str):
        """Query FMP / etf-holdings / API.

        Returns the portfolio holdings of a specified ETF (by symbol)
        and on a given date. To get available dates for a specific
        ETF, query 'available_dates' or 'available_dates_by_cik'.

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol
        date :
            Date to get portfolio holdings from in 'YYYY-MM-DD' format

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="etf-holdings",
            params={
                "symbol": symbol.upper(),
                "date": date,
                "apikey": self.apikey,
            },
        )

    def portfolio_holdings_by_cik(self, cik: str, date: str):
        """Query FMP / etf-holdings / API.

        Returns the portfolio holdings of a specified ETF (by CIK number)
        and on a given date. To get available dates for a specific
        ETF, query 'available_dates' or 'available_dates_by_cik'.

        Parameters
        ----------
        cik :
            Exchange Traded Fund (ETF) CIK number
        date :
            Date to get portfolio holdings from in 'YYYY-MM-DD' format

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="etf-holdings",
            params={
                "cik": cik,
                "date": date,
                "apikey": self.apikey,
            },
        )

    def expense_ratio(self, symbol: str):
        """Query FMP / etf-holdings / API.

        Returns information about a given ETF (by symbol).

        Some ETF info returned:
            - Assets under management (AUM)
            - CUSIP
            - Description
            - ISIN
            - Net asset value (NAV)
            - ...

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v4",
            path="etf-info",
            params={
                "symbol": symbol.upper(),
                "apikey": self.apikey,
            },
        )

    def country_weightings(self, symbol: str):
        """Query FMP / etf-country-weightings / API.

        Returns specific ETF (by symbol) portfolio exposure by country.

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"etf-country-weightings/{symbol.upper()}",
            params={"apikey": self.apikey},
        )

    def sector_weightings(self, symbol: str):
        """Query FMP / etf-sector-weightings / API.

        Returns specific ETF (by symbol) portfolio exposure by sector.

        Parameters
        ----------
        symbol :
            Exchange Traded Fund (ETF) ticker symbol

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"etf-sector-weightings/{symbol.upper()}",
            params={"apikey": self.apikey},
        )
