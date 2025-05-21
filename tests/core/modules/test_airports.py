def test_airport_all():
    """Test the all method of the Airport module."""
    from mfc.core.modules.airports import Airport, all

    airports = all()
    assert isinstance(airports, list)
    assert len(airports) > 0  # Check if the list is not empty
    for airport in airports:
        assert isinstance(airport, Airport)
        assert airport.id > 0  # Check if the airport ID is positive
        assert airport.name  # Check if the airport name is not empty
        assert airport.latitude != 0.0  # Check if the latitude is not zero
        assert airport.longitude != 0.0  # Check if the longitude is not zero


def test_airport_get_by_id():
    """Test the get_by_id method of the Airport module."""
    from mfc.core.modules.airports import Airport, all, id

    airports = all()
    airport = id(airports[0].id)
    assert isinstance(
        airport, Airport
    )  # Check if the returned object is an Airport instance
    non_existent_airport = id(0)  # Assuming this ID does not exist
    assert (
        non_existent_airport is None
    )  # Check if None is returned for non-existent airport
