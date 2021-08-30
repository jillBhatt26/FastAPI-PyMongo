# PyMongo Imports
from pymongo import MongoClient

# MongoDB Config
cluster = MongoClient('mongodb://localhost:27017')
database = cluster['py-fin-track']
collection = database['finances']