import json
from pprint import pprint
import unicodecsv

with open('opportunities22.json') as data_file:
    dataf=json.load(data_file)



super_list=[]

for i in dataf["data"]:
    sub_list=[]
    sub_list.append(i["location"])
    sub_list.append(i["branch"]["name"])
    sub_list.append(i["title"])
    sub_list.append(i["earliest_start_date"])
    sub_list.append(i["latest_end_date"])
    sub_list.append(i["duration_min"])
    try:
        sub_list.append(i["branch"]["organisation"]["contact_info"]["email"])
    except:
        sub_list.append("None")
    super_list.append(sub_list)




with open("europe.csv", "a") as f:
    writer = unicodecsv.writer(f,dialect='excel',encoding='utf-8')
    writer.writerows(super_list)







