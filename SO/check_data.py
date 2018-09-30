import pandas as pd
import numpy as np

# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('SO - SPOOUtcomeAtomicValue extract 2.csv', index_col=None, sep=',')

# df_pb = df_all[df_all['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISCLOSED'] == True]
# # df_pb = df_pb[df_all['SPO4__PLAYBOOK_NAME__C'] == '#2-Direct Competitive Net New']
# df_stat = df_pb.drop_duplicates(subset=['SPO4__SPOOPPORTUNITY__C', 'SPO4__PLAYBOOK_NAME__C'])
# # df_stat.to_csv('1.csv')
#
# df = df_stat.pivot_table(index=['SPO4__PLAYBOOK_NAME__C'], columns=['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISCLOSED','SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISWON'] , values=['SPO4__SPOOPPORTUNITY__C'],aggfunc=len)
# print(df.to_string)


df_all = df_all[df_all['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISCLOSED'] == True]
df = df_all.pivot_table(index=['SPO4__PLAYBOOK_NAME__C', 'SPO4__OUTCOME_STAGE__C','SPO4__OUTCOME__C'], columns=['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISWON'] , values=['SPO4__SPOOPPORTUNITY__C'],aggfunc=np.count_nonzero)
print(df.to_string())


# df_pb = df_all[df_all['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISCLOSED'] == True]
# df_pb = df_pb[df_pb['SPO4__PLAYBOOK_NAME__C'] == '#2-Direct Competitive Net New']
# df_pb['OPPORTUNITY__STATUS'] = df_pb['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISWON']
# df_pb['OPPORTUNITY__STATUS'].replace([True, False], ['Won', 'Lost'], inplace=True)
# # df = df_pb.pivot_table(index=['SPO4__OPPORTUNITY__C', 'OPPORTUNITY__STATUS'], columns=['SPO4__OUTCOME__C'] , values=['SPO4__COLOR__C'],aggfunc=np.count_nonzero)
# df_pb = df_pb.drop_duplicates(subset=['SPO4__SPOOPPORTUNITY__C'])
# # print(df_pb.to_string)
# # df_pb.to_csv('2.csv')
# df = df_pb.pivot_table(index=['SPO4__PLAYBOOK_NAME__C'], columns=['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISCLOSED','SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISWON'] , values=['SPO4__SPOOPPORTUNITY__C'],aggfunc=len)
# print(df.to_string)
#
# df.to_csv('so_stat.csv', sep=';')