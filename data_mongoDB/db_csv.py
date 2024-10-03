import csv, os
from pymongo import MongoClient
def get_database():
    CONNECTION_STRING = "mongodb+srv://xxx"

    client = MongoClient(CONNECTION_STRING)

    return client['景點']

dbname = get_database()


files = os.listdir('景點')
    
for file in files:

    name = file.replace('_景點.csv', '')
    print(name)
    collection = dbname[name]

    file_path = f"景點/{file}"
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        headers = next(csv_reader)
        headers[0] = headers[0].lstrip('\ufeff')
        

        for row in csv_reader:
            item = {}
            for i in range(len(row)):
                item[headers[i]] = row[i]
            # print(item)
            result = collection.insert_one(item)
            print("Inserted item with ID:", result.inserted_id)