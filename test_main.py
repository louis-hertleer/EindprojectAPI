import requests
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def test_create_worker():
    worker_data = {
        'email': 'Example@gmail.com',
        'password': 'admin'
    }
    response = requests.post('http://127.0.0.1:8000/workers/', json=worker_data)
    assert response.status_code == 200
    created_worker = response.json()
    assert 'id' in created_worker
    assert created_worker['email'] == worker_data['email']
    assert 'password' not in created_worker  # Ensure password is not exposed in the response


# Second test
def test_login_for_access_token():
    response = requests.post(
        'http://127.0.0.1:8000/token',
        data={'username': 'Example@gmail.com', 'password': 'admin'}
    )
    assert response.status_code == 200
    response_dict = response.json()
    assert 'access_token' in response_dict
    assert 'token_type' in response_dict
    assert response_dict['token_type'] == 'bearer'


# Third test
def test_read_workers():
    headers = {'Authorization': 'Bearer your_access_token'}
    response = requests.get('http://127.0.0.1:8000/workers/', headers=headers)
    assert response.status_code == 200
    workers = response.json()
    assert isinstance(workers, list)


# Fourth test
def test_read_worker():
    headers = {'Authorization': 'Bearer your_access_token'}
    response = requests.get('http://127.0.0.1:8000/workers/1', headers=headers)
    assert response.status_code == 200
    worker = response.json()
    assert 'id' in worker
    assert 'email' in worker


# Fifth test
def test_create_tractor_for_worker():
    headers = {'Authorization': 'Bearer your_access_token'}
    tractor_data = {'type': 'TractorType', 'year': '2023', 'worker_id': '1'}
    response = requests.post('http://127.0.0.1:8000/workers/2/tractors/', json=tractor_data, headers=headers)
    assert response.status_code == 200
    tractor = response.json()
    assert 'id' in tractor
    assert tractor['type'] == tractor_data['type']
    assert tractor['year'] == tractor_data['year']


# Sixth test
def test_read_tractors():
    headers = {'Authorization': 'Bearer your_access_token'}
    response = requests.get('http://127.0.0.1:8000/tractors/', headers=headers)
    assert response.status_code == 200
    tractors = response.json()
    assert isinstance(tractors, list)


# Seventh test
def test_create_location_for_worker():
    headers = {'Authorization': 'Bearer your_access_token'}
    location_data = {'type': 'Barn', 'address': 'Kleinhoefstraat', 'worker_id': '1'}
    response = requests.post('http://127.0.0.1:8000/workers/2/locations/', json=location_data, headers=headers)
    assert response.status_code == 200
    location = response.json()
    assert 'id' in location
    assert location['type'] == location_data['type']
    assert location['address'] == location_data['address']


# Eighth test
def test_read_locations():
    headers = {'Authorization': 'Bearer your_access_token'}
    response = requests.get('http://127.0.0.1:8000/locations/', headers=headers)
    assert response.status_code == 200
    locations = response.json()
    assert isinstance(locations, list)


# Ninth test
def test_delete_tractor():
    headers = {'Authorization': 'Bearer your_access_token'}
    response = requests.delete('http://127.0.0.1:8000/tractors/1', headers=headers)
    assert response.status_code == 200
    deleted_tractor = response.json()
    assert 'id' in deleted_tractor

def test_update_worker_location():
    # Mock data for the update request
    updated_location_data = {
        "type": "Headquarters",
        "address": "Kleinhoefstraat 4",
    }

    # Mock worker and location IDs
    worker_id = 1
    location_id = 1

    # Mock access token
    access_token = "your_valid_access_token"

    # Make the PUT request
    response = requests.put(
        f'http://127.0.0.1:8000/workers/{worker_id}/locations/{location_id}',
        json=updated_location_data,
        headers={'Authorization': f'Bearer {access_token}'}
    )

    # Check if the request was successful (status code 200)
    assert response.status_code == 200

    # Check if the response body matches the expected updated location data
    updated_location = response.json()
    assert updated_location['type'] == updated_location_data['type']
    assert updated_location['address'] == updated_location_data['address']
