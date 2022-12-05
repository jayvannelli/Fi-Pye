import requests
import pandas as pd


CONNECTION_TIMEOUT = 5
READ_TIMEOUT = 30

VALID_SEC_FILING_TYPES = [
    "10-Q", "8-K", "4", "13F-HR", "3", "SD", "PX14A6G", "DEFA14A",
    "DEF 14A", "424B5", "FWP", "PRE 14A", "SC 13G/A", "UPLOAD",
    "CORRESP", "SC 13G", "10-K", "424B2", "IRANNOTICE", "S-8",
    "S-3ASR", "3/A", "5", "POS AM", "424B3", "S-4", "S-8 POS",
    "8-K/A", "CT ORDER", "NO ACT", "ARS"
]


def _init_session(session=None):
    """Initialize requests session. """
    if session is None:
        session = requests.Session()
    else:
        if not isinstance(session, requests.Session):
            raise TypeError("session must be a requests.Session")

    return session


def _construct_url(url_version, path):
    """ """
    _valid_values = ["v3", "v4"]
    if url_version not in _valid_values:
        raise ValueError(
            f"Invalid url version: {url_version}. "
            "The only available url versions are 'v3' and 'v4'. "
        )

    else:
        return f"https://financialmodelingprep.com/api/{url_version}/{path}"


def _format_multiple_symbols(symbols: list[str]) -> str:
    """
    Used to format the 'symbols' param for a Price reader.

    The 'symbols' param is used when multiple symbols are being
    passed (for batch quotes / price history). This function
    ensures that a list was passed and that each of the items
    in the list is of type string. If those two requirements are
    met, the response will be a comma separated string containing
    an uppercase version of each symbol within the symbols list.
    """
    if not isinstance(symbols, list):
        raise TypeError(
            f"Invalid symbols type passed: {symbols} is of type {type(symbols)}. "
            "symbols must be of type list. "
        )

    for symbol in symbols:
        if not isinstance(symbol, str):
            raise TypeError(
                f"Invalid symbol passed within list of symbols: {symbols}. "
                f"Invalid symbol type passed: {symbol} is of type {type(symbol)}. "
                "symbol must be of type string (str). "
            )

    return ",".join([symbol.upper() for symbol in symbols])


def _validate_sec_filing_type(value):
    """
    Validates that the SEC form passed to a SEC reader is a
    valid form that FMP can return data for.
    """
    _valid_values = VALID_SEC_FILING_TYPES
    if value not in _valid_values:
        raise ValueError(
            f"Invalid SEC filing type passed: {value}. "
            f"Valid SEC filing types include: {_valid_values}. "
        )

    return value


def _validate_calendar_dates(start: str, end: str):
    """Validates 'from_date' and 'to_date' args passed to a Calendar reader method."""
    try:
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
    except (TypeError, ValueError):
        raise ValueError("Invalid date format.")

    if start > end:
        raise ValueError("start date must be earlier than end date.")

    diff = end - start

    if diff.days > 90:
        raise ValueError(
            "FMP allows a maximum of 3 months between the 'from' and 'to' dates. "
            f"Passed start date: {start} and end date: {end} . "
        )

    else:
        return start, end


def _validate_price_dates(start: str, end: str):
    """Validates 'from_date' and 'to_date' args passed to a Price reader method."""
    if not isinstance(start, str):
        raise TypeError(
            f"Invalid from date: {start} with type: {type(start)}. "
            "from date must be of type string (str) and in 'YYYY-MM-DD' format. "
        )

    if not isinstance(end, str):
        raise TypeError(
            f"Invalid from date: {end} with type: {type(end)}. "
            "from date must be of type string (str) and in 'YYYY-MM-DD' format. "
        )

    try:
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
    except (TypeError, ValueError):
        raise ValueError("Invalid date format.")

    if start > end:
        raise ValueError("start date must be earlier than end date.")

    return start, end


def _clean_historical_daily_price(data):
    """
    The historical daily price response from FMP is not the normal
    response, which is a list of dictionaries. This function is
    used to take the normal response from this endpoint and
    fix the formatting so the returned DataFrame contains only the
    intended data in a cleaner way.

    Parameters
    ---------
    data :
        Original response from the historical daily price endpoint.

    Return
    ------
    object : pandas.DataFrame
        pandas.Dataframe
    """
    columns = [
        "open", "high", "low", "close", "adjClose", "volume",
        "unadjustedVolume", "change", "changePercent", "vwap", "label",
        "changeOverTime"
    ]
    df = pd.DataFrame(index=[i['date'] for i in data['historical']])

    for c in columns:
        df[c] = [h[c] for h in data['historical']]

    return df
