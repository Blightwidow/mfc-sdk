import pytest


def test_login():
    """Test the login method of MyFlyClubClient."""
    from mfc.client.myflyclub import mfc_client

    response = mfc_client.login()
    assert isinstance(response, str)
    assert response  # Check if the response is not empty
    assert "cf_clearance" in mfc_client.session.cookies  # Check if the cookie is set
    assert mfc_client.session.cookies[
        "cf_clearance"
    ]  # Check if the cookie is not empty
    assert (
        mfc_client.session.cookies["cf_clearance"] == response
    )  # Check if the cookie value matches the response


def test_get():
    """Test the get method of MyFlyClubClient."""
    from mfc.client.myflyclub import mfc_client

    response = mfc_client.get("/colors")
    assert isinstance(response, dict)
    assert bool(response)  # Check if the response is not empty


def test_get_invalid_path():
    """Test the get method of MyFlyClubClient with an invalid path."""
    from mfc.client.myflyclub import mfc_client

    with pytest.raises(ValueError):
        mfc_client.get("invalid_path")  # Path must start with a leading slash
