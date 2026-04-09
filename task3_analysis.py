import pandas as pd
import numpy as np

#loading csv file into pandas dataframe
df = pd.read_csv("data/trends_clean.csv")

#data shape rows and columns
print("loaded data: ",df.shape)

#print first 5 rows
print("\nFirst 5 rows: ")
print(df.head())

#The average of sccore and num_comments 
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

#printing average score and num_comments
print("\nAverage score",round(avg_score,2))
print("Average comments",round(avg_comments,2))

#analysis with numpy
scores = df["score"].to_numpy() # converty to numpy
mean_score = np.mean(scores)
median_score = np.median(scores) #this all are statistics with numpy
std_score = np.std(scores)
min_score = np.max(scores) #highest score min and max
max_score = np.max(scores)
print("\n___numpy statistics____")
print("mean score",round(mean_score, 2))
print("median score",round(median_score,2))
print("standed deivation",round(std_score,2))
print("max score",max_score)
print("min score",min_score)

#category with most stories
categroy_counts = df["category"].value_counts()
top_category = categroy_counts.idxmax()
top_count = categroy_counts.max()
print("\nMost stories in:{top_category}({top_counts}stories)")

#story with most comments
max_comments_row = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story: ")
print(f'"{max_comments_row["title"]}" - {max_comments_row["num_comments"]} comments')

#adding new column(engagement and is_popular)
df["engagement"] = df["num_comments"] / (df["score"]+1)
df["is_popular"] = df["score"] > avg_score

#saveing the result with two new columns
df.to_csv("data/trends_analysed.csv",index=False)
print("\nSaved to data/trends_analysed.csv")
