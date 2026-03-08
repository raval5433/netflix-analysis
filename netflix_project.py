import pandas as pd
import matplotlib.pyplot as plt


# Load Dataset

df = pd.read_csv("netflix_titles.csv")


df['country'] = df['country'].fillna("Unknown")
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Unknown")

results = []


# DATA ANALYSIS TASKS 


# 1 Total titles
results.append(["1 Total Titles", len(df)])

# 2 Movies vs TV Shows
results.append(["2 Type Distribution", df['type'].value_counts().to_dict()])

# 3 Unique countries
results.append(["3 Unique Countries", df['country'].nunique()])

# 4 Top 5 countries with most content
results.append(["4 Top Countries", df['country'].value_counts().head(5).to_dict()])

# 5 Most common rating
results.append(["5 Rating Distribution", df['rating'].value_counts().to_dict()])

# 6 Most common genres
results.append(["6 Top Genres", df['listed_in'].value_counts().head(5).to_dict()])

# 7 Titles released after 2018
results.append(["7 Titles after 2018", len(df[df['release_year'] > 2018])])

# 8 Titles before 2000
results.append(["8 Titles before 2000", len(df[df['release_year'] < 2000])])

# 9 Average release year
results.append(["9 Average Release Year", df['release_year'].mean()])

# 10 Movies count
results.append(["10 Total Movies", len(df[df['type']=="Movie"])])

# 11 TV Shows count
results.append(["11 Total TV Shows", len(df[df['type']=="TV Show"])])

# 12 Content added in 2020
results.append(["12 Content added in 2020", len(df[df['date_added'].astype(str).str.contains("2020")])])

# 13 Content added in 2021
results.append(["13 Content added in 2021", len(df[df['date_added'].astype(str).str.contains("2021")])])

# 14 Longest duration movie
movie_df = df[df['type']=="Movie"]
results.append(["14 Longest Movie Duration", movie_df['duration'].value_counts().head(1).to_dict()])

# 15 Shortest duration movie
results.append(["15 Shortest Movie Duration", movie_df['duration'].value_counts().tail(1).to_dict()])

# 16 Top 5 directors
results.append(["16 Top Directors", df['director'].value_counts().head(5).to_dict()])

# 17 Top 5 actors
results.append(["17 Top Actors", df['cast'].value_counts().head(5).to_dict()])

# 18 Titles per year
results.append(["18 Titles per Year", df['release_year'].value_counts().head(10).to_dict()])

# 19 Missing values
results.append(["19 Missing Values", df.isnull().sum().to_dict()])

# 20 Duplicate rows
results.append(["20 Duplicate Rows", df.duplicated().sum()])

# 21 Content from India
results.append(["21 Titles from India", len(df[df['country'].str.contains("India")])])

# 22 Content from United States
results.append(["22 Titles from USA", len(df[df['country'].str.contains("United States")])])


# Save CSV Output


output_df = pd.DataFrame(results, columns=["Task","Result"])
output_df.to_csv("netflix_analysis_output.csv", index=False)

print("Analysis CSV created")



type_counts = df['type'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(type_counts,
        labels=type_counts.index,
        autopct='%1.1f%%')

plt.title("Netflix Content Type Distribution")
plt.savefig("type_pie_chart.png")
plt.show()



rating_counts = df['rating'].value_counts().head(5)

plt.figure(figsize=(7,7))
plt.pie(rating_counts,
        labels=rating_counts.index,
        autopct='%1.1f%%')

plt.title("Top 5 Ratings Distribution")
plt.savefig("rating_pie_chart.png")
plt.show()



country_counts = df['country'].value_counts().head(5)

plt.figure(figsize=(7,7))
plt.pie(country_counts,
        labels=country_counts.index,
        autopct='%1.1f%%')

plt.title("Top Countries Content Distribution")
plt.savefig("country_pie_chart.png")
plt.show()

print("Pie charts created")