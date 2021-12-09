import pytest
import datetime


def make_year_marker(year):
    return f"y{year}"


def make_day_marker(day):
    return f"d{day}"


def pytest_configure(config):
    for year in range(2015, datetime.date.today().year + 1):
        config.addinivalue_line("markers", make_year_marker(year))
    for day in range(1, 26):
        config.addinivalue_line("markers", make_day_marker(day))


def pytest_collection_modifyitems(items):
    for item in items:
        if hasattr(item, "callspec"):
            year, day, _ = item.callspec.id.split("_")
            item.add_marker(getattr(pytest.mark, make_year_marker(year)))
            item.add_marker(getattr(pytest.mark, make_day_marker(day)))
