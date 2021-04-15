import json
import requests
# total
# Active cases = confirmed - (recovered+deceased+others
#"confirmed":5247,"deceased":63,"recovered":5078,"tested":339482
response = requests.get('https://api.covid19india.org/v4/min/data.min.json')
data = response.json()
print("state\t\tActive cases")
print("-------------------------")
for state in data.keys():
    print(state, end="\t\t")
    total_cases = data[state]['total']
    deceased = total_cases['deceased'] if "deceased" in total_cases.keys() else 0
    recovered = total_cases['recovered'] if "recovered" in total_cases.keys() else 0
    others = total_cases['other'] if "others" in total_cases.keys() else 0
    active_cases = total_cases['confirmed'] - (deceased+recovered+others)
    print(active_cases)