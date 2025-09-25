from fastapi import Depends

from .services import DataStatisticsService
from .models import AggregationIn, AggregationOut, OutliersIn


async def data_aggregation(
    agg_data: AggregationIn,
    stat_serv: DataStatisticsService = Depends(),
) -> AggregationOut:
    return await stat_serv.aggregation(agg_data)


async def data_outliers(
    agg_data: OutliersIn,
    stat_serv: DataStatisticsService = Depends(),
):
    return await stat_serv.outliers(agg_data)
