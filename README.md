# Fi-Pye

# Table of Contents

   * [About the project](#about-the-project)
   * [Getting Started](#getting-started)
     * [Dev docs](#developer-documentation)
     * [Installation](#installation)
     * [Usage](#usage)
        * [Readers](#readers)
          * [Example #1](#example-1)
          * [Example #2](#example-2)

# About The Project

Fi-Pye is a python library for obtaining financial data from 
various sources, like Financial Modeling Prep, Nasdaq Data Link, and many more.

# Getting Started
FMP and Nasdaq both require API tokens to obtain data from them, so you must
obtain those keys prior to using their functionality in this library.

### Developer Documentation
Developer documentation for respective data provider.

- Financial Modeling Prep (FMP) : [link](https://site.financialmodelingprep.com/developer/docs/)
- Nasdaq Data Link : [link](https://data.nasdaq.com/tools/api)

## Installation
...

# Usage
Currently, the fmp readers are close to being fully documented and cleaned up,
but most of the functionality should be good. I'm working on implementing the nasdaq
readers so none of them are ready, but they will start coming up as I finish them.


## Readers
Readers are used to group similar functions/endpoints together under a common 
interface. Also, readers are grouped together based on where the data comes from. 


### Example #1
To access the Fundamentals reader, which is one of the Financial Modeling Prep (FMP) 
readers, do the following:
```python
from fi_pye.readers.fmp import Fundamentals

fundamentals = Fundamentals(apikey='123abc')

data = fundamentals.cash_flow("TSLA", period="quarter", limit=5)
```

### Example #2
To access the USTreasury reader, which is one of the Nasdaq readers, do the following:
```python
from fi_pye.readers.nasdaq import USTreasury

ustreasury = USTreasury(api_key='123abc')

data = ustreasury.real_yield_curve(limit=200)
```





