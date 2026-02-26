import sys

sys.path.append(".")
sys.path.append("../")
from main import average
import pytest


@pytest.mark.parametrize(
    "group_by_dataframe, group_column, column, expected",
    [
        (
            {
                "Spain": {
                    "year": ["2023", "2022", "2021"],
                    "gdp": ["1394", "1409", "1425"],
                    "gdp_growth": ["2.4", "5.5", "6.4"],
                    "inflation": ["3.2", "8.4", "3.0"],
                    "unemployment": ["11.8", "13.0", "14.8"],
                    "population": ["48", "48", "47"],
                    "continent": ["Europe", "Europe", "Europe"],
                },
                "Mexico": {
                    "year": ["2023", "2021"],
                    "gdp": ["1490", "1274"],
                    "gdp_growth": ["3.2", "5.7"],
                    "inflation": ["4.7", "5.7"],
                    "unemployment": ["2.9", "4.1"],
                    "population": ["128", "126"],
                    "continent": ["North America", "North America"],
                },
                "Indonesia": {
                    "year": ["2023"],
                    "gdp": ["1319"],
                    "gdp_growth": ["5.0"],
                    "inflation": ["3.0"],
                    "unemployment": ["5.3"],
                    "population": ["278"],
                    "continent": ["Asia"],
                },
            },
            "country",
            "gdp",
            {
                "country": ["Spain", "Mexico", "Indonesia"],
                "gdp": [1409.3333333333333, 1382.0, 1319.0],
            },
        ),
        (
            {
                "Asia": {
                    "country": ["Japan"],
                    "year": ["2023"],
                    "gdp": ["4230"],
                    "gdp_growth": ["1.9"],
                    "inflation": ["3.2"],
                    "unemployment": ["2.4"],
                    "population": ["125"],
                }
            },
            "continent",
            "inflation",
            {"continent": ["Asia"], "inflation": [3.2]},
        ),
        (
            {
                "2023": {
                    "country": ["Spain", "Mexico", "Indonesia"],
                    "gdp": ["1394", "1490", "1319"],
                    "gdp_growth": ["2.4", "3.2", "5.0"],
                    "inflation": ["3.2", "4.7", "3.0"],
                    "unemployment": ["11.8", "2.9", "5.3"],
                    "population": ["48", "128", "278"],
                    "continent": ["Europe", "North America", "Asia"],
                },
                "2022": {
                    "country": ["Spain"],
                    "gdp": ["1409"],
                    "gdp_growth": ["5.5"],
                    "inflation": ["8.4"],
                    "unemployment": ["13.0"],
                    "population": ["48"],
                    "continent": ["Europe"],
                },
                "2021": {
                    "country": ["Spain", "Mexico"],
                    "gdp": ["1425", "1274"],
                    "gdp_growth": ["6.4", "5.7"],
                    "inflation": ["3.0", "5.7"],
                    "unemployment": ["14.8", "4.1"],
                    "population": ["47", "126"],
                    "continent": ["Europe", "North America"],
                },
            },
            "year",
            "unemployment",
            {
                "year": ["2023", "2022", "2021"],
                "unemployment": [6.666666666666667, 13.0, 9.45],
            },
        ),
    ],
)
def test_average(group_by_dataframe, group_column, column, expected):
    assert (
        average(
            group_by_dataframe=group_by_dataframe,
            group_column=group_column,
            column=column,
        )
        == expected
    )
