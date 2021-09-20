# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:21:16 2021

@author: Ahmed
"""
import pandas as pd
import numpy as np
import datetime
import time
import calendar
import click


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def user_input():
    """ Ask the user to input the city, month and weekday"""
    m=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','ALL']
    d=[]
    for i in range(0,7):
        d.append(calendar.day_name[i])
    
    d.append('ALL')
    
    while True:
        try:
            name= click.prompt('What is the city of your choice? [C for Chicago, N for New yourk, W for Washignton]').upper()
            if name=="C":
                city = "chicago"
                print("your City of Choice is ", city)
                break;
            elif name=="N":
                city = "new york city"
                print("your City of Choice is ", city)
                break;
            elif name=="W":
                city = "washington"
                print("your City of Choice is", city)
                break;
            else:
                print("Check your Typing")
                
        except:
            continue
        
        
    while True:
        try:
            month= click.prompt('Please enter a month',m)
            if month in m:
                print('your month of choice is', month)
                break;
            else:
                print('Try again that is not a right choice')

        except:
            continue
    while True:
        try:
            day= click.prompt('Please enter a day',d)
            if day in d:
                print('your day of choice is', day)
                break;
            else:
                print('Try again that is not a right choice')

        except:
            continue
    print('-'*40)   
    return city, month, day
def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable."""
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name(locale='English')
    df['Hour']= df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'ALL':
        # use the index of the months list to get the corresponding int
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'ALL':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month  
    most_popular_month= df['month'].mode()[0]
    print('most common month of year',calendar.month_name[most_popular_month])  
# TO DO: display the most common day of week
    most_popular_day= df['day_of_week'].mode()[0]
    print('most common day of week',most_popular_day)
# TO DO: display the most common start hour
    most_popular_hr= df['Hour'].mode()[0]
    print('most common hour of day',most_popular_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def Station_stat(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_startst= df['Start Station'].mode()[0]
    print('most common start station is ',most_popular_startst)

    # TO DO: display most commonly used end station
    most_popular_endst= df['End Station'].mode()[0]
    print('most common end station is ',most_popular_endst)
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip']= 'From '+ df['Start Station']+' to '+df['End Station']
    most_popular_trip= df['Trip'].mode()[0]
    print('most common trip is ',most_popular_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def Trip_duration(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    Total_Travel_Time= df['Trip Duration'].sum()

    # TO DO: display mean travel time
    Average_Travel_Time= df['Trip Duration'].mean()
    print('total time is {} and Average Travel Time is {}'.format(Total_Travel_Time,Average_Travel_Time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def User_type(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_types= df['User Type'].value_counts().to_frame()
    print(User_types)

    # TO DO: Display counts of gender
    while True:
        try:
            Gender_types= df['Gender'].value_counts().to_frame()
            print(Gender_types)
            break;
        except:
            print('No Gender for this city')
            break;
    

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            Youngest= df['Birth Year'].max()
            print('earliest year of birth', Youngest)
            break;
        
        except:
            print('no Date of Birth for this city')
            break;
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = user_input()
        df = load_data(city, month, day)
        
        time_stats(df)
        Station_stat(df)
        Trip_duration(df)
        User_type(df)
        #Charts(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main() 