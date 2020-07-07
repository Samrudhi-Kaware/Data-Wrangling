import pandas as pd
import numpy as np


def function1():
    df = pd.read_csv('employees.csv')

    print(df.Salary)

    # add new column
    df['NewBonus'] = df.Salary * 0.10
    df['Dummy'] = 0

    print(df.head())


# function1()


def function2():
    df = pd.read_csv('employees.csv')

    # print(df.head(10))

    # select avg(Salary) from df group by Team
    result = df.groupby('Team')
    # print(df.groupby('Team'))

    for team, team_df in result:
        print(team)
        #print(team_df)
        print(team_df.Salary.mean())
        print(f"min    : {team_df.Salary.min()}")
        print(f"max    : {team_df.Salary.max()}")

        print('---' * 40)
#function2()
def function3():
    df = pd.read_csv('employees.csv')

    # print(df[df.Team == 'Sales'])
    # print(df.query("Team == 'Sales'"))

    # avg of salary for senior management in Teams = 'Sales'
    print(df.query("Team == 'Sales'").groupby('Senior Management').mean())


function3()