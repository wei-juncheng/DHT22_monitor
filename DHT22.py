import logging

import adafruit_dht
import board
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)
token = "mytoken"
org = "myorg"
url = (
    "http://<YOUR_INFLUXDB_IP>:<YOUR_INFLUXDB_PORT>"  # e.g. http://140.@@@.@@@.@@@:8086
)

write_client = InfluxDBClient(url=url, token=token, org=org)
bucket = "temperatures"

write_api = write_client.write_api(write_options=SYNCHRONOUS)


def get_cpu_temperature() -> float:
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temp = float(file.read()) / 1000.0
    return temp


temperature_c = dhtDevice.temperature
humidity = dhtDevice.humidity
logger.info("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))


point = (
    Point("temperature")
    .tag("temperature", "C")
    .tag("device", "DHT22")
    .field("temperature", temperature_c)
    .field("humidity", humidity)
    .field("cpu_temp", get_cpu_temperature())
)
logger.info(f"point: {point}")
write_api.write(bucket=bucket, org=org, record=point)
