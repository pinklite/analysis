import os
import pandas as pd

dirpath = os.getcwd()

credits = pd.read_csv(dirpath + '/csv/big/credits.csv')
movies = pd.read_csv(dirpath + '/csv/big/movies_metadata.csv')
links = pd.read_csv(dirpath + '/csv/big/links.csv')

# credits = pd.read_csv(dirpath + '/csv/small/practice_credits.csv')
# movies = pd.read_csv(dirpath + '/csv/small/practice_movies_metadata.csv')
# links = pd.read_csv(dirpath + '/csv/small/practice_links.csv')

def convert_to_imdb_id(credits_imdb_id):
	orig_length = len(credits_imdb_id)
	for i in range(orig_length, 7):
		credits_imdb_id = '0' + credits_imdb_id
	return 'tt' + credits_imdb_id

print(links.shape)
links = links[links.tmdb_id.notnull()]
links = links[links.imdb_id.notnull()]
links = links[links.lens_id.notnull()]
links['tmdb_id'] = links['tmdb_id'].astype(int)
print(links.shape)

print(credits.shape)
credits = credits[credits.cast.notnull()]
credits = credits[credits.crew.notnull()]
credits = credits[credits.tmdb_id.notnull()]
credits = credits[credits.tmdb_id.apply(lambda x: x.isnumeric())]
credits['tmdb_id'] = credits['tmdb_id'].astype(int)
print(credits.shape)

print(movies.shape)
movies = movies[movies.imdb_id.notnull()]
print(movies.shape)

print(credits.dtypes)
print(links.dtypes)

# credits_with_link = pd.merge(credits.drop(columns=["cast", "crew"]), links, on='tmdb_id')
credits_with_link = pd.merge(credits, links, on='tmdb_id')

print(credits_with_link.head(10))


credits_with_link['imdb_id'] = credits_with_link['imdb_id'].astype(str)
credits_with_link['imdb_id'] = credits_with_link['imdb_id'].apply(convert_to_imdb_id)


movies['imdb_id'] = movies['imdb_id'].astype(str)
merged = pd.merge(credits_with_link, movies.drop(columns=['lens_id', 'original_title', 'production_countries']), on='imdb_id')

print(credits_with_link.sort_values('imdb_id').head(10))
# trying to figure out the 'nan' column values in the movies['imdb_id']
print(movies.drop(columns=['lens_id', 'original_title', 'production_countries']).sort_values('imdb_id').head(10))

print(merged.head(10))