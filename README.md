# get-table

A FastAPI server that provides table information with CORS enabled.

## Features

- FastAPI web server with CORS support for all origins
- Returns table names and descriptions in JSON format
- Preset table data (no database required)

## API Endpoints

### GET /tables

Returns a list of available tables with their descriptions.

**Response format:**
```json
{
  "status": "success",
  "tables": [
    {
      "table_name": "users",
      "description": "User account information and profiles"
    },
    {
      "table_name": "inventory", 
      "description": null
    }
  ]
}
```

### GET /

Returns basic API information.

## Setup and Usage

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python main.py
```

The server will start on `http://localhost:8000`

3. Test the API:
```bash
curl http://localhost:8000/tables
```

## Testing

Run the test suite:
```bash
python test_api.py
```

## CORS Configuration

The server is configured to allow requests from all origins (`*`) with full CORS support including:
- All HTTP methods
- All headers
- Credentials support