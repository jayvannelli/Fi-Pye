import streamlit as st
from time import perf_counter

from fi_pye.readers.nasdaq import Treasuries

def main():
    start = perf_counter()


    t = Treasuries(st.secrets['NASDAQ_TOKEN'])

    #print(t)
    #print(t.yield_curve())
    #print(t.treasury_yield("1mo"))
    #print(t.long_term_rates())
    #print(t.real_yield_curve())
    #print(t.treasury_real_yield("5yr"))
    #print(t.marketable_issuance_breakdown())
    #print(t.net_non_marketable_borrowing())
    #print(t.non_marketable_borrowing("slgs"))

    end = perf_counter()
    print(end - start)


if __name__ == "__main__":
    main()
