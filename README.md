# Fi-Pye

# Table of Contents

   * [About the project](#about-the-project)
   * [Getting Started](#getting-started)
     * [Installation](#installation)
     * [Usage](#usage)
        * [Readers](#readers)
          * [Example #1](#example-1)
          * [Example #2](#example-2)

## About The Project

---
Fi-Pye is a library written in python for obtaining financial
data from Financial Modeling Prep. Since data is obtained from FMP's API,
you must have an API token in order to use this library.

# Getting Started

Since you must have an API token from FMP to use Fi-Pye, if you don't have one
already you can check out their developer documentation [here](https://site.financialmodelingprep.com/developer/docs/):

### Installation
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
readers, you must use the following import statement.
```python
from fi_pye.readers.fmp import Fundamentals
```

### Example #2
To access the USTreasury reader, which is one of the Nasdaq readers, you must use the 
following import statement.
```python
from fi_pye.readers.nasdaq import USTreasury
```





