
import pandas as pd
import numpy as np

df = pd.DataFrame({'ele_id':['a', 'a', 'b', 'b', 'a'],
	'floors_in service':np.random.randn(5)})
print(df)
print('-'*40)

grouped = df['floors_in service'].groupby(df['ele_id'])

uniques=df['ele_id'].unique()
print(uniques)
print('The numner of ele is ',len(uniques))
print('-'*40)


result=dict(list(grouped))
for eleid in uniques:
	print('The ID of the elevator is:', eleid)
	print('The number of the floors_in_service is:', list(result[eleid]))
	print('The sum of all the elements in the list is:', sum(list(result[eleid])))
	print('-'*100)

# print(list(result['a']))