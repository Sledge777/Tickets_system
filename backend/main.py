import uvicorn

from fastapi import FastAPI

from handlers import router as api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app)