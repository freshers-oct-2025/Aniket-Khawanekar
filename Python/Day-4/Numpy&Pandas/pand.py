import pandas as pd

df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 75000, 55000],
    'Department': ['IT', 'HR', 'IT', 'Finance']
})

print("DataFrame:\n", df1)

print("\nInfo:")
print(df1.info())

print("\nDescribe:")
print(df1.describe())



print("\nEmployees with salary > 55000:")
print(df1[df1['Salary'] > 55000])

print("\nAverage salary by department:")
print(df1.groupby('Department')['Salary'].mean())

df1.to_csv('employees.csv', index=False)
df_read = pd.read_csv('employees.csv')

df1['Bonus'] = df1['Salary'] * 0.1
df1['Total_Compensation'] = df1['Salary'] + df1['Bonus']

print("\nUpdated DataFrame:")
print(df1)