

Create a new column where it is `True` if some condition happens in another column. Easier than `map(dict)`
`voice['test_account'] = voice['participant_id'].astype(str).map(lambda x: 'test' in x)`
