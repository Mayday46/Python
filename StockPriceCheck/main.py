import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from emailSending import myEmail, emailPassword, sendMail
from Credentials import STOCK_API_KEY, news_API_KEY

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stocks_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}


response = requests.get(STOCK_ENDPOINT, params = stocks_params)
# print(response.json())
Json_Data = response.json()["Time Series (Daily)"]
# print(Json_Data)
Date = [key for key, value in Json_Data.items()] # Data -> Returns all the DATE
Stock_Data = [value for key, value in Json_Data.items()] # Stock_Data -> Returns all the Stock Info associated with DATE
# print("Data -> ", Date)
# print("Stock_Data -> ", Stock_Data)

yesterday_data = Stock_Data[0]
yesterday_Closing_Price = yesterday_data['4. close'] # Same as saying Stock_Data[0]['4. close']
yesterday_Closing_Price_Date = Date[0] # Return Yesterdays Date.
print(f"Date {yesterday_Closing_Price_Date}, Closing Price: {yesterday_Closing_Price}.")


#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday = Stock_Data[1]
day_before_Closing_Price = day_before_yesterday['4. close']
day_before_Closing_Price_Date = Date[1]
print(f"Date {yesterday_Closing_Price_Date}, Closing Price: {day_before_Closing_Price}.")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp


positiveDifference = abs(float(yesterday_Closing_Price) - float(day_before_Closing_Price ))
print(f"{yesterday_Closing_Price} - {day_before_Closing_Price} = {positiveDifference}")


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

Percentage = (positiveDifference / float(yesterday_Closing_Price)) * 100
print(f"Percentage Difference: {Percentage}")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if Percentage > 0:
    # print("Get News")
    news_params = {
        "apiKey": news_API_KEY,
        'q': COMPANY_NAME
    }
    news_reponse = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_reponse.json()['articles']
    # print(articles)

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

firstThree = articles[:3] # Slicing -> Return the first three
# print(firstThree)

format = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in firstThree]



for article in format:
    sendMail(article)


