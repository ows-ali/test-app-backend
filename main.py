
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Allow CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the dataset
try:
    data = pd.read_excel("TestData.xlsx")
except Exception as e:
    raise HTTPException(status_code=500, detail="Error loading dataset")

@app.get("/data")
async def get_data():
    print('sdf',data)
    return data.to_dict(orient="records")


