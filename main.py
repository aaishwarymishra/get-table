from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Union

app = FastAPI(title="Table Service API", description="API to get table information")

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Preset table data
PRESET_TABLES = [
    {
        "table_name": "users",
        "description": "User account information and profiles"
    },
    {
        "table_name": "products",
        "description": "Product catalog and inventory data"
    },
    {
        "table_name": "orders",
        "description": "Customer orders and transaction records"
    },
    {
        "table_name": "categories",
        "description": "Product categories and classification"
    },
    {
        "table_name": "inventory",
        "description": None
    }
]

@app.get("/tables")
async def get_tables() -> Dict[str, Union[str, List[Dict[str, Union[str, None]]]]]:
    """
    Get list of available tables with their descriptions.
    
    Returns:
        Dict containing status and list of tables
    """
    return {
        "status": "success",
        "tables": PRESET_TABLES
    }

@app.get("/")
async def root():
    """Root endpoint with basic API information."""
    return {
        "message": "Table Service API",
        "description": "Use /tables endpoint to get table information"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)