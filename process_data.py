import pandas as pd
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]
dataframes = []
for file in files:
    df = pd.read_csv(file)
    df = df[df["product"] == "pink morsel"]
    df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)
    df["sales"] = df["price"] * df["quantity"]
    df = df[["sales", "date", "region"]]
    df.columns = ["Sales", "Date", "Region"]
    dataframes.append(df)
final_df = pd.concat(dataframes, ignore_index=True)
final_df.to_csv("formatted_sales_data.csv", index=False)
print("formatted_sales_data.csv created successfully!")