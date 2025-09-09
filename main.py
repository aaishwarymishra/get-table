from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for all origins and endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TableInfo(BaseModel):
    table_name: str
    description: Optional[str] = None

class TablesResponse(BaseModel):
    status: str
    tables: List[TableInfo]

@app.get("/tables", response_model=TablesResponse)
def get_tables():
    # Dummy table data
    tables = [
        TableInfo(table_name="users", description="User accounts table"),
        TableInfo(table_name="orders", description=None),
        TableInfo(table_name="products", description="Product catalog"),
    ]
    return TablesResponse(status="success", tables=tables)
