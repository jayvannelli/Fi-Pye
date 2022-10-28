import streamlit as st
from time import perf_counter
from src.readers import ExchangeTradedFunds, Holders

def main():
    start = perf_counter()

    f = ExchangeTradedFunds(st.secrets['FMP_TOKEN'])
    h = Holders(st.secrets['FMP_TOKEN'])

    st.write(f)
    st.write(h)
    st.write(h.etf_holders("aapl"))
    st.write(f.available_dates("spy"))
    st.write(f.portfolio_holdings("spy", "2022-03-31"))
    st.write(f.country_weightings("spy"))
    st.write(f.expense_ratio("spy"))

    end = perf_counter()
    print(end - start)


if __name__ == "__main__":
    main()
