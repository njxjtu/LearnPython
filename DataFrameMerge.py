np.random.seed(0)
left = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': np.random.randn(4)})    
right = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': np.random.randn(4)})

pd.merge(left, right, on='key')

left.merge(right, on='key', how='left')

(left.merge(right, on='key', how='left', indicator=True)
     .query('_merge == "left_only"')
     .drop('_merge', 1))
