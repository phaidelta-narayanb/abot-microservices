import unittest

from abot_statapi import init_app
from fastapi.testclient import TestClient


class TestStatisticsAggregation(unittest.TestCase):
    client = TestClient(init_app())
    ENDPOINT = "/statistics/aggregation"
    MOCK_DATA1 = [{"y": 10}, {"y": 20}, {"y": 30}]

    def test_average(self):
        mock_data = self.MOCK_DATA1

        response = self.client.post(
            self.ENDPOINT,
            json={
                "df": {
                    "data": mock_data,
                },
                "method": "average",
                "aggregation_column": "y",
            },
        )

        result = response.json()
        self.assertDictEqual(result, {"average": 20})

    def test_max(self):
        mock_data = self.MOCK_DATA1

        response = self.client.post(
            self.ENDPOINT,
            json={
                "df": {
                    "data": mock_data,
                },
                "method": "maximum",
                "aggregation_column": "y",
            },
        )

        result = response.json()
        self.assertDictEqual(result, {"maximum": 30})

    def test_average_max_count(self):
        mock_data = self.MOCK_DATA1

        response = self.client.post(
            self.ENDPOINT,
            json={
                "df": {
                    "data": mock_data,
                },
                "method": ["average", "maximum", "count"],
                "aggregation_column": "y",
            },
        )

        result = response.json()
        self.assertDictEqual(result, {"average": 20, "maximum": 30, "count": 3})
