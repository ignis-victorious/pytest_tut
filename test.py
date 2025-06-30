#  _______________
#  Import LIBRARIES
# import pytest
from unittest.mock import Mock

from pytest_mock import MockerFixture
from requests import Response
from requests.exceptions import RequestException

#  Import FILES
from main import make_get_request

#  _______________

"""Tests for the get-request code."""
# For mock we dont want to have to rely on dependencies, plus we can t


def test_valid_response(mocker: MockerFixture) -> None:
    mock_response: Mock = mocker.Mock()
    mock_response.json.return_value = {"headers": {"tst": 123}}
    mocker.patch("main.rq.get", return_value=mock_response)

    result: Response | dict[str, str] = make_get_request(url="validurl")
    assert result == {"tst": 123}
    # assert result == {}


# You should import RequestException directly from requests.exceptions and use it in your test instead of accessing it as an attribute of the requests module.
def test_invalid_response(mocker: MockerFixture) -> None:
    mocker.patch("main.rq.get", side_effect=RequestException)
    # mocker.patch("main.rq.get", side_effect=rq.exceptions.RequestException)
    # mocker.patch("main.rq.get", side_effect=ValueError)

    result: Response | dict[str, str] = make_get_request(url="invalidurl")
    assert result == {"Error": "oh no!"}
