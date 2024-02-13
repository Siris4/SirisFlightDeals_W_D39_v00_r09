# Given list of parameters as strings, we want to extract only the keys and format them as requested

keys_str = """
"fly_from": "SAN",
"fly_to": "FRA",
"date_from": "02/13/2024",
"date_to": "08/13/2024",
"return_from": "04/04/2021",
"nights_in_dst_from": 7,
"nights_in_dst_to": 28,
"max_fly_duration": 20,
"ret_from_diff_city": "true",
"ret_to_diff_city": "true",
"one_for_city": 0,
"one_per_date": 0,
"adults": 1,
"children": 0,
"infants": 0,
"selected_cabins": "C",
"mix_with_cabins": "M",
"adult_hold_bag": "1,0",
"adult_hand_bag": "1,1",
"child_hold_bag": "0,0",
"child_hand_bag": "0,0",
"only_working_days": "false",
"only_weekends": "false",
"partner_market": "us",
"price_from": 0,
"price_to": 550,
"max_stopovers": 2,
"max_sector_stopovers": 2,
"vehicle_type": "aircraft",
"sort": "price",
"limit": 1
"""

# Extracting keys from the string
keys_list = [line.split(":")[0].strip().replace('"', '') for line in keys_str.split("\n") if line]

# Joining extracted keys with a comma
formatted_keys = ", ".join(keys_list)

formatted_keys