import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
  #Not eleigible make salary 0
  employees.loc[
    (employees['employee_id']%2==0)|
    (employees['name'].str.startswith('M')),'salary'
  ]=0
  #select employee_id and salary as bonus
  employees_bonus=employees[['employee_id','salary']].rename(
    columns={'salary':'bonus'}
  )
  #return employees_bonus sorted by employee_id
  return employees_bonus.sort_values('employee_id')