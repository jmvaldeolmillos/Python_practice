import pytest
import numpy as np
from unittest.mock import patch
from my_project import main
import requests


# Test fetching data from a valid URL
@patch("my_project.main.requests.get")
def test_fetch_data_success(mock_get):
    # Mocking the response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"userId": 1}, {"userId": 2}, {"userId": 3}]

    url = "https://jsonplaceholder.typicode.com/posts"
    data = main.fetch_data(url)

    assert data == [{"userId": 1}, {"userId": 2}, {"userId": 3}]
    assert isinstance(data, list) # Should be a list!


# Test fetching data from an invalid URL or failed request
@patch("my_project.main.requests.get")
def test_fetch_data_failure(mock_get):
    # Mocking a failed response
    mock_get.return_value.status_code = 404
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()

    url = "https://jsonplaceholder.typicode.com/invalid"
    data = main.fetch_data(url)

    assert data is None


# Test numpy operations with sample data
def test_numpy_operations():
    user_ids = [1, 2, 3, 4, 5]
    user_ids_array = np.array(user_ids)

    mean_user_id = np.mean(user_ids_array)
    std_dev_user_id = np.std(user_ids_array)

    assert mean_user_id == 3.0
    assert np.isclose(std_dev_user_id, 1.414213562, atol=1e-8)


# Additional test for empty data
def test_numpy_operations_empty_data():
    user_ids = []
    user_ids_array = np.array(user_ids)

    mean_user_id = np.mean(user_ids_array) if len(user_ids_array) > 0 else None
    std_dev_user_id = np.std(user_ids_array) if len(user_ids_array) > 0 else None

    assert mean_user_id is None
    assert std_dev_user_id is None
