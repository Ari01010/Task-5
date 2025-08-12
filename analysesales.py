import pandas as pd

def analyze_sales_data(sales_data.csv):
    """
    Analyzes sales data from a CSV file using Pandas.

    Args:
        file_path (str): The path to the sales data CSV file.
    """
    try:
        # Read the CSV file into a Pandas DataFrame. [1, 2, 3]
        sales_df = pd.read_csv(file_path)

        # --- Display Basic Information ---
        print("--- Basic Data Information ---")
        print("\nFirst 5 rows of the dataset:")
        print(sales_df.head())

        print("\nInformation about the dataset:")
        sales_df.info()

        # --- Data Cleaning (Example: Handling Missing Values) ---
        # sales_df.dropna(inplace=True)

        # --- Core Sales Analysis ---

        # Calculate the total sales by creating a 'TotalSales' column. [4, 7]
        sales_df['TotalSales'] = sales_df['Price'] * sales_df['Quantity']

        # 1. Calculate the overall total sales. [10, 15]
        total_sales = sales_df['TotalSales'].sum()

        # 2. Determine the total sales by product category. [7, 17]
        sales_by_category = sales_df.groupby('Category')['TotalSales'].sum()

        # 3. Identify the best-selling products by quantity. [11, 16]
        best_selling_products = sales_df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)


        # --- Print the Analysis Results ---
        print("\n\n--- Sales Analysis Results ---")

        print(f"\nTotal Sales: ${total_sales:,.2f}")

        print("\nTotal Sales by Category:")
        print(sales_by_category)

        print("\nBest-Selling Products (by Quantity):")
        print(best_selling_products)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # The name of your CSV file.
    csv_file = 'sales_data.csv'
    analyze_sales_data(csv_file)
