import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *


root = Tk()
root.title("IMDb Movie Analytics Dashboard")



df = pd.read_csv("data/IMDB-Movie-Data.csv")

df = df.rename(columns={
    "Runtime (Minutes)": "Runtime",
    "Revenue (Millions)": "Revenue"
})


df["Revenue"] = df["Revenue"].fillna(df["Revenue"].median())
df["Metascore"] = df["Metascore"].fillna(df["Metascore"].mean())


top10_rated = df.sort_values("Rating", ascending=False).head(10)[["Title", "Rating","Director"]]
bottom10_rated = df.sort_values("Rating", ascending=True).head(10)[["Title", "Rating","Director"]]


Label(root, text="IMDb Movie Performance Summaries", font=("Arial", 16, "bold"), fg="darkblue").pack(pady=10)


main_frame = Frame(root)
main_frame.pack(fill="both", expand=True, padx=20, pady=10)


left_frame = LabelFrame(main_frame, text=" Top 10 Highest Rated ", font=("Arial", 11, "bold"), fg="green")
left_frame.pack(side="left", fill="both", expand=True, padx=10)

for index, row in top10_rated.iterrows():
    movie_str = f"⭐ {row['Rating']} | {row['Title']} | Directed by:{row["Director"]}"
    Label(left_frame, text=movie_str, font=("Arial", 10)).pack(anchor="w", padx=5, pady=2)


right_frame = LabelFrame(main_frame, text=" Bottom 10 Lowest Rated ", font=("Arial", 11, "bold"), fg="red")
right_frame.pack(side="right", fill="both", expand=True, padx=10)

for index, row in bottom10_rated.iterrows():
    movie_str = f"❌ {row['Rating']} | {row['Title']} | Directed by:{row["Director"]}"
    Label(right_frame, text=movie_str, font=("Arial", 10)).pack(anchor="w", padx=5, pady=2)




plt.figure(figsize=(8, 4))
year_counts = df["Year"].value_counts().sort_index()
year_counts.plot(kind='bar', color='royalblue', edgecolor='black')
plt.title('Number of Movie Releases per Year (2006-2016)', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Count of Movies')
plt.xticks(rotation=45)
plt.tight_layout()


plt.figure(figsize=(8, 4))
plt.barh(top10_rated['Title'], top10_rated['Rating'], color='gold', edgecolor='black')
plt.gca().invert_yaxis()  # Keeps the highest rated movie at the very top
plt.title('Top 10 Highest Rated Movies', fontweight='bold')
plt.xlabel('IMDb Rating')
plt.tight_layout()


plt.show()    
root.mainloop()