import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime, timedelta

# Initialize sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# News API key and URL
NEWS_API_KEY = '07aee89ea6b741988a92fcb0ce852558'  # Replace with your actual API key
NEWS_API_URL = 'https://newsapi.org/v2/everything'

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def fetch_news(ticker, start_date, end_date):
    try:
        response = requests.get(NEWS_API_URL, headers={
            'Authorization': f'Bearer {NEWS_API_KEY}'
        }, params={
            'q': ticker,
            'from': start_date,
            'to': end_date,
            'language': 'en',
            'pageSize': 100
        })
        response.raise_for_status()  # Raise an error for bad responses
        articles = response.json()
        return pd.DataFrame(articles.get('articles', []))
    except Exception as e:
        print(f"Error fetching news: {e}")
        return pd.DataFrame()

def analyze_sentiment(df):
    if df.empty:
        print("No news data available to analyze.")
        return df
    
    content_column = 'content'  # Adjust based on actual column name from API
    if content_column not in df.columns:
        print(f"Column '{content_column}' not found in DataFrame.")
        return df

    df['sentiment'] = df[content_column].apply(lambda x: sentiment_analyzer.polarity_scores(x)['compound'] if x else 0)
    return df

def preprocess_data(stock_data, news_data):
    if news_data.empty:
        print("No news data available to preprocess.")
        return pd.DataFrame()

    news_data['publishedAt'] = pd.to_datetime(news_data['publishedAt']).dt.tz_localize(None)
    news_data.set_index('publishedAt', inplace=True)
    news_data = news_data[['sentiment']].resample('D').mean()  # Aggregate sentiment by day

    stock_data.reset_index(inplace=True)
    stock_data['Date'] = pd.to_datetime(stock_data['Date']).dt.tz_localize(None)
    merged_data = pd.merge(stock_data, news_data, left_on='Date', right_index=True, how='inner')

    return merged_data

def calculate_sentiment_momentum(df):
    if df.empty:
        print("No data available to calculate sentiment momentum.")
        return pd.DataFrame()
    
    df['Sentiment_Momentum'] = df['sentiment'].diff().fillna(0)
    return df

def custom_investment_strategy(df):
    if df.empty:
        print("No data available to apply investment strategy.")
        return pd.DataFrame()

    df['Signal'] = df.apply(lambda row: 'Buy' if row['sentiment'] > 0.5 and row['Sentiment_Momentum'] > 0 else 'Sell', axis=1)
    return df

def plot_with_custom_header(df):
    if df.empty:
        print("No data available to plot.")
        return
    
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Actual Prices', color='blue')
    plt.plot(df['Date'], df['Close'].rolling(window=7).mean(), label='7-Day Moving Average', linestyle='--', color='gray')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price Prediction\nby Chetan')  # Replace 'Your Name' with your actual name
    plt.legend()
    plt.grid(True)
    plt.show()

def styled_heatmap(correlation_matrix):
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='Blues', linewidths=0.5, linecolor='white')
    plt.title('Correlation Between Stock Price and Sentiment\nby Chetan')  # Replace 'Your Name' with your actual name
    plt.show()

def sentiment_vs_stock_price(df):
    if df.empty:
        print("No data available to plot sentiment vs. stock price.")
        return
    
    plt.figure(figsize=(12, 6))
    plt.scatter(df['sentiment'], df['Close'], alpha=0.5, color='blue')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Stock Price')
    plt.title('Sentiment vs. Stock Price\nby Chetan')  # Replace 'Your Name' with your actual name
    plt.grid(True)
    plt.show()

# Example usage
end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')  # Fetch news from the last month

data = fetch_stock_data('AAPL', start_date, end_date)
news_df = fetch_news('Apple', start_date, end_date)
news_df = analyze_sentiment(news_df)
merged_data = preprocess_data(data, news_df)
merged_data = calculate_sentiment_momentum(merged_data)
recommendations = custom_investment_strategy(merged_data)

# Plot results
plot_with_custom_header(merged_data)
if not merged_data.empty:
    styled_heatmap(merged_data[['Close', 'sentiment']].corr())
    sentiment_vs_stock_price(merged_data)
