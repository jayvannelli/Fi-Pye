import streamlit as st
from time import perf_counter

from fi_pye.readers.nasdaq.sp500_ratios import SP500Ratios

def main():
    start = perf_counter()

    s = SP500Ratios(st.secrets['NASDAQ_TOKEN'])

    print(s)
    print(s.dividend_yield("month"))

    end = perf_counter()
    print(end - start)


if __name__ == "__main__":
    main()
