# Predicting Price Moves with News Sentiment

## Overview

This project was completed as part of the Nova Financial Solutions challenge, which investigates the relationship between financial news sentiment and stock market behavior.

The objective is to determine whether sentiment extracted from financial news headlines can provide useful signals for predicting stock price movements. The project combines Natural Language Processing (NLP) techniques with technical analysis indicators and statistical correlation analysis.

---

## Business Objective

Financial markets generate enormous volumes of news every day. Some headlines influence investor behavior and stock prices, while others have little impact. Nova Financial Solutions aims to improve financial forecasting capabilities by integrating qualitative information from financial news with quantitative stock market data.

This project focuses on:

* Performing exploratory analysis of financial news data
* Extracting sentiment scores from news headlines
* Computing technical indicators from historical stock data
* Measuring the relationship between news sentiment and stock returns
* Generating insights that could support sentiment-informed investment strategies

---

## Dataset Description

### Financial News Dataset

The news dataset contains:

* Headline text
* Publisher information
* Publication timestamps
* Stock ticker symbols
* Article URLs

The dataset includes over 1.4 million financial news records.

### Historical Stock Price Dataset

Historical stock data was obtained through Yahoo Finance and contains:

* Date
* Open
* High
* Low
* Close
* Volume

The analysis focused on major technology stocks including:

* AAPL
* AMZN
* GOOG
* META
* NVDA

---

## Project Structure

```text
news-sentiment-analysis/
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── data/
│   └── raw/
│
├── notebooks/
│   ├── task1_eda.ipynb
│   ├── task2_technical_analysis.ipynb
│   └── task3_sentiment_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── indicators.py
│   ├── sentiment.py
│   └── correlation.py
│
├── tests/
│   ├── __init__.py
│   └── test_indicators.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Tasks Completed

### Task 1: Exploratory Data Analysis

Key analyses performed:

* Headline length distribution
* Publisher activity analysis
* Publication frequency trends
* Keyword extraction and topic exploration
* News volume visualization

Key findings:

* Financial headlines are generally short and information-dense
* News publication is concentrated among a small number of publishers
* Publication volume fluctuates significantly over time

---

### Task 2: Technical Analysis

Technical indicators were computed using TA-Lib:

#### Simple Moving Average (SMA)

Used to smooth price fluctuations and identify trends.

#### Relative Strength Index (RSI)

Used to identify overbought and oversold conditions.

#### Moving Average Convergence Divergence (MACD)

Used to identify momentum changes and possible trend reversals.

Visualizations were created to compare stock prices with technical indicators.

---

### Task 3: Sentiment and Correlation Analysis

#### Sentiment Analysis

Sentiment scores were generated using VADER (Valence Aware Dictionary and Sentiment Reasoner).

Each headline received a compound sentiment score.

#### Stock Returns

Daily stock returns were calculated using percentage change in closing prices.

#### Correlation Analysis

News sentiment and stock returns were aligned by trading day and analyzed using the Pearson correlation coefficient.

Result:

* Pearson Correlation ≈ 0.048

This indicates a weak positive relationship between sentiment and short-term stock returns.

---

## Technologies Used

### Data Analysis

* Python
* Pandas
* NumPy

### Visualization

* Matplotlib

### Natural Language Processing

* VADER Sentiment Analysis

### Financial Analysis

* TA-Lib

### Development Tools

* Git
* GitHub
* GitHub Actions
* Jupyter Notebook

---

## Installation

Clone the repository:

```bash
git clone https://github.com/lydiab04/news-sentiment-analysis.git
cd news-sentiment-analysis
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Run notebooks in the following order:

1. task1_eda.ipynb
2. task2_technical_analysis.ipynb
3. task3_sentiment_analysis.ipynb

---

## Key Findings

* Financial news sentiment exhibits a weak positive relationship with stock returns.
* Technical indicators provide valuable information about market momentum and trend direction.
* News sentiment alone is insufficient for accurate prediction but may serve as a useful supplementary signal.
* Combining sentiment analysis with technical indicators may improve investment decision-making.

---

## Limitations

* Missing timestamps reduced the amount of usable news data.
* Correlation does not imply causation.
* Sentiment models may not fully capture financial context.
* Market movements are influenced by many external variables beyond news sentiment.

---

## Future Work

Potential extensions include:

* Deep learning-based sentiment models
* Multi-day lag analysis
* Real-time news ingestion pipelines
* Predictive machine learning models
* Larger stock universe analysis

---

## Author

Lydia B.

Project completed for the Nova Financial Solutions Financial News Sentiment Analysis Challenge.
