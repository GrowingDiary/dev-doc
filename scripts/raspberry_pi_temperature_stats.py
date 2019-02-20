import copy
import time
import influxdb
from datetime import datetime


INFLUXDB_HOST = ''
INFLUXDB_PORT = 8086
INFLUXDB_USER = ''
INFLUXDB_PASS = ''
INFLUXDB_NAME = ''


TEMP_REPORT = {
    'measurement': 'pi_temperature',
    'tags': {},
    'time': '',
    'fields': {}
}


def get_cpu_temperature():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temperature = float(f.read()) / 1000
        return temperature


def main():
    db_client = influxdb.InfluxDBClient(host=INFLUXDB_HOST,
                                        port=INFLUXDB_PORT,
                                        username=INFLUXDB_USER,
                                        password=INFLUXDB_PASS,
                                        database=INFLUXDB_NAME)

    while True:
        request_body = []
        report_point = copy.deepcopy(TEMP_REPORT)
        report_point['time'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        report_point['fields']['value'] = get_cpu_temperature()
        report_point['tags']['type'] = 'cpu'
        request_body.append(report_point)
        db_client.write_points(request_body)

        time.sleep(30)

    db_client.close()


if __name__ == '__main__':
    main()
