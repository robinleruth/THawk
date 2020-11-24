from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(title='Market Data API',
              description='',
              version='0.1')

from .controllers import fundamentals_controller

api.include_router(fundamentals_controller.router,
                   prefix='/api/v1/fundamentals',
                   tags=['fundamentals'])

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
