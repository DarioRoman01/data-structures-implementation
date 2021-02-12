"""nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
 + What was the average temperature in first week of Jan
 + What was the maximum temperature in first 10 days of Jan."""

arr = []
weather_dict = {}

def open_csv_to_array(csv):
    """Extract the data and put it in to array"""
    with open(csv, 'r') as data:
        for line in data:
            ids = line.split(',')
            try:
                tempeture = int(ids[1])
                arr.append(tempeture)
            except:
                print('')

def open_csv_to_dict(csv):
    """Extract the data and put it in to dict"""
    with open(csv, 'r') as data:
        for line in data:
            ids = line.split(',')
            days = ids[0]
            try:
                tempeture = int(ids[1])
                weather_dict[days] = tempeture
            except:
                print('')
                

def get_average_tempeture(days):
    if days > 10 or days < 0:
        raise Exception('The days input are invalid')
    
    open_csv_to_array('nyc_weather.csv')

    average_tempeture = sum(arr[0:7])/len(arr[0:7])
    return print(f'The average tempeture in the first {days} days of jan was {average_tempeture}')


def get_max_tempeture(days):
    if days > 10 or days < 0:
        raise Exception('The days input are invalid')

    open_csv_to_array('nyc_weather.csv')
    max_tempeture = max(arr[0:days])
    return print(f'The max tempeture in the first {days} days of jan was {max_tempeture}')

def get_day_tempeture(day):
    if day > 10 or day < 0:
        raise Exception('Invalid date')
    
    open_csv_to_dict('nyc_weather.csv')

    day_tempeture = weather_dict[f'Jan {day}']
    return print(f'the tempeture on day {day} was {day_tempeture}')

if __name__ == "__main__":
    # What was the average temperature in first week of Jan?
    get_average_tempeture(7)

    # What was the maximum temperature in first 10 days of Jan?
    get_max_tempeture(10)

    # What was the temperature on Jan 9?
    get_day_tempeture(9)

    # What was the temperature on Jan 4
    get_day_tempeture(4)
    