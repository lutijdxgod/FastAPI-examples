
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote


# models.Base.metadata.create_all(bind=engine)
# don't need this line anymore, since we now use alembic
# to automatically perfrom database edits

app = FastAPI()

origins = ["https://www.google.com"] # ["*"] for public api
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credetials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


