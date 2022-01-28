# TDA of financial time series

This web app is a reimplementation of the paper
[TDA of financial time series: Landscapes of crashes](https://arxiv.org/abs/1703.04385)
using [gudhi](https://gudhi.inria.fr).


# Interactive dashboard from notebook with Voilà

## How to run it?

| Voilà | JupyterLab |
| :-----------------------: | :---------------------: |
| [![voila-binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GUDHI/tda_financial_time_series/HEAD?urlpath=voila%2Frender%2Findex.ipynb)| [![jupyterlab-binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GUDHI/tda_financial_time_series/HEAD?urlpath=lab%2Ftree%2Findex.ipynb) |


Binder or Voilà instance creation may take some time, but it requires no local installation.

### Local installation

One can install it easily from conda:

* Install [miniconda3](https://conda.io/miniconda.html) environment .
* Create a new conda environment and activate it:

```bash
conda env create -f environment.yml
conda activate tda_financial_time_series
```

### Run the web app

```bash
voila tda_web_app.ipynb
```

```bash
jupyter lab tda_web_app.ipynb
```

## Data generation

Data are generated using Yahoo! finance pip module to get the four major US stock market
indices: S&P 500, DJIA, NASDAQ, and Russel 2000. To install Yahoo! finance pip module:

```bash
conda install pip --yes
pip install yfinance
```

To generate the data with the latest values (should be done by the Continuous Integration automatically):

```bash
python data_generation.py
```

A new version of `latest.csv` is generated.