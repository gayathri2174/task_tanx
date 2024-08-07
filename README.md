# Customer Orders Analysis

## Overview

This project analyzes customer orders from an online store to compute:

- Total revenue generated by the online store for each month.
- Total revenue generated by each product.
- Total revenue generated by each customer.
- Top 10 customers by revenue generated.

## Project Structure

### Directories and Files

- **app/**: Contains the main application logic.
  - `main.py`: Reads the dataset, computes revenues, and identifies top customers.
- **tests/**: Contains unit tests.
  - `test_main.py`: Tests the functions in `main.py`.
- **Dockerfile**: Builds the Docker image for the application.
- **Dockerfile.test**: Builds the Docker image for running tests.
- **docker-compose.yml**: Defines services for the application and tests.
- **requirements.txt**: Lists Python dependencies.
- **orders.csv**: Dataset containing customer orders.

### `app/main.py`

- **read_data(file_path)**: Reads the CSV file located at `file_path` into a pandas DataFrame.
- **compute_monthly_revenue(df)**: Computes the total revenue for each month from the DataFrame.
- **compute_product_revenue(df)**: Computes the total revenue for each product from the DataFrame.
- **compute_customer_revenue(df)**: Computes the total revenue generated by each customer from the DataFrame.
- **top_customers_by_revenue(customer_revenue, top_n=10)**: Returns the top N customers based on their total revenue.
- **main()**: Main function to read data, compute revenue metrics, and print results.

### `tests/test_main.py`

- Contains unit tests for functions in `app/main.py`:
  - **test_compute_monthly_revenue**: Verifies the monthly revenue calculation.
  - **test_compute_product_revenue**: Verifies the revenue calculation by product.
  - **test_compute_customer_revenue**: Verifies the revenue calculation by customer.
  - **test_top_customers_by_revenue**: Verifies the identification of top customers by revenue.

### Docker Configuration

- **Dockerfile**: Defines the base image, working directory, copies the project files, installs dependencies, and sets the command to run the application.
- **Dockerfile.test**: Similar to Dockerfile but sets the command to run the tests.
- **docker-compose.yml**: Defines two services:
  - **app**: Builds from Dockerfile and runs the application.
  - **test**: Builds from Dockerfile.test and runs the tests.

### `requirements.txt`

- Lists the Python dependencies needed for the project. In this case, it includes:
  - `pandas`

### `data.csv`

- The dataset containing customer orders used for analysis.

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/gayathri2174/task_tanx
   ```

## Building the Docker Images

1. **Build the Docker images:**

   ```sh
   docker-compose build
   ```

   This command will build the Docker images for both the `app` and `test` services defined in the `docker-compose.yml` file.

## Running the Application

1. **Run the application container:**

   ```sh
   docker-compose run app
   ```

   This command will run the application, and you should see the output from `main.py`, such as the monthly revenue, product revenue, customer revenue, and top customers.

2. **Run the test:**

   ```sh
   docker-compose run test
   ```

   This will execute the test and print the test results to the console.
