import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
   
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    temp=input("What is the temperature in Celsius today: ")
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    
    """Converts and ISO formatted date into a human-readable format.
    
    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # 1. Input is ISO date string --> date = "2021-07-05T07:00:00+08:00"
    # 2. Convert ISO date to date/time object 
    # print(type(iso_string))
    readable_date=datetime.fromisoformat(iso_string)
    # print(type(readable_date))
    # 3. Convert back to string --> Needs to be formatted as "Weekday Date Month Year" format. 
    formatted_date=readable_date.strftime("%A %d %B %Y")
    # print(formatted_date)
    # 4. Return formatted datestring
    return(formatted_date)
    # iso_string = datetime.datetime.now()
    # readable_date = datetime.strftime("%B %d, %Y at %I:%M %p")
    # return(readable_date)
# convert_date("2021-07-06T07:00:00+08:00")
# print(convert_date("2021-07-06T07:00:00+08:00"))

def convert_f_to_c(temp_in_fahrenheit):
   
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    # 1. Input of temperature in Fahrenheit, float data format --> Took the value from the expected output of the tests, see line (64)
    temp_as_float=float(temp_in_fahrenheit)
    print(type(temp_as_float))
    # 2. Convert my temperature from Fahrenheit to Celsius
    temp_in_celsius = (temp_as_float - 32) * 5 / 9
    # print(type(temp_in_celsius))
    # print(temp_in_celsius)
    # 3. Rounded to 1 decimal place
    rounded_value=round(temp_in_celsius,1)
    # print(rounded_value)
    # 4. Return value, A float representing a temperature in degrees Celcius
    return(rounded_value)

 # Call the function
temp_in_f = "90"
# print(convert_f_to_c(temp_in_f))
# expected_result = 32.2


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.
    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # Get input for my weather data to calculate mean --> I am storing the values with temperatures variable
    # Get the sum of all insterted values
    total=0
    for n in weather_data:
        total+=float(n)
    
    # print(total)
    
    # Get the amount of all my values, as how many values do i have
    count=len(weather_data)
    # print(count)
    # Calculate the mean bu dividing the sum with the amount of values
    calculate_mean=total / count
    # print(type(calculate_mean))


    # return my mean value
    return float(calculate_mean)
    
    # Call my Function

# temperature = [49, 57, 56, 55, 53]
# print(calculate_mean(temperature))
# temperature = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
# print(calculate_mean(temperature))
# temperature = ["51", "58", "59", "52", "52", "48", "47", "53"]
# print(calculate_mean(temperature))
# temperature = [-51, -58, -59, -52, -52, -48, -47, -53]
# print(calculate_mean(temperature))

# expected_result = 54


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    data = []
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if row:  # Skip empty rows
    # Convert all values to float except the date (first column)
                converted_row = [row[0]] + [float(x) for x in row[1:]]
                data.append(converted_row)
    return data

print(repr(load_data_from_csv("tests/data/example_one.csv")))



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """




def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
