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
    print("1. Bar")
    print("2. Line\n")
    chart_type = int(input("Please enter the chart type you would like (1, 2): "))

    # if/elif/else that converts the number user entered into the desired chart type,
    # else statement can be used for input validation
    
    if chart_type == 1 or chart_type == 2:
        return chart_type
    else:
        print("INPUT ERROR: Please enter 1 or 2\n")
        get_chart_type()
             
    #return chart_type

def get_time_series_func():
    print("Select the Time Series of the chart you want to Generate\n----------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly\n")
    time_series = input("Please enter the time series function you would like to use (1, 2, 3, 4): ")
    res = ''
    # if/elif/else that converts the number user entered into the desired time series chart,
    # else statement can be used for input validation

    if(time_series == '1'):
        res = "TIME_SERIES_INTRADAY"
    elif(time_series == '2'):
        res = "TIME_SERIES_DAILY"
    elif(time_series == '3'):
        res = "TIME_SERIES_WEEKLY"
    elif(time_series == '4'):
        res = "TIME_SERIES_MONTHLY"

    return res

def get_interval():
    interval = input("Please enter the time interval (in minutes) you would like to use (1, 5, 15, 30, 60): ")

    return interval


def get_beginning_date():
    date1 = input("\nPlease enter the beginning date (YYYY-MM-DD): ")

    # input validation goes here




    
    return date1

def get_end_date():
    date2 = input("\nPlease enter the end date (YYYY-MM-DD): ")

    # input validation goes here



    
    
    return date2

def make_url():
    url = 'https://www.alphavantage.co/query?function='
    ss = get_stock_symbol()
    ct = get_chart_type()
    ts = get_time_series_func()
    
    if(ts == "TIME_SERIES_INTRADAY"):
        ti = get_interval()
        return url + ts + "&symbol=" + ss + "&interval=" + ti + "min&apikey=LIE8L1SQATAK0ZTM"

    else:
        return url + ts + "&symbol=" + ss + "&apikey=LIE8L1SQATAK0ZTM"

# enter other functions below










def main():
    print("Welcome to the Stock Data Visualizer!")
    print("--------------------------------------\n")





    # the below code is an example from the API's website. Aspects of this URL need to be altered
    # based on user input.

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    #url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=LIE8L1SQATAK0ZTM'
    r = requests.get(make_url())
    data = r.json()

    print(data)

    # returns a bunch of JSON. Need to use pygal to generate graph and lxml to open graph in browser.


main()
