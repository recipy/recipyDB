from pymongo import MongoClient
import os
import datetime

#Start mongoDB client
client = MongoClient()

#Access database named 'test_database'
db = client.test_database

#Create runs collection
recipies = db.recipies

#Create run objects to be stored in collection
authors = {"Janneke": "jvdzwaan", "Robin": "robintw", "Raquel": "raquel-ucl"}
for filename in os.listdir('.'):
    for author in authors:
        run = {"author": author,
            "title": filename,
            "filename": "path_to_image",
            "inputs": ["path_to_input1", "path_to_input2", "path_to_input3"],
            "outputs": ["path_to_output1"],
            "script": "path_to_script",
            "environment": ["python3.2", "PyMongo2.8", "MAC OS 10.10.02"],
            "command": "script -f flag",
            "gitrepo": ["git://otherhost.org/user/repo.git"],
            "gituser": "raquel-ucl",
            "gitrepo": "git://otherhost.org/user/repo.git",
            "gitcommit": "c72a071351e5b48e70f2515dce309671c4103586",
            "gituser": authors[author],
            "date": datetime.datetime.utcnow()}
        #Insert image metadata in DB
        run_id = recipies.insert(run)



