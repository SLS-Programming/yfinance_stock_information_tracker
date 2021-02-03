import yfinance as yf
import pandas as pd

print('Please Type a Stock Ticker that you would like to learn more information about\n')
selectedStock = input()

stock = yf.Ticker(selectedStock)

stock.info

print("\nWhat information would you like?\nMajor Holders\nCashflow\nBalance Sheet\nRecommendations\nCalendar\n")

chosenInfo = input()

if chosenInfo == 'Major Holders':
    print(stock.major_holders)
elif chosenInfo == 'Cashflow':
    print(stock.quarterly_cashflow)
elif chosenInfo == 'Balance Sheet':
    print(stock.quarterly_balance_sheet)
elif chosenInfo == 'Recommendations':
    print(stock.recommendations)
elif chosenInfo == 'Calendar':
    print(stock.calendar)
else:
    print("error")



# tickers = ["AAPL"]
# yf.download(tickers, start = "2014-01-01", end = "2018-12-31")