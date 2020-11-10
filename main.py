from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def example():
    return {"FastAPI": "The fastest modern web framework!"}


@app.get("/greetings")
def greeting():
    return {"Hello to my new REST API!"}


@app.get("/names")
def greeting():
    return {"name1": "Bek", "name2": "George", "name3": "Samuel"}


if __name__ == "__main__":
    uvicorn.run("main:app")
