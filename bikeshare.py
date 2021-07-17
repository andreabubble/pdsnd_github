import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
        try: 
            city = input("Do you want to explore data from Chicago, New York City or Washington?\n")
           
            if city.lower() in CITY_DATA:
                city = city.lower()
                break
            
        except:
            print("This is not a valid input for city.")
            
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try: 
            month = input("What month(s) do you want to explore? Options: all, January, February, March, April, June)\n")
            if month.lower() in months:
                month = month.lower()
                break
            elif month.lower() == 'all':
                month = month.lower()
                break
        except:
            print("This is not a valid input for month.")
    
 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try: 
            day = input("What day(s) do you want to explore? Options: all, Monday, Tuesday, Wednesday, Saturday, Sunday)\n")
            if day.lower() in days:
                day = day.lower()
                break
            elif day.lower() == 'all':
                day = day.lower()
                break
            
        except:
            print("This is not a valid input for day.")
    
    print('Your selection is {}, {}, {}'.format(city.title(), month.title(), day.title()))
    
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
    #this function I've taken from the Practice Solution #3 in the course
    df = pd.read_csv(CITY_DATA[city])
  
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
 
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
 
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("{} is the most common month".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("{} is the most common day of week".format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("{} is the most common start hour.".format(df['hour'].mode()[0]))
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("{} is the most common start station.".format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print("{} is the most common end station.".format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    print("{} is the most common start and end station combination.".format(df.groupby(['Start Station','End Station']).size().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("{} is the total travel time.".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("{} is the mean travel time.".format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Different users types with their total count: \n", df['User Type'].value_counts())
    
    if 'Gender' in df and 'Birth Year' in df:
        # TO DO: Display counts of gender
        print("Different genders and total count: \n", df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print("The oldest customer is born in {}".format(int(df['Birth Year'].min())))
        print("The youngest customer is born in {}".format(int(df['Birth Year'].max())))
        print("{} is the year where most of customers are born".format(df['Birth Year'].value_counts().idxmax()))
        
    else:
        print("User Gender and Birth Year information is not available for this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_display(df):
    i=1
    raw_display = input('\nWould you like to see individual trip data? Enter yes or no.\n')
    while raw_display == 'yes':
        print(df.iloc[[i, i+1, i+2, i+3, i+4]])
        i +=5
        raw_display = input('\nWould you like to see individual trip data? Enter yes or no.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        raw_display(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
