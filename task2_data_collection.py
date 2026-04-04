import pandas as pd
import os

#Task 1
#file path
file_loc = "data/trends_20260403.json"

#loading json into DataFrame
df = pd.read_json(file_loc)

#Printing how many rows were loaded
print(f"Loaded{len(df)} stories from {file_loc}")

#________________________________________
#TASk 2 clean the data
#removeing any rows with the same post_id
df = df.drop_duplicates(subset="post_id")
print(f"After droping duplicates: {len(df)}")

#droping rows where post_id, title, or score is missing
df = df.dropna(subset=["post_id","title","score"])
print(f"After removing missing values: {len(df)}")

#score and num_comments must be integer
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

#removing socre less than 5
df = df[df["score"]>= 5]
print(f"Score less than 5 is:{len(df)}")

#removeing extra sapces from the title
df["title"] = df["title"].str.strip()
#__________________________________________


#TASk 3 save as CSV
#saveing the cleaned DataFrame
os.makedirs("data",exist_ok=True)
new_file = "data/trends_clean.csv"
df.to_csv(new_file,index=False)


#printing the output
print(f"\nsaved{len(df)} rows to {new_file}")


#A quike summary
#how many stories by category
print(f"\nStories by Category: ")


category_count = df["category"].value_counts()
for category , count in category_count.items():
    print(f"{category} {count}")