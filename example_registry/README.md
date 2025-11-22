# Function Call Registry

A FastAPI-based function call registry system that provides a centralized catalog of available functions across multiple service categories.

## Features

- **Comprehensive Function Registry**: 43 functions across 17 categories
- **Executable APIs**: Each function exposed as a REST API endpoint
- **RESTful API**: Clean FastAPI endpoints for querying functions
- **Categories**: Google, Salesforce, Slack, GitHub, Notion, AWS, Stripe, and more
- **Search & Filter**: Find functions by name, description, category, or required credentials

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --host 0.0.0.0 --port 9999 --reload
```

The API will be available at `http://localhost:9999`

## API Endpoints

### Function Execution

**All 43 functions are exposed as executable API endpoints!**

```
POST /function/{function_name}/execute
```

Execute any function by posting its parameters as JSON:

```bash
curl -X POST "http://localhost:9999/function/google_sheets_append/execute" \
  -H "Content-Type: application/json" \
  -d '{
    "parameters": {
      "sheet_id": "abc123",
      "range": "Sheet1!A1",
      "values": [["Name", "Email"]]
    }
  }'
```

Response:
```json
{
  "function_name": "google_sheets_append",
  "result": "",
  "success": true,
  "error": null
}
```

See [API_USAGE.md](API_USAGE.md) for detailed examples of all 43 functions!

### Registry Endpoints

#### 1. List All Functions
```
GET /function/list
```
Returns all available functions in the registry.

#### 2. Get Function by Name
```
GET /function/{function_name}
```
Get details of a specific function.

Example: `GET /function/google_sheets_append`

#### 3. Get Functions by Category
```
GET /function/category/{category}
```
Get all functions in a specific category.

Example: `GET /function/category/google`

#### 4. Get All Categories
```
GET /function/categories
```
Returns a list of all available categories.

#### 5. Search Functions
```
GET /function/search?q={query}&category={category}&credential={credential}
```
Search functions by name or description with optional filters.

Examples:
- `GET /function/search?q=email`
- `GET /function/search?q=create&category=google`
- `GET /function/search?q=upload&credential=aws`

## Available Categories

- `google` - Google Workspace services (Sheets, Gmail, Groups)
- `salesforce` - Salesforce CRM operations
- `slack` - Slack messaging and channel management
- `github` - GitHub repository operations
- `email` - Email services (Mailchimp)
- `storage` - Cloud storage operations
- `database` - Database operations (PostgreSQL)
- `http` - Generic HTTP requests
- `notification` - Webhook notifications
- `notion` - Notion workspace operations
- `aws` - Amazon Web Services (S3, Lambda, DynamoDB)
- `airtable` - Airtable database operations
- `web` - Web scraping and automation
- `payment` - Payment processing (Stripe)
- `communication` - SMS and voice (Twilio)
- `ai` - AI services (OpenAI)
- `support` - Support ticketing (Zendesk)

## Project Structure

```
example_registry/
├── main.py              # FastAPI application
├── models.py            # Pydantic models
├── registry.py          # Function registry definitions
├── requirements.txt     # Python dependencies
├── test_functions.py    # Test script for functions
├── functions/           # Function implementations
│   ├── __init__.py      # Exports all functions
│   ├── google_services.py
│   ├── salesforce.py
│   ├── slack.py
│   ├── github.py
│   ├── email.py
│   ├── storage.py
│   ├── database.py
│   ├── http.py
│   ├── notion.py
│   ├── aws.py
│   ├── airtable.py
│   ├── web.py
│   ├── payment.py
│   ├── communication.py
│   ├── ai.py
│   └── support.py
└── README.md           # This file
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Usage

### Execute Functions via API

```python
import requests

BASE_URL = "http://localhost:9999"

def call_function(function_name, **parameters):
    """Helper to call any function"""
    response = requests.post(
        f"{BASE_URL}/function/{function_name}/execute",
        json={"parameters": parameters}
    )
    return response.json()

# Example 1: Append to Google Sheets
result = call_function(
    "google_sheets_append",
    sheet_id="abc123",
    range="Sheet1!A1",
    values=[["Name", "Email"], ["John", "john@example.com"]]
)
print(result)
# {'function_name': 'google_sheets_append', 'result': '', 'success': True, 'error': None}

# Example 2: Send Slack message
result = call_function(
    "slack_send_message",
    channel_id="C123456",
    text="Hello from the API!"
)
print(result)

# Example 3: Create GitHub PR
result = call_function(
    "github_create_pr",
    owner="myorg",
    repo="myrepo",
    title="New Feature",
    head="feature-branch",
    base="main",
    body="Description"
)
print(result)

# Example 4: OpenAI Chat
result = call_function(
    "openai_chat_completion",
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(result)
```

### Query the Registry

```python
# List all functions
response = requests.get(f"{BASE_URL}/function/list")
functions = response.json()

# Get a specific function
response = requests.get(f"{BASE_URL}/function/google_sheets_append")
function = response.json()

# Search for functions
response = requests.get(f"{BASE_URL}/function/search?q=email")
results = response.json()

# Get functions by category
response = requests.get(f"{BASE_URL}/function/category/google")
google_functions = response.json()

# Get all categories
response = requests.get(f"{BASE_URL}/function/categories")
categories = response.json()
```

## Function Implementations

All 60+ functions are now implemented as callable Python functions in the `functions/` directory. Currently, each function returns an empty string as a placeholder. You can now implement the actual logic for each function.

### Using Functions Directly

```python
from functions import google_sheets_append, slack_send_message

# Call functions directly
result = google_sheets_append(
    sheet_id="abc123",
    range="Sheet1!A1",
    values=[["Name", "Email"], ["John", "john@example.com"]]
)

# Or use the function map
from functions import FUNCTION_MAP

func = FUNCTION_MAP.get("slack_send_message")
result = func(channel_id="C123", text="Hello, World!")
```

### Testing Functions

Run the test script to verify all functions are importable:

```bash
python test_functions.py
```

## Next Steps

To implement real functionality:

1. Replace the `return ""` in each function with actual implementation
2. Add authentication/credential management
3. Implement actual service integrations (Google API, Slack SDK, etc.)
4. Add rate limiting and API key management
5. Implement logging and monitoring
6. Add database persistence for function execution history
7. Add proper error handling and validation

