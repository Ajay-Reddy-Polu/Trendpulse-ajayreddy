import pandas as pd
import matplotlib.pyplot as plt
import os
#loading data
df = pd.read_csv("data/trends_analysed.csv")

#creating output folder
os.makedirs("outputs", exist_ok=True)

#helper function
def shorten_title(title,max_len=50):
    return title[:max_len] + "..." if len(title) > max_len else title

#chart 1 Top 10 stories by score
top10 = df.sort_values(by="score",ascending=False).head(10)
titles = [shorten_title(t) for t in top10["title"]]

plt.figure(figsize=(10,6))
plt.barh(titles,top10["score"])
plt.xlabel("score")
plt.ylabel("stories")

plt.title("Top 10 stories by score")
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

#chart 2 stories per category
category_counts = df["category"].value_counts()

plt.figure(figsize=(8,5))
plt.bar(category_counts.index,category_counts.values)

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

#chart 3 score vs comments
popular = df[df["is_popular"]== True]
non_popular = df[df["is_popular"]== False]

plt.figure(figsize=(8,6))

plt.scatter(popular["score"], popular["num_comments"],label="Popular")
plt.scatter(non_popular["score"],non_popular["num_comments"],label="NOt popular")

plt.xlabel("Score")
plt.ylabel("Number of comments")
plt.title("Score vs Comments")

plt.legend()

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# bonus dashboard
fig, axs = plt.subplots(1,3,figsize=(18,5))

#chart 1 
axs[0].barh(titles,top10["score"])
axs[0].set_title("Top Stories")
axs[0].invert_yaxis()

#cahrt 2
axs[1].bar(category_counts.index,category_counts.values)
axs[1].set_title("categories")

#cahrt 3
axs[2].scatter(popular["score"],popular["num_comments"], label="Popular")
axs[2].scatter(non_popular["score"],non_popular["num_comments"],label="Not Popular")
axs[2].set_title("Score vs Comments")
axs[2].legend()

fig.suptitle("Trendspulse Dashboard")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All Charts saved sucessfully ")