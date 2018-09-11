import pandas as pd
import numpy as np

# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('SPO_UPDATED.csv', index_col=None, sep='\t')

print('all', len(df_all))
main_data = ['SPO4__CSF__C', 'SPO4__OUTCOME__C']

rename_dict = {'SPO4__PLAYBOOK_NAME__C': 'PlayBook',
               'SPO4__OUTCOME_STAGE__C': 'Stage',
               'SPO4__CSF_CATEGORY__C': 'CSF_category',
               'SPO4__CSF__C': 'CSF',
               'SPO4__OUTCOME__C': 'Outcome'
               }

# print(copy_group_columns)


df_all = df_all[(df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal >$50M >$25M CE/UKI or >$10M APAC/LATAM/MEA')
                | (df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal $10-50M $10-25M CE/UKI or $5-10M APAC/LATAM/MEA')
                | (df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal $2-10M or $2-5M APAC/LATAM/MEA')
]


df_all['COLOR_NUM'] = df_all['SPO4__COLOR__C']
df_all.COLOR_NUM.replace(['green', 'grey', 'red'], [1, -1, -1], inplace=True)

# df_all.SPO4__OUTCOME_STAGE__C.replace([
#                     '1. Engagement',
#                     '2. Shaping',
#                     '3. Solutioning',
#                     '4. End-Game',
#                     '5. Negotiation'],
#     ['1', '2', '3', '4', '5', ], inplace=True)


named_columns = ['SPO4__PLAYBOOK_NAME__C',
                 'SPO4__OUTCOME_STAGE__C',
                 'SPO4__CSF_CATEGORY__C',
                 'SPO4__CSF__C',
                 'OPPORTUNITY_WON__C',
                 'SPO4__OPPORTUNITY__C',
                 ]

group_columns = named_columns
copy_group_columns = group_columns.copy()
copy_group_columns.append('COLOR_NUM')


df_book_with_csf = df_all[copy_group_columns].groupby(group_columns).agg(['min'])

df_book_with_csf.reset_index(inplace=True)
# df_book_with_csf['COLOR_NUM']['min'].replace([1, 0, -1], ['green', 'grey', 'red'], inplace=True)

print(df_book_with_csf)
# df_book_with_csf.to_csv('t.csv', sep='\t')

writer = pd.ExcelWriter('cts_data_cfs.xlsx', engine='xlsxwriter')

named_columns = ['SPO4__PLAYBOOK_NAME__C',
                 'SPO4__OUTCOME_STAGE__C',
                 'SPO4__CSF_CATEGORY__C',
                 'SPO4__CSF__C',
                 ]
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
# print(df_csf.to_string())
# print(df_csf.to_string())
# continue
for i, row in df_book_with_csf.iterrows():
    # print(row)
    # pl = row['SPO4__PLAYBOOK_NAME__C']
    # os = row['SPO4__OUTCOME_STAGE__C'].values[0]
    st = row['OPPORTUNITY_WON__C'].values[0]
    # cl = row['COLOR_NUM'].values[0]
    # cc = row['SPO4__CSF_CATEGORY__C']
    # cs = row['SPO4__CSF__C']
    # oc = row['SPO4__OUTCOME__C']

    cl = row['COLOR_NUM']['min']
    if cl == 1:
        cl = 'green'
    elif cl == -1:
        cl = 'red'
    else:
        cl = 'grey'


    data_val = [row[x].values[0] for x in named_columns]
    # print(data_val)
    ind_cs = ''.join(data_val)
    # print(st, cl)
    df_csf.loc[ind_cs, cl] += 1
    df_csf.loc[ind_cs, st] += 1

    if (st == 'Won' and cl == 'green') or (st == 'Lost' and cl == 'red'):
        df_csf.loc[ind_cs, st + '_' + cl] += 1

# df_csf['part_green/(green+red+grey)%'] = (df_csf['green'] * 100.0)/(df_csf['green'] + df_csf['grey'] + df_csf['red'])
# df_csf['part_won/(won+lost) %'] = (df_csf['Won'] * 100.0)/(df_csf['Won'] + df_csf['Lost'])
# df_csf.fillna(0, inplace=True)

# print(df_csf)
df_csf.rename(index=str, columns=rename_dict, inplace=True)
print(df_csf)
df_csf.to_excel(writer, sheet_name='data', index=False)

writer.save()
