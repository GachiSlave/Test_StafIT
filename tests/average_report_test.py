import sys

sys.path.append(".")
sys.path.append("../")
from main import average_report
import pytest


@pytest.mark.parametrize(
    "group_column, filenames, report_type, expected",
    [
        (
            "country",
            ["./tests/economic_test.csv"],
            "average-gdp",
            {
                "country": ["Spain", "Mexico", "Indonesia"],
                "gdp": [1409.3333333333333, 1382.0, 1319.0],
            },
        ),
        (
            "country",
            ["./tests/economic_one_line.csv"],
            "average-gdp",
            {"country": ["Japan"], "gdp": [4230.0]},
        ),
        (
            "country",
            ["./tests/economic_test.csv", "./tests/economic_one_line.csv"],
            "average-gdp",
            {
                "country": ["Japan", "Spain", "Mexico", "Indonesia"],
                "gdp": [4230.0, 1409.3333333333333, 1382.0, 1319.0],
            },
        ),
        (
            "continent",
            ["./tests/economic_test.csv"],
            "average-gdp_growth",
            {
                "continent": ["Asia", "Europe", "North America"],
                "gdp_growth": [5.0, 4.766666666666667, 4.45],
            },
        ),
    ],
)
def test_average_report(group_column, filenames, report_type, expected):
    assert average_report(group_column, filenames, report_type) == expected
