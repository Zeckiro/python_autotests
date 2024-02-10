import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_by_level():
    """
    KIT-1. Get trainers by level
    """
    response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=3)
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_by_id():
    """
    KIT-2. Get trainers by id
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 5000}, timeout=3)
    assert response.status_code == 200, 'Unexpected status code'