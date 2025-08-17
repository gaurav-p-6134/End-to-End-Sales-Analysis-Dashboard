import pandas as pd

# --- 1. LOAD THE DATA ---
input_filepath = '.venv/data/train.csv' # Make sure this filename is correct!

print(f"Loading data from {input_filepath}...")
try:
    df = pd.read_csv(input_filepath, encoding='latin-1')
    print("Data loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{input_filepath}' was not found.")
    print("Please make sure the CSV file is in the correct directory and the filename is spelled correctly.")
    exit()

# --- 2. INITIAL INSPECTION ---
print("\n--- Initial Data Inspection ---")
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataframe Information (before cleaning):")
df.info()

print("\nChecking for missing values (before cleaning):")
print(df.isnull().sum())

print(f"\nNumber of duplicate rows found: {df.duplicated().sum()}")


# --- 3. CLEAN THE DATA ---
print("\n--- Starting Data Cleaning ---")

# Remove duplicate rows, if any
df.drop_duplicates(inplace=True)
print(f"Removed duplicate rows. New shape: {df.shape}")

# Correct data types for date columns with highly mixed formats
print("Converting highly mixed-format date columns to datetime objects...")

# Use format='mixed' to parse each date individually
# Keep dayfirst=True to handle ambiguous dates like '03-04-2021' correctly
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed', dayfirst=True)

print("Converted 'Order Date' and 'Ship Date' to datetime objects.")

# --- 4. FEATURE ENGINEERING ---
print("\n--- Starting Feature Engineering ---")

# Extract year and month from the 'Order Date' for easier filtering and aggregation
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
print("Created 'Order Year' and 'Order Month' columns.")

# Calculate Profit Margin to analyze profitability more effectively
# We add a small value (1e-9) to avoid division by zero if sales are 0.
df['Profit Margin'] = (df['Profit'] / (df['Sales'] + 1e-9)) * 100
print("Created 'Profit Margin' column.")


# --- 5. FINAL INSPECTION & SAVE ---
print("\n--- Final Data Inspection ---")
print("Dataframe Information (after cleaning and feature engineering):")
df.info()

print("\nFirst 5 rows of the cleaned and enriched data:")
print(df.head())

# Define the output file path
output_filepath = 'cleaned_superstore_sales.csv'

# Save the cleaned dataframe to a new CSV file
# index=False prevents pandas from writing the dataframe index as a column
df.to_csv(output_filepath, index=False)

print(f"\n✅ Process complete. Cleaned data saved to '{output_filepath}'.")