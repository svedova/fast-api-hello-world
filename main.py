import os
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "Hello World"

@app.get("/json")
def read_json():
    return {"message": "Hello World"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)