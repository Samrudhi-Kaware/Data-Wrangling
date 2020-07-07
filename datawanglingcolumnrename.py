import pandas as pd
import numpy as np


def function1():
    df = pd.read_csv('employees.csv')

    print(df.columns)

    # rename the columns
    # df_new = df.rename(columns={'First Name': 'FirstName', 'Start Date': 'StateDate', 'Bonus %': 'Bonus'})
    df.rename(columns={'First Name': 'FirstName', 'Start Date': 'StartDate', 'Bonus %': 'Bonus'}, inplace=True)
    print(df.columns)

    # rename the columns with all upper case characters
    # axis:
    # - 0: rows
    # - 1: columns
    # function alias
    df.rename(str.lower, axis='columns', inplace=True)
    print(df.columns)


function1()


def function2():
    df = pd.read_csv('employees.csv')
    # df = pd.read_csv('employees.csv', usecols=['Salary', 'Team'])
    print(df.columns)

    # drop the First Name
    # df.drop('First Name', axis='columns', inplace=True)
    # df.drop('Last Login Time', axis='columns', inplace=True)

    # df.drop(['First Name', 'Last Login Time'], axis='columns', inplace=True)

    del df['First Name']
    del df['Last Login Time']

    # df.drop([0], inplace=True)
    print(df.columns)


function2()
def function3():
    df = pd.DataFrame([
        {"city": "pune", "temperature": '24', "humidity": 20},
        {"city": "mumbai", "humidity": 40, "temperature": '21'},
        {"city": "satara", "temperature": '22', "humidity": 50}
    ])

    # print(pd.to_numeric(df['temperature']))
    print(df.loc[:, 'temperature'])
    # print(df['temperature'])


#function3()
def function4():
    df_temp = pd.DataFrame([
        {"city": "pune", "temperature": '24'},
        {"city": "mumbai", "temperature": '21'},
        {"city": "satara", "temperature": '22'},
        {"city": "nashik", "temperature": '29'}
    ])

    df_humidity = pd.DataFrame([
        {"city": "pune", "humidity": '50'},
        {"city": "mumbai", "humidity": '40'},
        {"city": "satara", "humidity": '60'},
        {"city": "karad", "humidity": '60'}
    ])

    # merging the the temp and humidity based on city
    # df_final = pd.merge(df_temp, df_humidity, on='city')
    # df_final = pd.merge(df_temp, df_humidity, on='city', how='left')
    df_final = pd.merge(df_temp, df_humidity, on='city', how='right', indicator=True)
    print(df_final)
function4()

