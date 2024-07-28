import pandas as pd

# Sample data with 10 records
data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_id': [1, 2, 1, 3, 4, 2, 5, 3, 1, 4],
    'order_date': [
        '2023-01-01', '2023-01-15', '2023-02-01', '2023-02-14', 
        '2023-03-01', '2023-03-15', '2023-04-01', '2023-04-14', 
        '2023-05-01', '2023-05-15'
    ],
    'product_id': [101, 102, 101, 103, 104, 102, 105, 103, 101, 104],
    'product_name': [
        'Product A', 'Product B', 'Product A', 'Product C', 'Product D', 
        'Product B', 'Product E', 'Product C', 'Product A', 'Product D'
    ],
    'product_price': [100, 150, 100, 200, 250, 150, 300, 200, 100, 250],
    'quantity': [1, 2, 1, 3, 1, 2, 1, 3, 1, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('data.csv', index=False)

print("data.csv file with 10 records has been created successfully.")
