import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('NetflixProject/netflix_titles.csv')

# print(df.head())


df = df.dropna(subset=['type', 'title','rating','release_year', 'duration', 'country'])


type_counts = df['type'].value_counts()

plt.figure(figsize=(6,4))

plt.bar(type_counts.index, type_counts.values, color=('skyblue', 'yellow'))

plt.title('No. of movies vs TV Shows on Netflix')

plt.xlabel('Type')

plt.ylabel('Count')

plt.tight_layout()

plt.savefig('NetflixProject/movies_vs_tvshows.png')

plt.show()

rating_counts = df['rating'].value_counts()

plt.figure(figsize=(8,6))


plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%',startangle=90)

plt.title('Percentage of content by rating on netflix')

plt.tight_layout()

plt.savefig('NetflixProject/content_by_rating.png')

plt.show()


movie_df = df[df['type']=='Movie'].copy()

movie_df['duration'] = movie_df['duration'].str.replace('min', '').astype(int)

plt.figure(figsize=(8,6))

plt.hist(movie_df['duration'],bins=45,color='purple', edgecolor='black')

plt.title('Distribution of Movie Durations on Netflix')


plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.savefig('NetflixProject/movie_durations_histogram.png')


plt.show()


release_counts = df['release_year'].value_counts().sort_index()

plt.figure(figsize=(12,6))

plt.scatter(release_counts.index, release_counts.values, color='red')

plt.title("Number of titles released each year on netflix")

plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
# plt.grid(True)
plt.tight_layout()
plt.savefig('NetflixProject/titles_released_per_year.png')  
plt.show()


country_counts = df['country'].value_counts().head(10)

plt.figure(figsize=(8,6))

plt.barh(country_counts.index,country_counts.values, color='green')

plt.title('Top 10 Countries by Number of Titles on Netflix')

plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('NetflixProject/top_10_countries.png')
plt.show()

content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2, figsize=(12,5))
#  subplot - movies

ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')


ax[0].set_title('Movies Released Over the Years')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('Number of Movies')

# subplot - tv shows

ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title('TV Shows Released Over the Years')
ax[1].set_xlabel('Release Year')

ax[1].set_ylabel('Number of TV Shows')
plt.tight_layout()
fig.suptitle('Movies vs TV Shows Released Over the Years on Netflix')
plt.savefig('NetflixProject/movies_tvshows_over_years.png')
plt.show()


