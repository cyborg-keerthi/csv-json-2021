
import csv
import json
import pandas as pd

read1=pd.read_csv('customer_data_one.csv')

read2=pd.read_csv('customer_data_two.csv')

#merging two csv files into one csv file
data=pd.concat([read1,read2])
data.to_csv('output.csv')

#converting csv file into json file
def csv_to_json(csvfilepath,jsonfilepath):
    jsonarray={}

    with open(csvfilepath,encoding='utf=8')as csvf:
        read1=csv.DictReader(csvf)

        for row in read1:
            key = row['mobile_number'] # using primary key as mobile_number
            jsonarray[key] = row

    with open(jsonfilepath,'w',encoding='utf-8')as jsonf:
        json_out=json.dumps(jsonarray, indent=4,sort_keys=True) #sorting the data
        jsonf.write(json_out)

csvfilepath=r'output.csv'
jsonfilepath=r'data.json'
csv_to_json(csvfilepath,jsonfilepath)



