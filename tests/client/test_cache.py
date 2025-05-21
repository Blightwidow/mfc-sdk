def test_set_and_get():
    from mfc.client.cache import MyFlyClubCache

    cache = MyFlyClubCache()
    cache.set("validator1", "key1", "value1")
    assert cache.get("validator1", "key1") == "value1"


def test_get_with_invalid_validator():
    from mfc.client.cache import MyFlyClubCache

    cache = MyFlyClubCache()
    cache.set("validator1", "key1", "value1")
    assert cache.get("invalid_validator", "key1") is None


def test_get_with_nonexistent_key():
    from mfc.client.cache import MyFlyClubCache

    cache = MyFlyClubCache()
    assert cache.get("validator1", "nonexistent_key") is None


def test_clear_cache():
    from mfc.client.cache import MyFlyClubCache

    cache = MyFlyClubCache()
    cache.set("validator1", "key1", "value1")
    cache.clear()
    assert cache.get("validator1", "key1") is None
    assert len(cache.data) == 0
    assert len(cache.cache_validators) == 0


def test_overwrite_existing_key():
    from mfc.client.cache import MyFlyClubCache

    cache = MyFlyClubCache()
    cache.set("validator1", "key1", "value1")
    cache.set("validator2", "key1", "value2")
    assert cache.get("validator1", "key1") is None
    assert cache.get("validator2", "key1") == "value2"
