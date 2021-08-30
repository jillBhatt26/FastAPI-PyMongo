import uvicorn

if __name__ == '__main__':
    uvicorn.run("API:app", host = 'localhost', port = 5000, reload = True )