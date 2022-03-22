import json

# Insert own path to NLP json file
with open('nlp-output.json') as json_file:
    data = json.load(json_file)

# Manually set total number of ads
TOTAL_ADS = 3

# Dictionaries for each element
dict_ads = dict()
dict_cntry_orig = dict()
dict_cntry_dest = dict()
dict_ad_id = dict()
dict_title = dict()
dict_industry = dict()
dict_country = dict()
dict_risk_score = dict()


# Put each element into seperate dictionary
x = 0
while x < TOTAL_ADS:
    dict_ads[x] = data['ads'][x]
    dict_ad_id[x] = dict_ads[x]['ad_id']
    dict_title[x] = dict_ads[x]['title']
    dict_industry[x] = dict_ads[x]['industry']
    dict_cntry_dest[x] = dict_ads[x]['country']['dest_country']
    dict_cntry_orig[x] = dict_ads[x]['country']['orig_country']
    dict_risk_score[x] = dict_ads[x]['risk_score']
    x += 1


# Print each dictionary
print(dict_ad_id)
print(dict_title)
print(dict_industry)
print(dict_cntry_dest)
print(dict_cntry_orig)
print(dict_risk_score)
