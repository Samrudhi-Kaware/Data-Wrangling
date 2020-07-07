#Data cleaning
import pandas as pd
import numpy as np
def function1():
    df = pd.read_csv('employees.csv')
    # print(df.columns)
    # print(df.info())
    #print(df.describe())
    #print(df.head())
    # check the NaN in entire dataframe
    # print(df.isna())

    # check the NaN in Team column
    #print(df.Team.isna())
    # check selecting or filtering data
    print(df[df.Team.isna()])
    #check count
    print(df.isna().sum())
    # handle the missing data
    #replace NAN with 0
    # df_new = df.fillna(0)
    # print(df_new)
    # print(df_new[df_new.Team.isna()])
    #it returns new df
    #df_new = df.fillna({"Team": "No Team", "Gender": "Male", "Salary": 0})
    #print(df_new)
    #modify current df
    df.fillna({"Team": "No Team", "Gender": "Male", "Salary": 0}, inplace=True)
    print(df)
    # replace the invalid values
    # df.replace(['NaN', 'No Team', -1, 10000000], [0, 'NA', 0, 0])
    print(df)
function1()


def function2():
    df = pd.DataFrame([
         {"city": "pune", "temperature": 24, "humidity": 20},
#         {"city": "mumbai", "temperature": 30, "humidity": 40},
         {"city": "mumbai", "humidity": 40},
         {"city": "satara", "temperature": 22, "humidity": 50}
     ])

    df = pd.DataFrame({
        "city": ['pune', 'mumbai', 'satara'],
        "temperature": [24, 30, 22],
        "humidity": [20, 40, 50]
    })
    # df.fillna(0, inplace=True)
    # df.fillna(20, inplace=True)
    #df.fillna(method='ffill', inplace=True)#forward fill
    df.fillna(method='bfill', inplace=True)  # backward fill
    print(df)


#function2()
def function3():
    df = pd.read_csv('employees.csv')

    print(df.Gender)

    # convert the textual values to numeric ones
    # Male = 1, Female = 2
    # df.replace(['Male', 'Female'], [1, 2], inplace=True)
    # print(df.Gender)

    # convert the textual values to numeric ones
    unique_teams = df.Team.unique()
    print(unique_teams)

    replacements = range(1, len(unique_teams) + 1)
    print(replacements)

    df.replace(unique_teams, replacements, inplace=True)
    print(df)


function3()