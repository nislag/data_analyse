import pandas as pd
import numpy as np


df_all = pd.DataFrame.from_csv('SO - SPOOUtcomeAtomicValue extract 2.csv', index_col=None, sep=',')


writer = pd.ExcelWriter('so_net_new_data_analise_2.xlsx', engine='xlsxwriter')

df_pb = df_all[df_all['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISCLOSED'] == True]
df_pb = df_pb[df_pb['SPO4__PLAYBOOK_NAME__C'] == '#2-Direct Competitive Net New']
df_pb.reset_index(inplace=True)
df_pb.SPO4__COLOR__C.replace(['green', 'grey', 'red'], [1, 0, -1], inplace=True)
df_pb['OPPORTUNITY__STATUS'] = df_pb['SPO4__SPOOPPORTUNITY__R.SPO4__OPPORTUNITY__R.ISWON']
df_pb['OPPORTUNITY__STATUS'].replace([True, False], ['Won', 'Lost'], inplace=True)
# print(df_pb.to_string())
df_stages_out = df_pb.pivot_table(index=['SPO4__OUTCOME_STAGE__C','SPO4__OUTCOME__C'], columns=['SPO4__COLOR__C'] , values=['SPO4__SPOOPPORTUNITY__C'],aggfunc=len)
df_stages_out.sort_values(['SPO4__OUTCOME_STAGE__C','SPO4__OUTCOME__C'], inplace=True)

df_stages_out = df_stages_out[df_stages_out['SPO4__SPOOPPORTUNITY__C'][-1] > 50]
print(df_stages_out.to_string())

df_to_save = df_stages_out
df_to_save.columns = df_to_save.columns.droplevel()
# df_to_save.columns = df_to_save.columns.droplevel()
df_to_save.to_excel(writer, 'Prediction')


df_stages_out.reset_index(inplace=True)
# print(df_stages_out)
outcomes = df_stages_out['SPO4__OUTCOME__C'].values.tolist()
print(len(outcomes))
# df_stages_out.to_excel(writer, '2')

df_data = df_pb[['SPO4__OPPORTUNITY__C', 'OPPORTUNITY__STATUS']].drop_duplicates()

df_data.set_index('SPO4__OPPORTUNITY__C', inplace=True)
# print(df_data)
# df_result = df_result.merge(results, how='left', left_index=True, right_index=True)


for outcome in outcomes:
    # df_result[csf] = np.nan
    df_data[outcome] = 0

for i, row in df_pb.iterrows():
    op = row['SPO4__OPPORTUNITY__C']
    out = row['SPO4__OUTCOME__C']
    color = row['SPO4__COLOR__C']
    if out in outcomes:
        df_data.loc[op, out] = color

df_data.to_excel(writer, 'Data')

writer.save()
