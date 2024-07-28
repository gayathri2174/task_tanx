import unittest
import pandas as pd
import sys
import os

# Adjust the system path to include the parent directory for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import functions to be tested
from app.main import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_customers_by_revenue

class TestMain(unittest.TestCase):
    """Test suite for the functions in the app.main module."""

    def setUp(self):
        """
        Set up test data for the test cases.
        Creates a sample DataFrame to be used in tests.
        """
        data = {
            'order_id': [1, 2, 3],
            'customer_id': [1, 2, 1],
            'order_date': ['2023-01-01', '2023-01-15', '2023-02-01'],
            'product_id': [101, 102, 101],
            'product_name': ['Product A', 'Product B', 'Product A'],
            'product_price': [100, 150, 100],
            'quantity': [1, 2, 1]
        }
        self.df = pd.DataFrame(data)

    def test_compute_monthly_revenue(self):
        """
        Test the compute_monthly_revenue function.
        Checks if the monthly revenue is calculated correctly.
        """
        result = compute_monthly_revenue(self.df)
        # Verify January revenue
        self.assertEqual(result.iloc[0]['Total Revenue'], 250)
        # Verify February revenue
        self.assertEqual(result.iloc[1]['Total Revenue'], 100)

    def test_compute_product_revenue(self):
        """
        Test the compute_product_revenue function.
        Checks if the revenue by product is calculated correctly.
        """
        result = compute_product_revenue(self.df)
        # Verify revenue for Product A
        self.assertEqual(result[result['Product Name'] == 'Product A']['Total Revenue'].values[0], 200)
        # Verify revenue for Product B
        self.assertEqual(result[result['Product Name'] == 'Product B']['Total Revenue'].values[0], 150)

    def test_compute_customer_revenue(self):
        """
        Test the compute_customer_revenue function.
        Checks if the revenue by customer is calculated correctly.
        """
        result = compute_customer_revenue(self.df)
        # Verify revenue for Customer ID 1
        self.assertEqual(result[result['Customer ID'] == 1]['Total Revenue'].values[0], 200)
        # Verify revenue for Customer ID 2
        self.assertEqual(result[result['Customer ID'] == 2]['Total Revenue'].values[0], 150)

    def test_top_customers_by_revenue(self):
        """
        Test the top_customers_by_revenue function.
        Checks if the top customers are identified correctly based on revenue.
        """
        customer_revenue = compute_customer_revenue(self.df)
        result = top_customers_by_revenue(customer_revenue)
        # Verify the top customer by revenue
        self.assertEqual(result.iloc[0]['Customer ID'], 1)
        # Verify the second top customer by revenue
        self.assertEqual(result.iloc[1]['Customer ID'], 2)

if __name__ == '__main__':
    unittest.main()
