import os
import pandas as pd

dirpath = os.getcwd()

credits = pd.read_csv(dirpath + '/csv/credits.csv')
movies = pd.read_csv(dirpath + '/csv/movies_metadata.csv')
links = pd.read_csv(dirpath + '/csv/links.csv')

# credits = pd.read_csv(dirpath + '/csv/practice_credits.csv')
# movies = pd.read_csv(dirpath + '/csv/practice_movies_metadata.csv')
# links = pd.read_csv(dirpath + '/csv/practice_links.csv')

def convert_to_imdb_id(credits_imdb_id):
	orig_length = len(credits_imdb_id)
	for i in range(orig_length, 7):
		credits_imdb_id = '0' + credits_imdb_id
	return 'tt' + credits_imdb_id

# credits_with_link = pd.merge(credits.drop(columns=["cast", "crew"]), links, on='tmdb_id')
# credits_with_link['imdb_id'] = credits_with_link['imdb_id'].astype(str)
# credits_with_link['imdb_id'] = credits_with_link['imdb_id'].apply(convert_to_imdb_id)
# print(credits_with_link.head(10))

# movies['imdb_id'] = movies['imdb_id'].astype(str)
# print(movies.head(10))
# merged = pd.merge(credits_with_link, movies.drop(columns=['lens_id']), on='imdb_id')

# # merged = credits.drop(columns=["cast", "crew"]).join(links, on='tmdb_id')#.set_index('imdb_id').join(movies.set_index('imdb_id'), on='imdb_id')
# print(merged.head(10))
# print(merged.dtypes)


# # merged.to_csv(path_or_buf = dirpath + '/csv/merged.csv', encoding='utf-8', index=True)

credits_with_link = pd.merge(credits, links, on='tmdb_id')
movies['imdb_id'] = movies['imdb_id'].astype(str)
credits_with_link['imdb_id'] = credits_with_link['imdb_id'].astype(str)
credits_with_link['imdb_id'] = credits_with_link['imdb_id'].apply(convert_to_imdb_id)
merged = pd.merge(credits_with_link, movies.drop(columns=['lens_id', 'original_title', 'production_countries']), on='imdb_id')

print(credits_with_link.head(10))

# print(merged.head(10))
# print(links.head(10))