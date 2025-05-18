import pandas as pd

# Generic Construction
print(pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}))


# Flexible Datatypes
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}))


# Custom Indexing
print(pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B']))

# Series is a list
print(pd.Series([1, 2, 3, 4, 5]))
# Custon Indexing
print(pd.Series([1, 2, 3, 4, 5], index =["2015 Sales", "2016 Sales", "2017 Sales", "2018 Sales", "2019 Sales"]))