from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge, webhooks
import os

from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=[os.getenv("FRONTEND_URL")],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


app.include_router(challenge.router,prefix="/api")
app.include_router(webhooks.router,prefix="/webhooks")