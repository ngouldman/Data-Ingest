from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name="mort"):
    return f'hello {name}'