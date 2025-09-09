import json
import requests

def test_tables_endpoint():
    """Test the /tables endpoint returns correct JSON format."""
    try:
        response = requests.get("http://localhost:8000/tables")
        assert response.status_code == 200
        
        data = response.json()
        
        # Check required fields in response
        assert "status" in data
        assert "tables" in data
        assert isinstance(data["status"], str)
        assert isinstance(data["tables"], list)
        
        # Check table format
        for table in data["tables"]:
            assert "table_name" in table
            assert "description" in table
            assert isinstance(table["table_name"], str)
            # description can be string or None (null in JSON)
            assert table["description"] is None or isinstance(table["description"], str)
        
        print("✅ All tests passed!")
        print(f"Status: {data['status']}")
        print(f"Number of tables: {len(data['tables'])}")
        print("Tables:")
        for table in data["tables"]:
            print(f"  - {table['table_name']}: {table['description']}")
        
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_cors_headers():
    """Test CORS headers are present."""
    try:
        # Test with regular GET request to see CORS headers
        response = requests.get("http://localhost:8000/tables", 
                               headers={"Origin": "http://test.com"})
        assert "access-control-allow-origin" in response.headers
        print("✅ CORS test passed!")
        print(f"CORS Origin: {response.headers.get('access-control-allow-origin')}")
        return True
    except Exception as e:
        print(f"❌ CORS test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing FastAPI server...")
    test_tables_endpoint()
    test_cors_headers()