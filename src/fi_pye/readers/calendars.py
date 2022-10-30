from .reader import Reader
from .utils import _validate_calendar_dates


class Calendars(Reader):
    """Calendar data from FMPs api."""
    def earnings(self, from_date: str, to_date: str):
        """Query FMP / earning_calendar / API.

        Obtain earnings calendar.
        *FMP allows a MAXIMUM of 3 months between 'from_date' and 'to_date'.

        Parameters
        ----------
        from_date :
            Starting date in 'YYYY-MM-DD' format.
        to_date : default = 'annual'
            Ending date in 'YYYY-MM-DD' format.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(from_date, str) or not isinstance(to_date, str):
            raise TypeError(
                f"Invalid from_date: {from_date} or to_date: {to_date}. "
                f"Type for from_date: {type(from_date)} and to_date: {type(to_date)}. "
                "from_date and to_date must both be of type: str."
            )
        from_d, to_d = _validate_calendar_dates(from_date, to_date)
        return self.data(
            url_version="v3",
            path="earning_calendar",
            params={
                "from": from_d,
                "to": to_d,
                "apikey": self.apikey
            },
        )

    def confirmed_earnings(self, from_date: str, to_date: str):
        """Query FMP / earning-calendar-confirmed / API.

        Obtain only the confirmed earnings calendar.
        *FMP allows a MAXIMUM of 3 months between 'from_date' and 'to_date'.

        Parameters
        ----------
        from_date :
            Starting date in 'YYYY-MM-DD' format.
        to_date : default = 'annual'
            Ending date in 'YYYY-MM-DD' format.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(from_date, str) or not isinstance(to_date, str):
            raise TypeError(
                f"Invalid from_date: {from_date} or to_date: {to_date}. "
                f"Type for from_date: {type(from_date)} and to_date: {type(to_date)}. "
                "from_date and to_date must both be of type: str."
            )
        from_d, to_d = _validate_calendar_dates(from_date, to_date)
        return self.data(
            url_version="v4",
            path="earning-calendar-confirmed",
            params={
                "from": from_d,
                "to": to_d,
                "apikey": self.apikey
            },
        )

    def economic(self, from_date: str, to_date: str):
        """Query FMP / economic_calendar / API.

        Obtain economic calendar.
        *FMP allows a MAXIMUM of 3 months between 'from_date' and 'to_date'.

        Parameters
        ----------
        from_date :
            Starting date in 'YYYY-MM-DD' format.
        to_date : default = 'annual'
            Ending date in 'YYYY-MM-DD' format.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(from_date, str) or not isinstance(to_date, str):
            raise TypeError(
                f"Invalid from_date: {from_date} or to_date: {to_date}. "
                f"Type for from_date: {type(from_date)} and to_date: {type(to_date)}. "
                "from_date and to_date must both be of type: str."
            )
        from_d, to_d = _validate_calendar_dates(from_date, to_date)
        return self.data(
            url_version="v3",
            path="economic_calendar",
            params={
                "from": from_d,
                "to": to_d,
                "apikey": self.apikey
            },
        )

    def dividends(self, from_date: str, to_date: str):
        """Query FMP / stock_dividend_calendar / API.

        Obtain dividends calendar (for the entire market, not a specific stock).
        *FMP allows a MAXIMUM of 3 months between 'from_date' and 'to_date'.

        Parameters
        ----------
        from_date :
            Starting date in 'YYYY-MM-DD' format.
        to_date : default = 'annual'
            Ending date in 'YYYY-MM-DD' format.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(from_date, str) or not isinstance(to_date, str):
            raise TypeError(
                f"Invalid from_date: {from_date} or to_date: {to_date}. "
                f"Type for from_date: {type(from_date)} and to_date: {type(to_date)}. "
                "from_date and to_date must both be of type: str."
            )
        from_d, to_d = _validate_calendar_dates(from_date, to_date)
        return self.data(
            url_version="v3",
            path="stock_dividend_calendar",
            params={
                "from": from_d,
                "to": to_d,
                "apikey": self.apikey
            },
        )

    def ipos(self, from_date: str, to_date: str):
        """Query FMP / ipo_calendar / API.

        Obtain initial public offering (IPO) calendar.
        *FMP allows a MAXIMUM of 3 months between 'from_date' and 'to_date'.

        Parameters
        ----------
        from_date :
            Starting date in 'YYYY-MM-DD' format.
        to_date : default = 'annual'
            Ending date in 'YYYY-MM-DD' format.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(from_date, str) or not isinstance(to_date, str):
            raise TypeError(
                f"Invalid from_date: {from_date} or to_date: {to_date}. "
                f"Type for from_date: {type(from_date)} and to_date: {type(to_date)}. "
                "from_date and to_date must both be of type: str."
            )
        from_d, to_d = _validate_calendar_dates(from_date, to_date)
        return self.data(
            url_version="v3",
            path="ipo_calendar",
            params={
                "from": from_d,
                "to": to_d,
                "apikey": self.apikey
            },
        )

    def confirmed_ipos(self, from_date: str, to_date: str):
        """Query FMP / ipo-calendar-confirmed / API.

        Obtain only the confirmed initial public offering (IPO) calendar.
        *FMP allows a MAXIMUM of 3 months between 'from_date' and 'to_date'.

        Parameters
        ----------
        from_date :
            Starting date in 'YYYY-MM-DD' format.
        to_date : default = 'annual'
            Ending date in 'YYYY-MM-DD' format.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(from_date, str) or not isinstance(to_date, str):
            raise TypeError(
                f"Invalid from_date: {from_date} or to_date: {to_date}. "
                f"Type for from_date: {type(from_date)} and to_date: {type(to_date)}. "
                "from_date and to_date must both be of type: str."
            )
        from_d, to_d = _validate_calendar_dates(from_date, to_date)
        return self.data(
            url_version="v4",
            path="ipo-calendar-confirmed",
            params={
                "from": from_d,
                "to": to_d,
                "apikey": self.apikey
            },
        )

    def ipos_w_prospectus(self, from_date: str, to_date: str):
        """Query FMP / ipo-calendar-prospectus / API.

        Obtain initial public offering (IPO) calendar (with prospectus).
        *FMP allows a MAXIMUM of 3 months between 'from_date' and 'to_date'.

        Parameters
        ----------
        from_date :
            Starting date in 'YYYY-MM-DD' format.
        to_date : default = 'annual'
            Ending date in 'YYYY-MM-DD' format.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(from_date, str) or not isinstance(to_date, str):
            raise TypeError(
                f"Invalid from_date: {from_date} or to_date: {to_date}. "
                f"Type for from_date: {type(from_date)} and to_date: {type(to_date)}. "
                "from_date and to_date must both be of type: str."
            )
        from_d, to_d = _validate_calendar_dates(from_date, to_date)
        return self.data(
            url_version="v4",
            path="ipo-calendar-prospectus",
            params={
                "from": from_d,
                "to": to_d,
                "apikey": self.apikey
            },
        )

    def stock_splits(self, from_date: str, to_date: str):
        """Query FMP / stock_split_calendar / API.

        Obtain initial public offering (IPO) calendar.
        *FMP allows a MAXIMUM of 3 months between 'from_date' and 'to_date'.

        Parameters
        ----------
        from_date :
            Starting date in 'YYYY-MM-DD' format.
        to_date : default = 'annual'
            Ending date in 'YYYY-MM-DD' format.

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        if not isinstance(from_date, str) or not isinstance(to_date, str):
            raise TypeError(
                f"Invalid from_date: {from_date} or to_date: {to_date}. "
                f"Type for from_date: {type(from_date)} and to_date: {type(to_date)}. "
                "from_date and to_date must both be of type: str."
            )
        from_d, to_d = _validate_calendar_dates(from_date, to_date)
        return self.data(
            url_version="v3",
            path="ipo_calendar",
            params={
                "from": from_d,
                "to": to_d,
                "apikey": self.apikey
            },
        )


class StockCalendars(Reader):
    """For historical stock calendar. """

    def historical_earnings(self, symbol: str, limit: int = 25):
        """Query FMP / historical/earning_calendar / API.

        Obtain historical earnings calendar.

        Parameters
        ----------
        symbol :
            Stock ticker symbol
        limit : default = 25
            Number of rows to return

        Return
        -------
        object : pandas.DataFrame
            pandas.Dataframe
        """
        return self.data(
            url_version="v3",
            path=f"historical/earning_calendar/{symbol.upper()}",
            params={
                "limit": limit,
                "apikey": self.apikey
            },
        )

    def historical_dividends(self, symbol: str):
        """Query FMP / historical-price-full/stock_dividend / API.

        Obtain historical earnings calendar.

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
            url_version="v3",
            path=f"historical-price-full/stock_dividend/{symbol.upper()}",
            params={"apikey": self.apikey},
        )