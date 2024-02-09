from fastapi import FastAPI
from planner.routers.user import user_router

import uvicorn

app = FastAPI()
app.include_router(user_router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
