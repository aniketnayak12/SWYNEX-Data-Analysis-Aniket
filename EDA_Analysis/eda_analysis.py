import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD CLEANED DATASET
# ============================================================

file_path = r"C:\Users\ankit\OneDrive\Desktop\SWYNEX Project\Data\Cleaned\online_retailed_clean.csv"

df = pd.read_csv(
    file_path,
    encoding="latin1"
)

print("Dataset loaded successfully!")

# Remove accidental spaces from column names
df.columns = df.columns.str.strip()

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())


# ============================================================
# 2. DATA INFORMATION
# ============================================================

print("\n======================================")
print("          DATA INFORMATION")
print("======================================")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ============================================================
# 3. DATA TYPE CONVERSION
# ============================================================

# Convert InvoiceDate
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"],
    format="%d-%m-%Y %H:%M",
    errors="coerce"
)

# Convert numeric columns
df["Quantity"] = pd.to_numeric(
    df["Quantity"],
    errors="coerce"
)

df["UnitPrice"] = pd.to_numeric(
    df["UnitPrice"],
    errors="coerce"
)

df["Revenue"] = pd.to_numeric(
    df["Revenue"],
    errors="coerce"
)


# ============================================================
# 4. KEY STATISTICS
# ============================================================

print("\n======================================")
print("           KEY STATISTICS")
print("======================================")

total_transactions = len(df)

unique_invoices = df["InvoiceNo"].nunique()

unique_customers = df["Cleaned_CustomerID"].nunique()

unique_products = df["StockCode"].nunique()

unique_countries = df["Country"].nunique()

total_quantity = df["Quantity"].sum()

total_revenue = df["Revenue"].sum()

# Revenue per invoice
invoice_revenue = (
    df.groupby("InvoiceNo")["Revenue"]
    .sum()
)

average_order_value = invoice_revenue.mean()

average_quantity = df["Quantity"].mean()


print("Total Transactions:", total_transactions)

print("Unique Invoices:", unique_invoices)

print("Unique Customers:", unique_customers)

print("Unique Products:", unique_products)

print("Unique Countries:", unique_countries)

print("Total Quantity Sold:", total_quantity)

print("Total Revenue:", round(total_revenue, 2))

print(
    "Average Order Value:",
    round(average_order_value, 2)
)

print(
    "Average Quantity per Transaction:",
    round(average_quantity, 2)
)


# ============================================================
# 5. MONTHLY REVENUE TREND
# ============================================================

print("\n======================================")
print("          MONTHLY REVENUE")
print("======================================")

monthly_revenue = (
    df.groupby(
        df["InvoiceDate"].dt.to_period("M")
    )["Revenue"]
    .sum()
)

print(monthly_revenue)


# Convert Period to string for chart
monthly_revenue_chart = monthly_revenue.copy()

monthly_revenue_chart.index = (
    monthly_revenue_chart.index.astype(str)
)


plt.figure(figsize=(12, 6))

plt.plot(
    monthly_revenue_chart.index,
    monthly_revenue_chart.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "monthly_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 6. TOP 10 PRODUCTS BY REVENUE
# ============================================================

print("\n======================================")
print("       TOP 10 PRODUCTS BY REVENUE")
print("======================================")

top_products = (
    df.groupby("Cleaned_Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)


plt.figure(figsize=(10, 6))

top_products.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Products by Revenue")

plt.xlabel("Revenue")

plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    "top_10_products.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 7. TOP 10 COUNTRIES BY REVENUE
# ============================================================

print("\n======================================")
print("       TOP 10 COUNTRIES BY REVENUE")
print("======================================")

country_revenue = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_countries = country_revenue.head(10)

print(top_countries)


plt.figure(figsize=(10, 6))

top_countries.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Countries by Revenue")

plt.xlabel("Revenue")

plt.ylabel("Country")

plt.tight_layout()

plt.savefig(
    "top_10_countries_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 8. TOP 10 COUNTRIES BY QUANTITY
# ============================================================

print("\n======================================")
print("       TOP 10 COUNTRIES BY QUANTITY")
print("======================================")

country_quantity = (
    df.groupby("Country")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

top_quantity_countries = country_quantity.head(10)

print(top_quantity_countries)


plt.figure(figsize=(10, 6))

top_quantity_countries.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Countries by Quantity Sold")

plt.xlabel("Quantity Sold")

plt.ylabel("Country")

plt.tight_layout()

plt.savefig(
    "top_10_countries_quantity.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 9. TOP 10 CUSTOMERS BY REVENUE
# ============================================================

print("\n======================================")
print("       TOP 10 CUSTOMERS BY REVENUE")
print("======================================")

customer_revenue = (
    df.groupby("Cleaned_CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_customers = customer_revenue.head(10)

print(top_customers)


plt.figure(figsize=(10, 6))

top_customers.sort_values().plot(
    kind="barh"
)

plt.title("Top 10 Customers by Revenue")

plt.xlabel("Revenue")

plt.ylabel("Customer ID")

plt.tight_layout()

plt.savefig(
    "top_10_customers.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 10. REVENUE DISTRIBUTION
# ============================================================

print("\n======================================")
print("          REVENUE DISTRIBUTION")
print("======================================")

plt.figure(figsize=(10, 6))

plt.hist(
    df["Revenue"].dropna(),
    bins=50
)

plt.title("Revenue Distribution")

plt.xlabel("Revenue per Transaction")

plt.ylabel("Number of Transactions")

plt.tight_layout()

plt.savefig(
    "revenue_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# 11. HIGH-VALUE TRANSACTIONS / ANOMALIES
# ============================================================

print("\n======================================")
print("       HIGH-VALUE TRANSACTIONS")
print("======================================")

revenue_threshold = df["Revenue"].quantile(0.99)

high_value_transactions = df[
    df["Revenue"] >= revenue_threshold
]

print(
    "99th Percentile Revenue Threshold:",
    round(revenue_threshold, 2)
)

print(
    "Number of High-Value Transactions:",
    len(high_value_transactions)
)

print("\nTop High-Value Transactions:")

print(
    high_value_transactions[
        [
            "InvoiceNo",
            "Cleaned_Description",
            "Quantity",
            "UnitPrice",
            "Revenue"
        ]
    ]
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(20)
)


# ============================================================
# 12. LARGE QUANTITY TRANSACTIONS
# ============================================================

print("\n======================================")
print("       LARGE QUANTITY TRANSACTIONS")
print("======================================")

large_quantity = df.nlargest(
    10,
    "Quantity"
)

print(
    large_quantity[
        [
            "InvoiceNo",
            "Cleaned_Description",
            "Quantity",
            "UnitPrice",
            "Revenue"
        ]
    ]
)


# ============================================================
# 13. BEST AND WORST MONTH
# ============================================================

best_month = monthly_revenue.idxmax()

best_month_revenue = monthly_revenue.max()

worst_month = monthly_revenue.idxmin()

worst_month_revenue = monthly_revenue.min()


print("\n======================================")
print("          MONTHLY INSIGHTS")
print("======================================")

print(
    "Highest Revenue Month:",
    best_month
)

print(
    "Highest Monthly Revenue:",
    round(best_month_revenue, 2)
)

print(
    "Lowest Revenue Month:",
    worst_month
)

print(
    "Lowest Monthly Revenue:",
    round(worst_month_revenue, 2)
)


# ============================================================
# 14. TOP PRODUCT
# ============================================================

best_product = top_products.idxmax()

best_product_revenue = top_products.max()


print("\n======================================")
print("          PRODUCT INSIGHT")
print("======================================")

print(
    "Top Product:",
    best_product
)

print(
    "Top Product Revenue:",
    round(best_product_revenue, 2)
)


# ============================================================
# 15. TOP COUNTRY
# ============================================================

best_country = country_revenue.idxmax()

best_country_revenue = country_revenue.max()


print("\n======================================")
print("          COUNTRY INSIGHT")
print("======================================")

print(
    "Top Country:",
    best_country
)

print(
    "Top Country Revenue:",
    round(best_country_revenue, 2)
)


# ============================================================
# 16. SAVE EDA SUMMARY
# ============================================================

summary = pd.DataFrame({

    "Metric": [

        "Total Transactions",

        "Unique Invoices",

        "Unique Customers",

        "Unique Products",

        "Unique Countries",

        "Total Quantity Sold",

        "Total Revenue",

        "Average Order Value",

        "Average Quantity per Transaction",

        "Highest Revenue Month",

        "Highest Revenue Month Value",

        "Lowest Revenue Month",

        "Lowest Revenue Month Value",

        "Top Product",

        "Top Product Revenue",

        "Top Country",

        "Top Country Revenue"

    ],

    "Value": [

        total_transactions,

        unique_invoices,

        unique_customers,

        unique_products,

        unique_countries,

        total_quantity,

        round(total_revenue, 2),

        round(average_order_value, 2),

        round(average_quantity, 2),

        str(best_month),

        round(best_month_revenue, 2),

        str(worst_month),

        round(worst_month_revenue, 2),

        best_product,

        round(best_product_revenue, 2),

        best_country,

        round(best_country_revenue, 2)

    ]

})


summary.to_csv(
    "eda_summary.csv",
    index=False
)


# ============================================================
# 17. FINAL MESSAGE
# ============================================================

print("\n======================================")
print("       EDA ANALYSIS COMPLETED")
print("======================================")

print("\nCharts created:")

print("1. monthly_revenue.png")

print("2. top_10_products.png")

print("3. top_10_countries_revenue.png")

print("4. top_10_countries_quantity.png")

print("5. top_10_customers.png")

print("6. revenue_distribution.png")

print("7. eda_summary.csv")

print("\nTask 2 analysis completed successfully!")