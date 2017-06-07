import pandas

df1 = pandas.DataFrame(
    [[1,2,3], [4,5,6]],
    columns=["One", "Two", "Three"],
    index=['Row1', 'Row2']
)

df2 = pandas.DataFrame(
    [{'Name':'Alex','Surname':'USA'}, {'Name':'Nat','Surname':'USA'}, {'Name':'Lisa'}]
)

print(df1)
print(df2)

print(df1.mean())
print(df1.mean().mean())
