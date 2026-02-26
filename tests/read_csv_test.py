import sys

sys.path.append(".")
sys.path.append("../")
from main import read_csv
import pytest


@pytest.mark.parametrize(
    "dataframe, filename, expected",
    [
        (
            {},
            "./tests/economic_test.csv",
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
        ),
        ({}, "./tests/economic_empty.csv", {"index": []}),
        (
            {},
            "./tests/economic_one_line.csv",
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
            "./tests/economic_test.csv",
            {
                "index": [0, 1, 2, 3, 4, 5, 6],
                "country": [
                    "Japan",
                    "Spain",
                    "Spain",
                    "Spain",
                    "Mexico",
                    "Mexico",
                    "Indonesia",
                ],
                "year": ["2023", "2023", "2022", "2021", "2023", "2021", "2023"],
                "gdp": ["4230", "1394", "1409", "1425", "1490", "1274", "1319"],
                "gdp_growth": ["1.9", "2.4", "5.5", "6.4", "3.2", "5.7", "5.0"],
                "inflation": ["3.2", "3.2", "8.4", "3.0", "4.7", "5.7", "3.0"],
                "unemployment": ["2.4", "11.8", "13.0", "14.8", "2.9", "4.1", "5.3"],
                "population": ["125", "48", "48", "47", "128", "126", "278"],
                "continent": [
                    "Asia",
                    "Europe",
                    "Europe",
                    "Europe",
                    "North America",
                    "North America",
                    "Asia",
                ],
            },
        ),
    ],
)
def test_read_csv(dataframe, filename, expected):
    assert read_csv(dataframe=dataframe, filename=filename) == expected
