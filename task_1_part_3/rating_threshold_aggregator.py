import json
import pandas as pd

# Load restaurant data from given JSON file, faced error initially without utf-8 encoding
with open('../data_files/restaurant_data.json', encoding='utf-8') as file:
    restaurant_data = json.load(file)

# Extract rating text and aggregate rating, then filter by rating text
ratings = []
for restaurant_info in restaurant_data:
    for restaurant in restaurant_info['restaurants']:
        restaurant_details = restaurant['restaurant']
        rating_text = restaurant_details['user_rating']['rating_text']
        aggregate_rating = float(restaurant_details['user_rating']['aggregate_rating'])
        
        if rating_text in ['Excellent', 'Very Good', 'Good', 'Average', 'Poor']:
            ratings.append([rating_text, aggregate_rating])

ratings_df = pd.DataFrame(ratings, columns=['Rating Text', 'Aggregate Rating'])

# Group by 'Rating Text' and find the min and max aggregate rating for each group
rating_thresholds = ratings_df.groupby('Rating Text')['Aggregate Rating'].agg(['min', 'max']).reset_index()
rating_thresholds.to_csv('rating_thresholds.csv', index=False)
