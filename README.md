# OGS Trading Bot (*traderbot*)

> *Automatic Trading Bot built  with python to implement my trading strategy.*

![Python version][python-version]
![Latest version][latest-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

NOTE: This project was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

## Initial setup

```zsh
cd Projects
git clone https://github.com/clamytoe/traderbot.git
cd traderbot
```

### Anaconda setup

If you are an Anaconda user, this command will get you up to speed with the base installation.

```zsh
conda env create
conda activate traderbot
```

### Regular Python setup

If you are just using normal Python, this will get you ready, but I highly recommend that you do this in a virtual environment.
There are many ways to do this, the simplest using *venv*.

```zsh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Final setup

```zsh
pip install -e .
```

## Usage

```zsh
traderbot
```

The output should be: `Successfully installed your project file: traderbot`

## Possible indicators

- Value vs P/E ratio
- Earnings beats estimates
- Trends outside market
- Pre-IPO information
  - How did they fund
  - Who is backing

## 🛠️ Flask Dashboard Blueprint: “Projected Value Navigator”

This is a blueprint that I have been working on for my retirement ROTH IRA account. I plan to build it modularly:

### 📥 Input Layer

- CSV or JSON parser for your portfolio holdings
- Optional form for setting share counts, current prices, and custom CAGR assumptions

### 📈 Projection Engine

- Apply per-asset CAGR calculations to estimate 5-year values
- Allow toggling between current price vs. target price mode
- Show thresholds like "Take Profit" and "Buyback Trigger"

### 📊 Visualization Tabs

- Summary table showing current vs projected value, % to target, potential gains
- Timeline graphs to show how projected value compounds
- Pie charts for portfolio composition — present vs projected

### 📤 Output Layer

- Export projected values or thresholds as JSON (ready for alerts or script triggers)
- Optional integration with TradingView price alerts or shell script execution

## Contributing

Contributions are welcomed.
Tests can be run with with `pytest -v`, please ensure that all tests are passing and that you've checked your code with the following packages before submitting a pull request:

* black
* flake8
* isort
* mypy
* pytest-cov

I am not adhering to them strictly, but try to clean up what's reasonable.

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "traderbot" is free and open source software.

## Issues

If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog

* **v0.1.0** Initial commit.

[python-version]:https://img.shields.io/badge/python-3.13.3-brightgreen.svg
[latest-version]:https://img.shields.io/badge/version-0.1.0-blue.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/traderbot.svg
[issues-url]:https://github.com/clamytoe/traderbot/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/traderbot.svg
[fork-url]:https://github.com/clamytoe/traderbot/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/traderbot.svg
[stars-url]:https://github.com/clamytoe/traderbot/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/traderbot.svg
[license-url]:https://github.com/clamytoe/traderbot/blob/main/LICENSE
