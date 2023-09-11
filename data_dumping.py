import pymongo
import pandas as pd
from json import loads as jl

client = pymongo.MongoClient('mongodb://localhost:27017')

PATH = 'C:/Users/PRAMOD/OneDrive/Desktop/ML/aps-fault-detection/Data.csv'
DATABASE_NAME = 'APS'
COLLECTION_NAME = 'sensors'

if __name__ == '__main__':
    df = pd.read_csv(PATH)
    df.reset_index(drop=True, inplace=True)

    json_rec = list(jl(df.T.to_json()).values())

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_rec)
