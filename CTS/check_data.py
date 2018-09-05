import pandas as pd

# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('SPO_UPDATED_WITHOUT_GREY.csv', index_col=None, sep='\t')

# df_book_with_csf = df_all[['SPO4__OUTCOME_STAGE__C', 'SPO4__CSF__C', 'SPO4__OUTCOME__C','SPO4__CHANGE_DATE__C']].groupby(['SPO4__OUTCOME_STAGE__C', 'SPO4__CSF__C', 'SPO4__OUTCOME__C',]).agg(['count'])
# print(df_book_with_csf.to_string())

# group_columns = ['SPO4__PLAYBOOK_NAME__C', 'SPO4__OUTCOME_STAGE__C', 'SPO4__CSF_CATEGORY__C', 'SPO4__CSF__C', 'SPO4__OUTCOME__C', 'OPPORTUNITY_CLOSED__C', 'SPO4__COLOR__C']
# df = df_all.drop_duplicates(subset=group_columns)
# df.sort_values(group_columns, inplace=True)
# print(df.to_string())

rename_dict = {'SPO4__PLAYBOOK_NAME__C': 'PlayBook',
               'SPO4__OUTCOME_STAGE__C': 'Stage',
               'SPO4__CSF_CATEGORY__C': 'CSF_category',
               'SPO4__CSF__C': 'CSF',
               'SPO4__OUTCOME__C': 'Outcome'
               }

writer = pd.ExcelWriter('cts_data_analise_without_grey.xlsx', engine='xlsxwriter')
group_columns = ['SPO4__PLAYBOOK_NAME__C', 'SPO4__OUTCOME_STAGE__C', 'SPO4__CSF_CATEGORY__C', 'SPO4__CSF__C',
                 'SPO4__OUTCOME__C', 'OPPORTUNITY_CLOSED__C', 'SPO4__COLOR__C']
copy_group_columns = group_columns.copy()
copy_group_columns.append('SPO4__CHANGE_DATE__C')
print(copy_group_columns)
df_book_with_csf = df_all[copy_group_columns].groupby(group_columns).agg(['count'])
print('opo+out', len(df_book_with_csf))
# print(df_book_with_csf)

df_book_with_csf.reset_index(inplace=True)

named_columns = list(rename_dict.keys())
df_csf = df_all.drop_duplicates(subset=named_columns)[named_columns]
df_csf.sort_values(named_columns, inplace=True)

df_csf['green'] = 0
df_csf['red'] = 0
# df_csf['grey'] = 0
df_csf['Won'] = 0
df_csf['Lost'] = 0
df_csf['Won_green'] = 0
df_csf['Lost_red'] = 0
# df_csf['Open'] = list_st_on_csf


df_csf['ind'] = df_csf[named_columns].apply(lambda x: ''.join(x), axis=1)
df_csf.set_index('ind', inplace=True)

print(df_csf.to_string())

for i, row in df_book_with_csf.iterrows():
    # print(row)
    pl = row['SPO4__PLAYBOOK_NAME__C']
    os = row['SPO4__OUTCOME_STAGE__C']
    st = row['OPPORTUNITY_CLOSED__C']
    cl = row['SPO4__COLOR__C']
    cc = row['SPO4__CSF_CATEGORY__C']
    cs = row['SPO4__CSF__C']
    oc = row['SPO4__OUTCOME__C']
    data_val = [row[x].values[0] for x in named_columns]
    # print(data_val)
    ind_cs = ''.join(data_val)
    print(ind_cs)