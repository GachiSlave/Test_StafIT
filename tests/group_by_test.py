import sys

sys.path.append(".")
sys.path.append("../")
from main import group_by
import pytest


@pytest.mark.parametrize(
    "dataframe, group_column, expected",
    [
        (
            {
                "index": [0, 1, 2, 3, 4, 5],
                "country": ["Spain", "Spain", "Spain", "Mexico", "Mexico", "Indonesia"],
                "year": ["2023", "2022", "2021", "2023", "2021", "2023"],
                "gdp": ["1394", "1409", "1425", "1490", "1274", "1319"],
                "gdp_growth": ["2.4", "5.5", "6.4", "3.2", "5.7", "5.0"],
                "inflation": ["3.2", "8.4", "3.0", "4.7", "5.7", "3.0"],
                "unemployment": ["11.8", "13.0", "14.8", "2.9", "4.1", "5.3"],
                "population": ["48", "48", "47", "128", "126", "278"],
                "continent": [
                    "Europe",
                    "Europe",
                    "Europe",
                    "North America",
                    "North America",
                    "Asia",
                ],
            },
            "country",
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
        ),
        (
            {
                "index": [0, 1, 2, 3, 4, 5],
                "country": ["Spain", "Spain", "Spain", "Mexico", "Mexico", "Indonesia"],
                "year": ["2023", "2022", "2021", "2023", "2021", "2023"],
                "gdp": ["1394", "1409", "1425", "1490", "1274", "1319"],
                "gdp_growth": ["2.4", "5.5", "6.4", "3.2", "5.7", "5.0"],
                "inflation": ["3.2", "8.4", "3.0", "4.7", "5.7", "3.0"],
                "unemployment": ["11.8", "13.0", "14.8", "2.9", "4.1", "5.3"],
                "population": ["48", "48", "47", "128", "126", "278"],
                "continent": [
                    "Europe",
                    "Europe",
                    "Europe",
                    "North America",
                    "North America",
                    "Asia",
                ],
            },
            "year",
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
        ),
        (
            {
                "index": [0],
                "country": ["Japan"],
                "year": ["2023"],
                "gdp": ["4230"],
                "gdp_growth": ["1.9"],
                "inflation": ["3.2"],
                "unemployment": ["2.4"],
                "population": ["125"],
                "continent": ["Asia"],
            },
            "continent",
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
        ),
    ],
)
def test_group_by(dataframe, group_column, expected):
    assert group_by(dataframe=dataframe, group_column=group_column) == expected
