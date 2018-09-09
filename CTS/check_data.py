import pandas as pd

# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('SPO_UPDATED.csv', index_col=None, sep='\t')

# 'Buyer Relationship and Insight', 'Client Intent to Buy', 'Pursuit Team Readiness', 'Win Themes and Differentiation'

# 0066100000F5C9NAAV


df_all = df_all[(df_all['SPO4__OUTCOME_STAGE__C'] == '1. Engagement')
                | (df_all['SPO4__OUTCOME_STAGE__C'] == '2. Shaping')
]
df_all = df_all[(df_all['SPO4__OPPORTUNITY__C'] == '0066100000F5C9NAAV')
]


df_all = df_all[(df_all['SPO4__CSF__C'] == 'Buyer Relationship and Insight')
                | (df_all['SPO4__CSF__C'] == 'Client Intent to Buy')
                | (df_all['SPO4__CSF__C'] == 'Pursuit Team Readiness')
                | (df_all['SPO4__CSF__C'] == 'Win Themes and Differentiation')
]

df_all.to_csv('t.csv')


# 1
# 2
# 3
# 4
# 5
# 1, 2
# 3, 4
# 3, 4, 5
# 1, 2, 3, 4
# 1, 2, 3, 4, 5