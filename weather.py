import csv
from datetime import datetime
import weather

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
   
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    # temp=input("What is the temperature in Celsius today: ")
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
print(convert_f_to_c(temp_in_f))
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

    # 1. Open the csv file
    
    if not csv_file:
        return []   
    data = []
    with open(csv_file, mode='r') as file:
     # 2. Read the file and store the data in a list
        reader = csv.reader(file)
    # 3. Skip the header row
        next(reader)
        for row in reader:
            if row:  # Skip empty rows
    # 4. Convert all values to float except the date (first column)
                converted_row = [row[0]] + [float(x) for x in row[1:]]
                data.append(converted_row)
    # 5. Return the data as a list of lists
    return data

print(repr(load_data_from_csv("tests/data/example_one.csv")))



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # 1. Check if the input is empty
    # 2. If empty, return an empty tuple
    # 3. If not empty, find the minimum value and its index
 
    if not weather_data:
        return ()
    min_value = float(weather_data[0])
    min_index = 0
    for i, value in enumerate(weather_data):
        value = float(value)
        if value <= min_value:
            min_value = value
            min_index = i
    # 4. Return the minimum value and its index as a tuple 
    return (min_value, min_index)




def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    max_value = float(weather_data[0])
    max_index = 0
    for i, value in enumerate(weather_data):
        value = float(value)
        if value >= max_value:
            max_value = value
            max_index = i
    # Return the maximum value and its index as a tuple
   
    return (max_value, max_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
     
    if not weather_data:
        return "No data provided.\n"

    num_days = len(weather_data)
    # Convert all temperatures from F to C for summary
    min_temps = [convert_f_to_c(day[1]) for day in weather_data]
    max_temps = [convert_f_to_c(day[2]) for day in weather_data]
               

    min_temp, min_index = find_min(min_temps)
    max_temp, max_index = find_max(max_temps)

    min_date = convert_date(weather_data[min_index][0])
    max_date = convert_date(weather_data[max_index][0])

    mean_low = calculate_mean(min_temps)
    mean_high = calculate_mean(max_temps)

    summary = (
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(f'{min_temp:.1f}')}, and will occur on {min_date}.\n"
        f"  The highest temperature will be {format_temperature(f'{max_temp:.1f}')}, and will occur on {max_date}.\n"
        f"  The average low this week is {format_temperature(f'{mean_low:.1f}')}.\n"
        f"  The average high this week is {format_temperature(f'{mean_high:.1f}')}.\n"
    )
    return summary


for filename in [
    "tests/data/example_one.csv",
    "tests/data/example_two.csv",
    "tests/data/example_three.csv"
]:
    data = load_data_from_csv(filename)
    print(generate_summary(data))
    print("-" * 40)


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No data provided.\n"


    summary = ""
    for day in weather_data:
        date = convert_date(day[0])
        min_temp_c = format_temperature(f"{convert_f_to_c(day[1]):.1f}")
        max_temp_c = format_temperature(f"{convert_f_to_c(day[2]):.1f}")
        summary += (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {min_temp_c}\n"
            f"  Maximum Temperature: {max_temp_c}\n\n"
        )
    return summary

for filename in [
    "tests/data/example_one.csv",
    "tests/data/example_two.csv",
    "tests/data/example_three.csv"
]:
    data = load_data_from_csv(filename)
    print(generate_daily_summary(data))
    print("-" * 40)
