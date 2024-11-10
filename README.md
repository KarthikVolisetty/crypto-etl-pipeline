Here's a README file for your **Cryptocurrency ETL Pipeline with Airflow** project. This file outlines the project overview, requirements, setup instructions, and the project structure. You can add or modify sections as needed.

---

# Cryptocurrency ETL Pipeline with Airflow

This project is an ETL (Extract, Transform, Load) pipeline designed to fetch cryptocurrency data from the CoinGecko API, transform it into a structured format, and load it into a PostgreSQL database. The ETL process is orchestrated by Apache Airflow, allowing for easy scheduling and monitoring of the data pipeline.

## Project Overview

The ETL pipeline has three main stages:
1. **Extract**: Fetches the current price of Bitcoin in USD from the CoinGecko API.
2. **Transform**: Converts the raw API data into a pandas DataFrame, with columns suitable for database insertion.
3. **Load**: Inserts the transformed data into a PostgreSQL database.

The pipeline is scheduled and managed by an Airflow DAG, which can be run daily or at a desired interval to keep the data up-to-date.

## Project Structure

The project directory is structured as follows:

```
project_directory/
├── dags/
│   └── crypto_etl_dag.py    # Airflow DAG for scheduling
├── scripts/
│   ├── fetch_data.py        # Data extraction script
│   ├── transform_data.py    # Data transformation script
│   └── load_data.py         # Data loading script
├── logs/                    # Folder for Airflow logs
└── plugins/                 # Folder for any Airflow plugins (empty for now)
```

## Requirements

- **Python 3.6+**
- **Apache Airflow**
- **Docker**
- **PostgreSQL**
- **psycopg2** and **pandas** Python packages

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/crypto-etl-pipeline.git
cd crypto-etl-pipeline
```

### 2. Set Up the Python Environment

Install the required Python libraries:

```bash
pip install pandas psycopg2 requests
```

### 3. Set Up PostgreSQL

Make sure PostgreSQL is running, and create a new database called `cryptodata`. Adjust database credentials in `load_data.py` to match your setup:

```sql
CREATE DATABASE cryptodata;
```

### 4. Configure Airflow

1. **Initialize Airflow**: Set up and initialize Airflow.
   ```bash
   airflow db init
   ```

2. **Add the DAG**: Place the `crypto_etl_dag.py` file in the Airflow `dags` directory.

3. **Start Airflow**: Launch the Airflow web server and scheduler.
   ```bash
   airflow scheduler & airflow webserver
   ```

4. **Access Airflow UI**: Open the Airflow web UI at [http://localhost:8080](http://localhost:8080), log in, and activate the `crypto_etl_pipeline` DAG to start running it.

### 5. Verify Data in PostgreSQL

After running the DAG, connect to PostgreSQL to verify that the data has been loaded successfully:

```bash
psql -U youruser -d cryptodata -c "SELECT * FROM prices;"
```

## Project Files

- **`fetch_data.py`**: Fetches the latest Bitcoin price data from CoinGecko API.
- **`transform_data.py`**: Transforms the raw JSON data into a structured DataFrame.
- **`load_data.py`**: Loads the transformed data into the `prices` table in PostgreSQL.
- **`crypto_etl_dag.py`**: Airflow DAG to orchestrate the ETL pipeline, with tasks for extraction, transformation, and loading.

## Testing Each Component

You can test each script individually to ensure they work as expected:

- **Extract**:
  ```bash
  python3 scripts/fetch_data.py
  ```
- **Transform**:
  ```bash
  python3 -c "from scripts.transform_data import transform_data; transform_data({'bitcoin': {'usd': 30000}})"
  ```
- **Load**:
  ```bash
  python3 -c "import pandas as pd; from scripts.load_data import load_data; df = pd.DataFrame({'cryptocurrency': ['bitcoin'], 'price_usd': [30000.0]}); load_data(df)"
  ```

## Future Improvements

- Add more cryptocurrencies to fetch data for a wider range of assets.
- Schedule the DAG to run at a desired interval for continuous data ingestion.
- Integrate data visualization tools to analyze historical cryptocurrency trends.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [CoinGecko API](https://www.coingecko.com/en/api) for cryptocurrency data.
- [Apache Airflow](https://airflow.apache.org/) for workflow orchestration.

--- 

This README should help others understand, set up, and run your ETL pipeline project on GitHub. Let me know if you'd like further details added!
