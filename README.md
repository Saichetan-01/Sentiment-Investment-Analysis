# Sentimental Investment Analysis

## Overview

The **Sentimental Investment Analysis** project combines financial data analysis with sentiment analysis to provide insights into stock investments. This project fetches historical stock data, retrieves related news articles, analyzes their sentiment, and visualizes the results to assist in making informed investment decisions.

## Features

- Fetch historical stock data for various tickers using `yfinance`.
- Retrieve and analyze news articles' sentiment using the News API and VADER sentiment analysis.
- Visualize stock price trends, sentiment analysis results, and their correlation.
- Interactive web app using Streamlit to visualize Indian stock prices.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**

   Run the following command to clone the repository:
   `git clone https://github.com/Saichetan-01/sentimental-investment-analysis.git`
   Then navigate to the project directory:
   `cd sentimental-investment-analysis`

2. **Create and Activate a Virtual Environment (optional but recommended)**

   Create a virtual environment:
   `python -m venv venv`
   Activate the virtual environment:
   - On macOS/Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`

3. **Install Required Packages**

   Install all necessary Python packages using pip:
   `pip install yfinance pandas numpy matplotlib seaborn requests vaderSentiment streamlit`

## Usage

### Sentiment Analysis Script

1. **Set Up Your API Key:**
   - Obtain your API key from [NewsAPI](https://newsapi.org/) and set it in the script.

2. **Run the Sentiment and Stock Analysis Script:**

   Execute the script with the following command:
   `python sentiment_investment_analysis.py`

   This script performs the following:
   - Fetches stock data for a given ticker and date range.
   - Retrieves news articles and performs sentiment analysis.
   - Merges stock and sentiment data, calculates sentiment momentum, and applies a basic investment strategy.
   - Plots stock prices, sentiment, and their correlations.

### Streamlit App

1. **Run the Streamlit App:**

   Start the Streamlit app with the following command:
   `streamlit run app.py`

   The Streamlit app features:
   - A user interface to input date ranges.
   - Visualization of stock prices for selected Indian stocks (NSE).
   - Display of stock data in tabular form and as time series plots.

## Dependencies

The project relies on the following Python packages:

- `yfinance` - For fetching stock market data.
- `pandas` - For data manipulation and analysis.
- `numpy` - For numerical operations.
- `matplotlib` - For plotting data visualizations.
- `seaborn` - For statistical data visualization.
- `requests` - For making HTTP requests to the News API.
- `vaderSentiment` - For performing sentiment analysis on news articles.
- `streamlit` - For creating an interactive web application.

## Notes

- Ensure that you replace the placeholder API key in `sentiment_investment_analysis.py` with your actual News API key.
- You may need to adjust date ranges and tickers based on your specific requirements.
- For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/Saichetan-01/sentimental-investment-analysis/issues).

## Acknowledgments

- [NewsAPI](https://newsapi.org/) for providing news articles.
- [VADER](https://github.com/cjhutto/vaderSentiment) for sentiment analysis.
