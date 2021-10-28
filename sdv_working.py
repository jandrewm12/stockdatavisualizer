import json
import pygal
import lxml
import requests
from datetime import datetime

# Jacob McIntosh API Key: LIE8L1SQATAK0ZTM

# this function asks the user for a company's stock symbol
# and returns that symbol
def get_stock_symbol():
    stock_symbol = input("Please enter the company's stock symbol: ")    
    return stock_symbol

# this function asks a user if they would like to generate
# a bar or line graph, then returns their choice
def get_chart_type():
    while True:
        try:
            print("\nChart Types\n----------------")
            print("1. Bar")
            print("2. Line\n")
            chart_int = int(input("Please enter the chart type you would like (1, 2): "))
            chart_type = ""

            if chart_int == 1: chart_type = "bar"
            elif chart_int == 2: chart_type = "line"
            else: 
                print("Please enter either 1 or 2\n")
                continue
            break
        except ValueError:
            print("Please enter either 1 or 2\n")
            continue
    return chart_type

# this functions asks the user which time series they would like
# then returns their choice
def get_time_series_func():
    while True:
        try:
            print("\nSelect the Time Series of the chart you want to Generate\n----------------------------")
            print("1. Intraday")
            print("2. Daily")
            print("3. Weekly")
            print("4. Monthly")
            time_series = int(input("\nPlease enter the time series function you would like to use (1, 2, 3, 4): "))

            ts = ""
            if time_series == 1: ts = "TIME_SERIES_INTRADAY"
            elif time_series == 2: ts = "TIME_SERIES_DAILY"
            elif time_series == 3: ts = "TIME_SERIES_WEEKLY"
            elif time_series == 4: ts = "TIME_SERIES_MONTHLY"
            else: 
                print("Please enter the integer corresponding to your desired Time Series.")
                continue
            break
        except ValueError:
            print("Please enter the integer corresponding to your desired Time Series.")
            continue
    return ts

# this functions gets the beginning date of the data to be graphed
def get_beginning_date():
    while True:
        try:
            date1 = input("\nPlease enter the beginning date (YYYY-MM-DD): ")
            split_date = date1.split('-')

            year = int(split_date[0])
            month = int(split_date[1])
            day = int(split_date[2])

            beginning_date = datetime(year, month, day)
            current_date = datetime.today()

            if beginning_date > current_date:
                print("Beginning date must be before current date.")
                continue
            break
        except:
            print("Please enter a beginning date in proper YYYY-MM-DD format.")
            continue
    return beginning_date.strftime('%Y-%m-%d')

# this functions gets the end date of the data to be graphed
def get_end_date(beginning_date):
    while True:
        try:
            date2 = input("\nPlease enter the end date (YYYY-MM-DD): ")
            split_date = date2.split('-')
            split_beginning_date = beginning_date.split('-')

            year = int(split_date[0])
            month = int(split_date[1])
            day = int(split_date[2])

            year2 = int(split_beginning_date[0])
            month2 = int(split_beginning_date[1])
            day2 = int(split_beginning_date[2])

            ending_date = datetime(year, month, day)
            begin_date = datetime(year2, month2, day2)
            current_date = datetime.today()

            if begin_date > ending_date:
                print("Ending date must be after beginning date.")
                continue
            elif ending_date > current_date:
                print("Ending date must be equal to or before the current date.")
                continue
            break
        except:
            print("Please enter an ending date in proper YYYY-MM-DD format.")
            continue
    return ending_date.strftime('%Y-%m-%d')

# this function concatenates the necessary information the user entered
# into a URL to be sent to the API
def make_url(stock_symbol, time_series):
    url = "https://www.alphavantage.co/query?function=" + time_series + "&symbol=" + stock_symbol + "&interval=5min&outputsize=full&apikey=LIE8L1SQATAK0ZTM"
    return url

# gets JSON data from API using the url 
def get_json(url):
    r = requests.get(url)
    data = r.json()
    return data

# this function parses the JSON data
def parse_json(data):
    data = str(data)
    data = data.replace("'", '"')
    parsed_json = json.loads(str(data))
    return parsed_json

# this function creates a chart based on whether the user
# chose a bar or line graph
def choose_graph(chart_type):
    if chart_type == 'bar': line_chart = pygal.Bar(x_label_rotation=40)
    elif chart_type == 'line': line_chart = pygal.Line(x_label_rotation=40)
    return line_chart

# main function
def main():
    print("Welcome to the Stock Data Visualizer!")
    print("--------------------------------------")
    while True:
        try:
            # get all user input
            ss = get_stock_symbol()
            ct = get_chart_type()
            ts = get_time_series_func()
            d1 = get_beginning_date()
            d2 = get_end_date(d1)

            # make URL for API query
            url = make_url(ss, ts)
            # get JSON data
            json_data = get_json(url)
            # parse JSON data
            parsed_json = parse_json(json_data)

            # change the time series string to a string that can 
            # be used to access data in the parsed_json variable
            if ts == "TIME_SERIES_INTRADAY":
                ts = "Time Series (5min)"
            elif ts == "TIME_SERIES_DAILY":
                ts = "Time Series (Daily)"
            elif ts == "TIME_SERIES_WEEKLY": 
                ts = "Weekly Time Series"
            elif ts == "TIME_SERIES_MONTHLY":
                ts = "Monthly Time Series"

            # lists to hold open, high, low, and close prices for stocks
            open_list = []
            high_list = []
            low_list = []
            close_list = []

            # the below for loop loops through the json data, assigning each price
            # to its respective list.

            beginning_date_split = d1.split("-")
            ending_date_split = d2.split("-")

            beg_year = int(beginning_date_split[0])
            beg_month = int(beginning_date_split[1])
            beg_day = int(beginning_date_split[2])

            end_year = int(ending_date_split[0])
            end_month = int(ending_date_split[1])
            end_day = int(ending_date_split[2])

            beg_date = datetime(beg_year, beg_month, beg_day)
            end_date = datetime(end_year, end_month, end_day)

            # date_list is used for generating a list of dates to use for x_values
            date_list = []
            for date in parsed_json[ts]:
                d = date.split("-")
                dy = int(d[0])
                dm = int(d[1])
                dd = d[2]
                
                if len(dd.split()) > 1:
                    dd = dd.split()
                    d_day = int(dd[0])
                    dt = dd[1]
                    dt_split = dt.split(":")
                    dhour = int(dt_split[0])
                    dmin = int(dt_split[1])
                    dsec = int(dt_split[2])
                    d_date = datetime(dy, dm, d_day, dhour, dmin, dsec)
                else: d_date = datetime(dy, dm, int(dd))


                # if statement filters out data that is outside range of beginning and end dates
                if beg_date <= d_date and d_date <= end_date:
                    date_list.append(date)
                    open_list.append(float(parsed_json[ts][date]["1. open"]))
                    high_list.append(float(parsed_json[ts][date]["2. high"]))
                    low_list.append(float(parsed_json[ts][date]["3. low"]))
                    close_list.append(float(parsed_json[ts][date]["4. close"]))
                else: continue
            
            # reverses the data because the dates are in reverse chronological order
            date_list.reverse()
            open_list.reverse()
            high_list.reverse()
            low_list.reverse()
            close_list.reverse()

            # the following code makes the chart
            title = "Stock Data for " + ss + ": " + d1 + " to " + d2

            line_chart = choose_graph(ct)
            line_chart.title = title
            line_chart.x_labels = map(str, date_list)
            line_chart.add('Open', open_list)
            line_chart.add('High', high_list)
            line_chart.add('Low', low_list)
            line_chart.add('Close', close_list)
            line_chart.render_in_browser()

            # asks the user if they would like to generate another graph
            do_again = input("Would you like to generate another graph? (y/n): ")
            if do_again != 'y':
                break
        # a KeyError will occur if the user enters an invalid stock symbol
        except KeyError as error:
            print("You must enter a valid stock symbol.\nPlease try again.")
        # if an unknown error occurs, the user will be notified and the program will terminate
        except Exception as err:
            print("AN ERROR HAS OCCURRED\n")
            print(err)

# main function call
main()
