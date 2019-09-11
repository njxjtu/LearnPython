"""
DataFrame.merge(self, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
"""

np.random.seed(0)
left = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': np.random.randn(4)})    
right = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': np.random.randn(4)})

pd.merge(left, right, on='key')

pd.merge(left, right, on='key', how='left')

(pd.merge(left, right, on='key', how='left', indicator=True)
     .query('_merge == "left_only"')
     .drop('_merge', 1))
