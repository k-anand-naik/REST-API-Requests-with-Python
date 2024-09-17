import requests
import json
from typing import Any, Dict, Optional, List, Union

# Base API Endpoint
api_endpoint = 'https://jsonplaceholder.typicode.com/todos'

# 1. GET Request (Retrieve data)
def get_todos() -> Union[List[Dict[str, Any]], None]:
    """Fetches the first 5 'todos' and returns them, or None in case of error."""
    try:
        response: requests.Response = requests.get(api_endpoint)
        response.raise_for_status()  # Check for HTTP errors
        todos: List[Dict[str, Any]] = response.json()[0:5]
        return todos
    except requests.exceptions.RequestException as e:
        print(f"Error fetching todos: {str(e)}")
        return None

# 2. POST Request (Create new data)
def create_todo() -> Optional[Dict[str, Any]]:
    """Creates a new 'todo' and returns the created todo or None in case of error."""
    new_todo: Dict[str, Any] = {
        "userId": 1111,
        "id": 5555,
        "title": "Have to study hard",
        "completed": False
    }
    try:
        response: requests.Response = requests.post(api_endpoint, json=new_todo)
        response.raise_for_status()  # Check for HTTP errors
        created_todo: Dict[str, Any] = response.json()
        return created_todo
    except requests.exceptions.RequestException as e:
        print(f"Error creating todo: {str(e)}")
        return None

# 3. PUT Request (Update data entirely)
def update_todo_put(id: int) -> Optional[Dict[str, Any]]:
    """Updates the entire 'todo' and returns the updated todo or None in case of error."""
    api_endpoint_put: str = api_endpoint + f'/{str(id)}'
    todo_to_update: Dict[str, Any] = {
        "userId": 1,
        "title": "Study hard",
        "completed": False
    }
    try:
        response: requests.Response = requests.put(api_endpoint_put, json=todo_to_update)
        response.raise_for_status()  # Check for HTTP errors
        updated_todo: Dict[str, Any] = response.json()
        return updated_todo
    except requests.exceptions.RequestException as e:
        print(f"Error updating todo: {str(e)}")
        return None

# 4. PATCH Request (Update data partially)
def update_todo_patch(id: int) -> Optional[Dict[str, Any]]:
    """Partially updates the 'todo' and returns the updated todo or None in case of error."""
    api_endpoint_patch: str = api_endpoint + f'/{str(id)}'
    todo_to_update: Dict[str, Any] = {
        "title": "Study hard",
        "completed": True
    }
    try:
        response: requests.Response = requests.patch(api_endpoint_patch, json=todo_to_update)
        response.raise_for_status()  # Check for HTTP errors
        patched_todo: Dict[str, Any] = response.json()
        return patched_todo
    except requests.exceptions.RequestException as e:
        print(f"Error patching todo: {str(e)}")
        return None

# 5. DELETE Request (Delete data)
def delete_todo(id: int) -> Optional[int]:
    """Deletes the specified 'todo' and returns the status code or None in case of error."""
    api_endpoint_delete: str = api_endpoint + f'/{str(id)}'
    try:
        response: requests.Response = requests.delete(api_endpoint_delete)
        response.raise_for_status()  # Check for HTTP errors
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error deleting todo: {str(e)}")
        return None


# Execute all requests and return results

todos = get_todos()  # Perform GET
if todos:
    print("GET Request - Todos:", json.dumps(todos, indent=4))

created_todo = create_todo()  # Perform POST
if created_todo:
    print("POST Request - Created Todo:", json.dumps(created_todo, indent=4))

updated_todo = update_todo_put(10)  # Perform PUT
if updated_todo:
    print("PUT Request - Updated Todo:", json.dumps(updated_todo, indent=4))

patched_todo = update_todo_patch(10)  # Perform PATCH
if patched_todo:
    print("PATCH Request - Patched Todo:", json.dumps(patched_todo, indent=4))

deleted_status = delete_todo(10)  # Perform DELETE
if deleted_status:
    print(f"DELETE Request - Status Code: {deleted_status}")