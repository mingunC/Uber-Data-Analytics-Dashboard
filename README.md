# Uber-Data-Analytics-Dashboard

## Overview
The Uber Data Analytics Dashboard is a comprehensive tool for analyzing New York City taxi trip data. Built with Streamlit and powered by BigQuery, this dashboard provides real-time data analysis, SQL-based insights, and predictive analytics to derive actionable business intelligence from taxi trip patterns.


| Figure 1. DAG Graph View | Figure 2. DAG Gantt View |
|:--:|:--:|
| <img src="./images/dashboard_overview.png" alt="dashboard overview" width="400" /><br><em>dashboard overview</em> | <img src="./images/realtime_analysis.png" alt="realtime analysis" width="400" /><br><em>real-time analysis</em> |



## Features
### Advanced Data Analytics

Multi-source Data Integration: Connect to BigQuery, local CSV files, or use generated test data
Comprehensive Visualizations: Analyze trip patterns by time, distance, fare, and location
Geographic Analysis: Map pickup and dropoff locations with borough and zone breakdowns
SQL-Powered Insights: Run pre-built SQL queries for deeper data analysis

### Real-time Capabilities

Auto-refresh: Set the dashboard to update automatically every 5 minutes
Time Range Analysis: Filter data by specific time periods (1 hour, 24 hours, 7 days, 30 days)
Live Metrics: Monitor key performance indicators in real-time
Trend Analysis: Track hourly changes in trip volume, fare amounts, and revenue

### Interactive Filtering

Custom Date Ranges: Select specific date ranges for data analysis
Day and Time Filters: Filter by day of week and time of day
Advanced Filters: Analyze specific segments by applying multiple filters simultaneously
Dynamic Dashboard: See instant updates as filters are applied

### Machine Learning Models

Fare Prediction: Train linear regression models to predict taxi fares
Feature Importance: Identify key factors affecting fare prices
Interactive Predictions: Input trip parameters to get real-time fare estimates
Model Performance Metrics: View R² scores and other evaluation metrics

### Tech Stack

Frontend: Streamlit (Python-based web app framework)
Data Processing: Pandas, NumPy
Data Visualization: Plotly Express
Database: Google BigQuery
Cloud Services: Google Cloud Platform
Machine Learning: Scikit-learn
ETL Pipeline: Integration with Mage AI (optional)

## Project Structure
```text
Uber-Data-Analytics-Dashboard/
├── dashboard/
│   ├── app.py                 # Main Streamlit application
│   ├── prediction.py          # Fare prediction model
│   ├── data/
│   │   └── raw/               # Raw data files
│   └── queries/               # SQL query files
│       ├── daily_trips.sql    # Daily trip analysis query
│       └── hourly_stats.sql   # Hourly statistics query
├── mage_data/                 # Data processed by Mage AI
│   └── data/
│       └── processed/         # Processed data files
└── README.md                  # Project documentation
```
## Getting Started
### Prerequisites
Python 3.8+
Google Cloud account with BigQuery access
Service account key with appropriate permissions

## Installation
1. Clone the repository
git clone https://github.com/yourusername/Uber-Data-Analytics-Dashboard.git
cd Uber-Data-Analytics-Dashboard

2. Create and activate a virtual enviroment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Set up Google Cloud authentication:
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account-key.json"

5. Run the dashboard:
cd dashboard
streamlit run app.py

# Data Sources
The dashboard can connect to three different data sources:
- BigQuery: Connect to Google BigQuery for real-time data analysis
- Local CSV: Use local CSV files for offline analysis
- Test Data: Generate synthetic data for development and testing

## Usage Examples
Real-time Trip Analysis
1. Select "BigQuery" as the data source
2. Enable auto-refresh or click "Refresh Now"
3. Choose a time window (1 hour, 24 hours, 7 days, 30 days)
4. Analyze the real-time trip data visualizations

## SQL-Based Analysis
1. Navigate to the "SQL Analysis" tab
2. View pre-built SQL query results for daily trips and hourly statistics
3. Explore trends and patterns in the visualizations

## Fare Prediction
1. Navigate to the "Fare Prediction" section
2. Click "Train Prediction Model" to build a new model
3. Input trip parameters (distance, duration, passengers, etc.)
4. Click "Predict Fare" to get an estimated fare

# Additional Configuration
## SQL Query Customization
Create custom SQL queries by adding new .sql files to the queries directory:
```
-- example_query.sql
SELECT
  DATE(tpep_pickup_datetime) AS trip_date,
  COUNT(*) AS total_trips,
  AVG(fare_amount) AS avg_fare
FROM
  `your-project-id.uber_analytics.yellow_taxi_data`
GROUP BY
  trip_date
ORDER BY
  trip_date DESC
LIMIT 30;
```
Then add the query execution to the dashboard:
# Execute custom query
custom_df = execute_query("example_query")

# Display results
st.dataframe(custom_df)

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
### License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgements
- NYC Taxi & Limousine Commission for the dataset
- Google Cloud Platform for BigQuery services
- Streamlit for the web application framework
