import json
with open('data.txt') as json_data:
    d = json.load(json_data)
    print(max(d['mean_reward']), max(d['saving_time']))
    print(d['score'])
