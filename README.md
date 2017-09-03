# moneytalks

Library for stock data manipulation

## Installation

This package requires Python >= 3.6.

~~~bash
$ git clone https://github.com/vlasenkov/finam.git
$ cd finam
$ pip install .
~~~

## Usage

### Finam

Download dataset:

~~~python
>>> import pandas as pd
>>> from moneytalks.finam import export
>>> url = export.make_url('SBER', start='2016-01-01')  # end = now by default
>>> pd.read_csv(url)  # this guy automatically downloads the data
       <DATE>    <TIME>  <OPEN>   <HIGH>    <LOW>  <CLOSE>     <VOL>
0    20160104  00:00:00   5.828   5.8440   5.6320   5.6560   7586265
1    20160105  00:00:00   5.675   5.6890   5.5370   5.6300   7625315
...
~~~

Update and access dictionary of emitents:

~~~python
>>> export.emitents.update()
>>> export.emitents.bycode['SBER']
Сбербанк (SBER)
~~~

### Moscow Exchange



## License

[MIT](LICENSE)
