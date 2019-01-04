import pandas as pd
import os, re
import ast
import csv
from textblob import TextBlob

df = pd.read_csv(os.path.expanduser(r"~/Desktop/670projectdata/initialdata.csv"), encoding='unicode_escape', sep=",")

for index, row in df.iterrows():
    ST_Airline_Name = row['Airline_Name']
    ST_review = row['Reviews']
    item = ST_review.split(',')
    for rev in item:
        print_list = []
        blob = TextBlob(rev)
        polarity = blob.polarity
        subjectivity = blob.subjectivity
        rev = re.sub('[^a-zA-Z0-9| \n\.]', '', rev)
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        print_list = [ST_Airline_Name, rev, polarity, subjectivity, sentiment]


        with open(os.path.expanduser(r"~/Desktop/670projectdata/sentiment.csv"),"a",encoding='utf-8') as w_file:
                csv_app = csv.writer(w_file)
                csv_app.writerow(print_list)


