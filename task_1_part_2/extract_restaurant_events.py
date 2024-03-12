import json
import pandas as pd

# Load restaurant data from given JSON file, faced error initially without utf-8 encoding
with open('../data_files/restaurant_data.json', encoding='utf-8') as file:
    restaurant_data = json.load(file)

# Extract all relevant restaurant fields, then extract
restaurant_events = []
for restaurant_info in restaurant_data:
    for restaurant in restaurant_info['restaurants']:
        restaurant_summary = restaurant['restaurant']
        events = restaurant_summary.get('zomato_events', [])

        for event in events:
                restaurant_id = restaurant_summary['R']['res_id']
                restaurant_name = restaurant_summary['name']
                event_summary = event['event']
                event_id = event_summary['event_id']
                photo_url = event_summary['photos'][0]['photo']['url'] if event_summary['photos'] else "NA"
                event_title = event_summary.get('title', "NA")
                start_date = event_summary['start_date']
                end_date = event_summary['end_date']
                
                # Check if the event is in April 2019
                if '2019-04' in start_date or '2019-04' in end_date:
                    restaurant_events.append([
                        event_id, restaurant_id, restaurant_name, photo_url, event_title, start_date, end_date
                    ])

# Convert to DataFrame and save to CSV
restaurant_events_df = pd.DataFrame(restaurant_events, columns=['Event Id', 'Restaurant Id', 'Restaurant Name', 'Photo URL', 'Event Title', 'Event Start Date', 'Event End Date'])
restaurant_events_df.to_csv('restaurant_events.csv', index=False)
