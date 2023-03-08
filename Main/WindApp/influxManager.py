from influxdb_client import InfluxDBClient
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS


def getDataByTime(bucket, url, token, organization):
    bucket = bucket

    client = InfluxDBClient(url=url,
                            token=token,
                            org=organization)

    query_api = client.query_api()

    tables = query_api.query('from(bucket:"wind") |> range(start: -1h)')

    values = []

    for table in tables:
        for row in table.records:
            values.append(row.values['_value'])

    return values
