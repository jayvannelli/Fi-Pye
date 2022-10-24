import streamlit as st
from src.interfaces.fundamentals import IFundamentals
from src.readers import Analysts, Symbols, Fundamentals, CompanyInformation
import config
import sys


from time import perf_counter


def main():
    start = perf_counter()


    end = perf_counter()
    print(end - start)


if __name__ == "__main__":
    main()
