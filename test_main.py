from unittest.mock import patch, MagicMock
from requests.exceptions import ConnectionError, InvalidURL
from main import is_host_alive

def test_host_is_down_on_connection_error():
    with patch('main.requests.get', side_effect=ConnectionError):
        assert is_host_alive('google.com') == False

def test_host_is_up_on_200():
    mock_response = MagicMock()
    mock_response.status_code = 200
    with patch('main.requests.get', return_value=mock_response):
        assert is_host_alive('google.com') == True

def test_host_is_down_on_500():
    mock_response = MagicMock()
    mock_response.status_code = 500
    with patch('main.requests.get', return_value=mock_response):
        assert is_host_alive('google.com') == False