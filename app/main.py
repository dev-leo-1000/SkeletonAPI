import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.db.database import Database
from app.routers import user, item


def init_app():
    """
    API 초기화
    :return:
    """
    app = FastAPI()

    # 라우터
    app.include_router(user.router)
    app.include_router(item.router)

    # 미들웨어
    # SOP 방지용 미들웨어
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )

    # # db 연결 및 초기화
    # Database()

    return app

app = init_app()
@app.get("/")
async def root():
    return "Welcome to SkeletonAPI"

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)



