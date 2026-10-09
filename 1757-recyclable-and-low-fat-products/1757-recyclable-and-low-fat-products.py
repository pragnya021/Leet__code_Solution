import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    product=(products["low_fats"]=="Y")&(products["recyclable"]=="Y")
    return products.loc[product,["product_id"]]