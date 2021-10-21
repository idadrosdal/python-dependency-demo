from app import get_cat_fact


def test_cat_fact():
    assert get_cat_fact() == ""
