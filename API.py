# FAST API Imports
from fastapi import FastAPI, HTTPException, status

# Classes imports
from classes.Finace import CreateFinance, UpdateFinance


# Database imports
from database.Mongo import collection

# MongoDB imports
from bson import ObjectId
from pymongo import ReturnDocument
from bson.json_util import loads, dumps

# Functions imports
from functions.ParseDocument import ParseDocument



# Fast Api app init
app = FastAPI()

# Endpoints

# GET: Fetch all finances
@app.get('/')
def get_finances_all():
    finances = []

    try:
        docs = collection.find({})

        for doc in docs:
            jsonDoc = ParseDocument(doc)

            finances.append(jsonDoc)

        response = {
            'success': True,
            'data': finances
        }

        return response

    except Exception as e:
        # return { 'success': False, 'error' : e }
        raise HTTPException(status_code = status.HTTP_500, detail = f'Error occurred fetching documents: {e}')



# GET: Fetch a finance detail using the mongoDB ObjectId
@app.get('/{fin_id}')
def fetch_task_by_id(fin_id: str):
    try:
        doc = collection.find_one({ '_id': ObjectId(fin_id) })

        jsonDoc = ParseDocument(doc)

        return { 'success': True, 'data': jsonDoc }
    except Exception as e:
        return { 'success' : False, 'error' : e }



# POST: Create a new finance detail
@app.post('/')
def create_finance(finance: CreateFinance):
    try:
        collection.insert_one({ 
            'title': finance.title, 
            'amount': int(finance.amount), 
            'description': finance.description,
            'category': finance.category,
            'isDue': finance.isDue
        })

        return { 'success': True }
    except Exception as e:
        return { 'success' : False, 'error': e }



# PUT: Update an existing finance detail
@app.put('/{fin_id}')
def update_finance(fin_id: str, finance: UpdateFinance):
    try:
        updated = collection.find_one_and_update(
            {
                '_id': ObjectId(fin_id)
            },
            {
                '$set': {
                    'title': finance.title,
                    'amount': int(finance.amount),
                    'description': finance.description,
                    'category': finance.category,
                    'isDue': finance.isDue
                }
            },
            return_document = ReturnDocument.AFTER
        )

        if updated:
            return { 'success': True, 'updated': updated }
        else:
            return { 'success' : False }
    except Exception as e:
        return { 'success': False, 'error': e }



@app.delete('/{fin_id}')
def delete_finance(fin_id: str):
    try:
        deleted = ParseDocument(collection.find_one_and_delete({ '_id': ObjectId(fin_id) }))

        if deleted:
            return { 'success': True, 'deleted': deleted}
        else:
            return { 'success' : False }
    except Exception as e:
        return { 'success': False, 'error': e }