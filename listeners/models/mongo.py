import json
import pymongo

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

# config = {}
# with open('./config.json') as config_file:
# 	config = json.load(config_file)

url = "mongodb+srv://yogeshbhakli:4f27NeSt02fIZUFl@cluster0.nsri0sp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
	
client = pymongo.MongoClient(url)

# database connection
db = pymongo.database.Database(client, 'test')
