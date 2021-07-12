import pandas as pd

def load_data(path) :
    df = pd.read_csv(path)
    df1 = {
        "bill_PayerAccountId": df['bill/PayerAccountId'],
        "lineItem_UnblendedCost": df['lineItem/UnblendedCost'],
        "lineItem_UnblendedRate": df['lineItem/UnblendedRate'],
        "lineItem_UsageAccountId": df['lineItem/UsageAccountId'],
        "lineItem_UsageAmount": df['lineItem/UsageAmount'],
        "lineItem_UsageStartDate": df['lineItem/UsageStartDate'],
        "lineItem_UsageEndDate": df['lineItem/UsageEndDate'],
        "product_ProductName": df['product/ProductName']
    }
    df1 = pd.DataFrame(df1)
    return df1