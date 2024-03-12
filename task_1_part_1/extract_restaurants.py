import json
import pandas as pd

# Load restaurant data from given JSON file, faced error initially without utf-8 encoding
with open('../data_files/restaurant_data.json', encoding='utf-8') as file:
    restaurant_data = json.load(file)

# Load country codes from given Excel file
country_codes = pd.read_excel('../data_files/Country-Code.xlsx')

# Create a dictionary to reference country names from country codes
country_code_dict = country_codes.set_index('Country Code')['Country'].to_dict()

# Extract the relevant fields according to the data format in JSON file
restaurants = []
for restaurant_info in restaurant_data:
    for restaurant in restaurant_info['restaurants']:
        restaurant_summary = restaurant['restaurant']
        restaurant_id = restaurant_summary['R']['res_id']
        restaurant_name = restaurant_summary['name']
        city = restaurant_summary['location']['city']
        country_id = restaurant_summary['location']['country_id']
        country = country_code_dict.get(country_id, 'Unknown')
        user_rating_votes = restaurant_summary['user_rating']['votes']
        user_aggregate_rating = float(restaurant_summary['user_rating']['aggregate_rating'])
        cuisines = restaurant_summary['cuisines']

        restaurants.append([
            restaurant_id, restaurant_name, country, city, user_rating_votes, user_aggregate_rating, cuisines
        ])

# Convert to pandas DataFrame and save to CSV
restaurants_df = pd.DataFrame(restaurants, columns=['Restaurant Id', 'Restaurant Name', 'Country', 'City', 'User Rating Votes', 'User Aggregate Rating', 'Cuisines'])
restaurants_df.to_csv('restaurants.csv', index=False)
