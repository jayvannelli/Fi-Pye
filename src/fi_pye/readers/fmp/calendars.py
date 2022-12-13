from .reader import FmpReader
from .utils import _validate_calendar_dates


class Calendars(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related
    to calendars.

    Calendars contain TOTAL market data, not STOCK data.
    This means that the 'earnings', 'dividends' & 'stock_splits'
    methods will return data for the whole market and NOT data
    pertaining to a specific stock's earning, dividend or stock
    split history. For historical calendars of a specific stock's
    events' like earnings and dividends, use StockCalendars.

    Calendars
    ---------
    - Earnings
    - Confirmed Earnings
    - Economic
    - Dividends
    - Stock splits
    - Initial public offerings (IPOs)
    - Confirmed IPOs
    - IPOs with prospectus

    Examples
    --------
    >>> calendars = Calendars(apikey="abc123") # Initialize data source
    >>>
    >>> # Maximum of 3 months between 'from' and 'to' dates
    >>> FROM_DATE = "2022-01-01"
    >>> TO_DATE = "2022-03-25"
    >>>
    >>> # Earnings calendars.
    >>> earnings_cal = calendars.earnings(FROM_DATE, TO_DATE)
    >>> confirmed_earnings_cal = calendars.confirmed_earnings(FROM_DATE, TO_DATE)
    >>>
    >>> # economic, dividend & stock-split calendars.
    >>> economic_cal = calendars.economic(FROM_DATE, TO_DATE)
    >>> dividend_cal = calendars.dividend(FROM_DATE, TO_DATE)
    >>> stock_split_cal = calendars.stock_split(FROM_DATE, TO_DATE)
    >>>
    >>> # IPO calendars.
    >>> ipo_cal = calendars.ipo(FROM_DATE, TO_DATE)
    >>> confirmed_ipo_cal = calendars.confirmed_ipo(FROM_DATE, TO_DATE)
    >>> ipo_w_prospectus_cal = calendars.ipo_w_prospectus(FROM_DATE, TO_DATE)
    """

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

        Examples
        --------
        >>> calendars = Calendars(apikey="abc123") # Initialize data source
        >>>
        >>> earnings_cal = calendars.earnings("2022-01-01", "2022-03-25")
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

        Examples
        --------
        >>> calendars = Calendars(apikey="abc123") # Initialize data source
        >>>
        >>> confirmed_earnings_cal = calendars.confirmed_earnings("2022-01-01", "2022-03-25")
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

        Examples
        --------
        >>> calendars = Calendars(apikey="abc123") # Initialize data source
        >>>
        >>> economic_cal = calendars.economic("2022-01-01", "2022-03-25")
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
            },
        )

    def dividend(self, from_date: str, to_date: str):
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

        Examples
        --------
        >>> calendars = Calendars(apikey="abc123") # Initialize data source
        >>>
        >>> divided_cal = calendars.dividend("2022-01-01", "2022-03-25")
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
            },
        )

    def stock_split(self, from_date: str, to_date: str):
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

        Examples
        --------
        >>> calendars = Calendars(apikey="abc123") # Initialize data source
        >>>
        >>> stock_split_cal = calendars.stock_split("2022-01-01", "2022-03-25")
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
            },
        )

    def ipo(self, from_date: str, to_date: str):
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

        Examples
        --------
        >>> calendars = Calendars(apikey="abc123") # Initialize data source
        >>>
        >>> ipo_cal = calendars.ipo("2022-01-01", "2022-03-25")
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
            },
        )

    def confirmed_ipo(self, from_date: str, to_date: str):
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

        Examples
        --------
        >>> calendars = Calendars(apikey="abc123") # Initialize data source
        >>>
        >>> confirmed_ipo_cal = calendars.confirmed_ipo("2022-01-01", "2022-03-25")
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
            },
        )

    def ipo_w_prospectus(self, from_date: str, to_date: str):
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

        Examples
        --------
        >>> calendars = Calendars(apikey="abc123") # Initialize data source
        >>>
        >>> ipo_w_prospectus_cal = calendars.ipo_w_prospectus("2022-01-01", "2022-03-25")
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
            },
        )


class StockCalendars(FmpReader):
    """
    Query Financial Modeling Prep API endpoints related
    to stock calendars/events.

    StockCalendars is used to obtain stock's historical
    calendar of events like earnings and dividends.

    Examples
    --------
    >>> stock_calendars = StockCalendars(apikey="abc123") # Initialize data source
    >>>
    >>> # Earnings.
    >>> aapl_historical_earnings = stock_calendars.historical_earnings("AAPL")
    >>> tsla_historical_earnings = stock_calendars.historical_earnings("TSLA")
    >>>

    **Using a constant stock symbol**

    >>> stock_calendars = StockCalendars(apikey="abc123") # Initialize data source
    >>>
    >>> SYMBOL = "TSLA"
    >>>
    >>> historical_earnings = stock_calendars.historical_earnings(SYMBOL)
    """

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

        Examples
        --------
        >>> stock_calendars = StockCalendars(apikey="abc123") # Initialize data source
        >>>
        >>> data = stock_calendars.historical_earnings(symbol="AAPL", limit=5)
        """
        return self.data(
            url_version="v3",
            path=f"historical/earning_calendar/{symbol.upper()}",
            params={"limit": limit}
        )
