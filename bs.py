import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago','new york city','washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = (input('Select a city among chicago, new york city and washington, Please stick to the spelling:  '))
        city = city.lower()
        if city not in cities:
            print('Invalid city name.')
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Select a month: January, February, March, April, May, or June. /n you can also Enter all! ')
        month = month.lower()
        if month not in months:
            print('invalid input, Make sure you select one of the months!')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Select a day, you can also select all: ')
        day = day.lower()
        if day not in days:
           print('invalid input, make sure to spell the day correctly! ')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    #create a column for start time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #create a column to to the month
    df['month'] = df['Start Time'].dt.month
    #extract day
    df['week_day'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['week_day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_month = df['month'].mode()[0]
    print('Most common month is: ', most_month)
    # TO DO: display the most common day of week
    most_day = df['week_day'].mode()[0]
    print('Most common day is: ', most_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    print('Most common hour is: ', most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start = df['Start Station'].mode()[0]
    print('Most Common Start Station is: ', most_start)

    # TO DO: display most commonly used end station
    most_end = df['End Station'].mode()[0]
    print('Most Common End Station is: ', most_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_stations = df['Start Station'] + ' to ' + df['End Station']
    print('Most Common Combination of start and end stations is : ', most_stations.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time is: ', round(total_travel,1), ' Hours.')
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean Travel Time is: ', round(mean_travel,1),' Hours.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df.groupby('User Type')['User Type'].count()

    print('Count of user types is: ', user_type)
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Count of Genders is: \n', gender)
    except:
        print('Gender data cannot be determind, SORRY!\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('The Earliest Year of birth is: {}. \nThe Most recent is: {}. \nThe Most Common is: {}'.format(int(earliest_year),int(most_recent),int(common_year)))

    except:
        print('Birth Year Data is Missing, SORRY!\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

start_loc = 0
def view(df):
    """ To Ask the user if he wants to see the first 5 rows of data"""
    start_loc = 0
    while True:
        data_view=input('do you want to see the first 5 rows of data? ')
        data_view=data_view.lower()
        if data_view == 'yes':
            print(df.iloc[start_loc:(start_loc+5)])
            view_more(df)
            break
        elif data_view == 'no':
            break
        else:
            print('Invalid Input!')
def view_more(df):
    """ For continue viewing the data in a seperate function"""
    start_loc=5

    while True:
        cont_view = input('Do you wish to continue? ')
        if cont_view=='no':
            break
        elif cont_view == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5
        else:
            print('invalid input')
            continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
