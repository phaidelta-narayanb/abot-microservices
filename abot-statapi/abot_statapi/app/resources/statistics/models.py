from enum import Enum
from typing import Any

from pydantic import BaseModel


class DataIn(BaseModel):
    # Pandas DataFrame parameters
    data: list[dict[str, Any]]
    index: list[Any] | None
    columns: list[str] | None

    # Other optional settings
    index_column_names: str | list[str] | None
    datetime_column_names: str | list[str] | None


class AggregationMethod(str, Enum):
    RECENT = "recent"
    AVERAGE = "average"
    MINIMUM = "minimum"
    MAXIMUM = "maximum"
    STDDEV = "stddev"
    COUNT = "count"
    COMPLIANCE = "compliance"
    QUANTILE = "quantile"
    MEDIAN = "median"
    SUMMARY = "summary"


class AggregationIn(DataIn, BaseModel):
    method: AggregationMethod | list[AggregationMethod] = AggregationMethod.RECENT
    aggregation_column: str | None = None
    aggregation_options: dict[str, Any] | None = None


AggregationOut = dict[AggregationMethod, float | int]


class OutliersIn(DataIn, BaseModel):
    outliers_column: str | None
