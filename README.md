## Overview

This project analyzes customer orders from an online store to compute:

- Total revenue generated by the online store for each month.
- Total revenue generated by each product.
- Total revenue generated by each customer.
- Top 10 customers by revenue generated.

- **app/**: Contains the main application logic.
  - `main.py`: Reads the dataset and computes revenues and top customers.
- **tests/**: Contains unit tests.
  - `testm.py`: Tests the functions in `main.py`.
- **Dockerfile**: Builds the Docker image for the application.
- **Dockerfile.test**: Builds the Docker image for running tests.
- **docker-compose.yml**: Defines services for the application and tests.
- **requirements.txt**: Lists Python dependencies.
- **data.csv**: Dataset containing customer orders.

## Setup

1. **Clone the repository:**

   ```sh
   clone the repository
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

## Additional Commands

1. **Check container logs (optional):**

   You can check the logs of the running containers to debug any issues.

   ```sh
   docker-compose logs
   ```
