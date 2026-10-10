import pandas as pd
#Perfrom left join 
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge=pd.merge(
        left=customers,right=orders,
        how='left',
        left_on='id',right_on='customerId'
    )
    #Based on null value filter and select name column
    result=merge[merge['customerId'].isna()][['name']]
    #Rename name-->Customers
    result.columns=['Customers']
    return result
