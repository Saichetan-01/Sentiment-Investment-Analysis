import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Create a Streamlit app
st.title('Indian Stock Price Visualization')

# User input for date range
start_date = st.date_input("Start date", pd.to_datetime('2023-01-01'))
end_date = st.date_input("End date", pd.to_datetime('2024-01-01'))

# Example tickers for Indian stocks (NSE)
tickers = ['TATASTEEL.NS', 'RELIANCE.NS', 'INFY.NS', 'HDFCBANK.NS', 'SBIN.NS']

# Function to fetch stock data
def fetch_stock_data(tickers, start_date, end_date):
    all_data = {}
    for ticker in tickers:
        try:
            stock_data = yf.download(ticker, start=start_date, end=end_date)
            if not stock_data.empty:
                all_data[ticker] = stock_data
        except Exception as e:
            st.error(f"Error fetching data for {ticker}: {e}")
    return all_data

# Fetch stock data
stock_data_dict = fetch_stock_data(tickers, start_date, end_date)

if stock_data_dict:
    for ticker, stock_data in stock_data_dict.items():
        st.subheader(f'Stock Prices for {ticker}')

        # Display the stock data table
        st.dataframe(stock_data)

        # Create a figure and axis object
        fig, ax = plt.subplots()

        # Plotting
        ax.plot(stock_data.index, stock_data['Close'], marker='o', linestyle='-')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.set_title(f'{ticker} Stock Price')

        # Display the plot in Streamlit
        st.pyplot(fig)
else:
    st.error("No data available to display.")
