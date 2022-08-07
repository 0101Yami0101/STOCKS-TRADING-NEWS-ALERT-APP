import requests
from datetime import *
from twilio.rest import Client




#Datetime
today = date.today() #default
# new_today = today - timedelta(days = 2) #Incase the day is saturday or sunday this logic can be applied and replaced with today date
yesterday = today - timedelta(days = 1)
daybefore_yesterday = today - timedelta(days = 2)


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNCTION = "TIME_SERIES_DAILY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = "NEKALGFL563FS36P"
stock_parameters = {
    "function": FUNCTION,
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
stock_data = response.json()

yesterday_closing_data = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])

day_before_yesterday_closing_data = float(stock_data["Time Series (Daily)"][str(daybefore_yesterday)]["4. close"])

difference = day_before_yesterday_closing_data - yesterday_closing_data
positive_difference = abs(difference)

average_change = (day_before_yesterday_closing_data + yesterday_closing_data)/2
percentage_difference = (positive_difference/average_change)*100



NEWS_API_KEY = "0a184a5b5cf944aabfd9b94a2cb6f901"

if percentage_difference >= 5 :
    print("NEWS")
    news_parameters ={
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }
    r = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = r.json()
    news_articles = news_data['articles']


    #twilio details
    account_sid = "ACb395f4340abc099e6fbffcb1ff018d08"
    auth_token = "85985b20f6f9426387679f68958f26cf"

    for i in range(3):
        newsTitle = news_articles[i]['title']
        newsBrief = news_articles[i]['description']
        article = f"HEADLINE: {newsTitle}\n. Brief: {newsBrief}\n\n"

        
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body= article,
                     from_='+12029785045',
                     to='+916002059806'
                 )
        # print(message.status)
    

  
        
    


 









