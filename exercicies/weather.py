"""nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
 + What was the average temperature in first week of Jan
 + What was the maximum temperature in first 10 days of Jan."""

arr = []

def open_csv(csv):
    """Handle csv data extraction."""
    with open(csv, 'r') as data:
        for line in data:
            ids = line.split(',')
            try:
                tempeture = int(ids[1])
                arr.append(tempeture)
            except:
                print('')
    

def get_average_tempeture(days):
    if days > 10 or days < 0:
        raise Exception('The days input are invalid')
    
    open_csv('nyc_weather.csv')

    tempetures = 0
    for i in range(0, days):
        tempetures += arr[i]

    average_tempeture = tempetures / days
    return print(f'The average tempeture in the first {days} days of jan was {average_tempeture}')


def get_max_tempeture(days):
    if days > 10 or days < 0:
        raise Exception('The days input are invalid')

    open_csv('nyc_weather.csv')
    max_tempeture = max(arr[0:days])
    return print(f'The max tempeture in the first {days} days of jan was {max_tempeture}')


if __name__ == "__main__":
    get_average_tempeture(7)
    get_max_tempeture(10)