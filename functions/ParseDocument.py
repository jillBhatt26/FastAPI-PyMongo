def ParseDocument(doc):
    doc_id =  str(doc['_id'])
    del doc['_id']
    doc['_id'] = doc_id

    return doc