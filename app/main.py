import uvicorn
from fastapi import FastAPI

from app.routers import user

app = FastAPI()
app.include_router(user.router)

@app.get("/")
async def root():
    return "Welcome to SkeletonAPI"

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)