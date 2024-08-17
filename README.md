# DHT22 Monitor

This repository contains the necessary files to set up a DHT22 temperature monitor using InfluxDB and Docker Compose as the server, and a Python script (`DHT22.py`) running on a Raspberry Pi device to send the temperature data to the server.

## Prerequisites

Before setting up the DHT22 monitor, make sure you have the following installed:

- Docker
- Docker Compose
- Python

## Installation

1. Clone this repository to your Raspberry Pi device.
2. Navigate to the cloned repository directory.
3. Run the following command to start the InfluxDB server:

    ```
    docker-compose up -d
    ```

4. Connect the DHT22 sensor to your Raspberry Pi device.
5. Run the `DHT22.py` script to start sending temperature data to the server.

## Usage

Once the installation is complete, the DHT22 monitor will continuously send temperature data to the InfluxDB server. You can access the data using the InfluxDB client or any other compatible tools.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
