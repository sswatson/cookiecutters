
SUBJECT = "{{ cookiecutter.subject }}"

import pandas as pd
df = pd.read_csv("email-addresses.csv")
df

import yagmail
yag = yagmail.SMTP("samuel_watson@brown.edu", useralias = "Samuel S. Watson")
def contents(row):
    return f"""
    Dear {row.Name},



    Best,
    Sam
    """

row = list(df.itertuples())[0]
yag.send(to = samuel.s.watson@gmail.com, 
         subject = SUBJECT, 
         contents = contents(row))

for row in df.itertuples():
    yag.send(to=row.Email, 
             subject = SUBJECT, 
             cc = "daniel_potter@brown.edu", 
             contents = contents(row))
