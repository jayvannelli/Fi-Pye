import logging
import requests
import datetime as dt
import pandas as pd

from pandas import to_datetime

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
    """ """
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


def _get_df(url, params, session):
    """ """
    if session is None:
        raise Exception("requests.Session cannot be None.")

    response = session.get(
        url=url,
        params=params,
        timeout=(CONNECTION_TIMEOUT, READ_TIMEOUT),
    )
    if len(response.json()) == 1 and "Error Message" in response.json():
        raise ValueError("Invalid API token response received.")

    try:
        df = pd.DataFrame(response.json())

        # Historical dividends returns a weird json from FMP, this is for that.
        if 'historical-price-full/stock_dividend/' in url:
            df = pd.DataFrame(response.json()['historical'])

    except Exception as e:
        logging.error(f"DataFrame conversion exception: {e}")

    else:
        if len(df) == 0:
            logging.error(
                "DataFrame appears to be empty. "
                f"Request ( url / params): {url} / {params}. "
                "Returning None."
            )
            return None

        return df


def _validate_sec_filing_type(value):
    """ """
    _valid_values = VALID_SEC_FILING_TYPES
    if value not in _valid_values:
        raise ValueError(
            f"Invalid SEC filing type passed: {value}. "
            f"Valid SEC filing types include: {_valid_values}. "
        )

    return value


def _validate_calendar_dates(start: str, end: str):
    """ """
    try:
        start = to_datetime(start)
        end = to_datetime(end)
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
