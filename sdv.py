import requests

# Jacob McIntosh API Key: LIE8L1SQATAK0ZTM


# the following functions need code to validate the user input.

    # the stock symbol should exist in the API, same with the chart type and time series function

    # the dates should be checked to make sure they are in the proper format and valid (beginning
    # date should not be in the future, end date should not be before start date, etc.)

def get_stock_symbol():
    stock_symbol = input("Please enter the company's stock symbol: ")

    # input validation goes here






    
    
    return stock_symbol

def get_chart_type():
    print("Chart Types\n----------------")
    print("1. Bar\n")
    print("2. Line\n\n")
    chart_type = input("Please enter the chart type you would like (1, 2): ")

    # if/elif/else that converts the number user entered into the desired chart type,
    # else statement can be used for input validation








    
    return chart_type

def get_time_series_func():
    print("Select the Time Series of the chart you want to Generate\n----------------------------")
    print("1. Intraday\n")
    print("2. Daily\n")
    print("3. Weekly\n")
    print("4. Monthly\n\n")
    time_series = input("Please enter the time series function you would like to use (1, 2, 3, 4): ")

    # if/elif/else that converts the number user entered into the desired time series chart,
    # else statement can be used for input validation






    
    return time_series

def get_beginning_date():
    date1 = input("Please enter the beginning date (YYYY-MM-DD): ")

    # input validation goes here




    
    return date1

def get_end_date():
    date2 = input("Please enter the end date (YYYY-MM-DD): ")

    # input validation goes here



    
    
    return date2

def make_url():
    ss = get_stock_symbol()
    ct = get_chart_type()
    ts = get_time_series_func()
    d1 = get_beginning_date()
    d2 = get_end_date()

    # use stringbuider to make url containing user input?
    





    return url

# enter other functions below










def main():
    print("Welcome to the Stock Data Visualizer!")
    print("--------------------------------------")





    # the below code is an example from the API's website. Aspects of this URL need to be altered
    # based on user input.

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=LIE8L1SQATAK0ZTM'
    r = requests.get(url)
    data = r.json()

    print(data)

    # returns a bunch of JSON. Need to use pygal to generate graph and lxml to open graph in browser.


main()
