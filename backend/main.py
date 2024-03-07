import uvicorn


if __name__ == "__main__":
                 #nomearquivo#nomeAppMain   
    uvicorn.run("app.FastAPI:app", host="127.0.0.1", port=8002, reload=True)