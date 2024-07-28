import pandas as pd

def read_data(file_path):
    return pd.read_csv(file_path)

def compute_monthly_revenue(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    monthly_revenue = df.groupby('month')['product_price'].sum().reset_index()
    monthly_revenue.columns = ['Month', 'Total Revenue']
    return monthly_revenue

def compute_product_revenue(df):
    product_revenue = df.groupby('product_name')['product_price'].sum().reset_index()
    product_revenue.columns = ['Product Name', 'Total Revenue']
    return product_revenue

def compute_customer_revenue(df):
    customer_revenue = df.groupby('customer_id')['product_price'].sum().reset_index()
    customer_revenue.columns = ['Customer ID', 'Total Revenue']
    return customer_revenue

def top_customers_by_revenue(customer_revenue, top_n=10):
    top_customers = customer_revenue.sort_values(by='Total Revenue', ascending=False).head(top_n)
    return top_customers

def main():
    file_path = 'data.csv'
    df = read_data(file_path)
    
    monthly_revenue = compute_monthly_revenue(df)
    print("Monthly Revenue:\n", monthly_revenue)
    
    product_revenue = compute_product_revenue(df)
    print("Product Revenue:\n", product_revenue)
    
    customer_revenue = compute_customer_revenue(df)
    print("Customer Revenue:\n", customer_revenue)
    
    top_customers = top_customers_by_revenue(customer_revenue)
    print("Top 10 Customers:\n", top_customers)

if __name__ == "__main__":
    main()
