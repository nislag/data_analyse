import pandas as pd
import numpy as np

# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('9_12\SPO_9_12_UPDATED.csv', index_col=None, sep='\t')

print('all', len(df_all))
main_data = ['SPO4__CSF__C', 'SPO4__OUTCOME__C']

rename_dict = {'SPO4__PLAYBOOK_NAME__C': 'PlayBook',
               'Customer_Category__c': 'Customer_Category',
               'SPO4__OUTCOME_STAGE__C': 'Stage',
               'SPO4__CSF_CATEGORY__C': 'CSF_category',
               'SPO4__CSF__C': 'CSF',
               'SPO4__OUTCOME__C': 'Outcome'
               }

# print(copy_group_columns)


# df_all = df_all[(df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal >$50M >$25M CE/UKI or >$10M APAC/LATAM/MEA')
#                 | (df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal $10-50M $10-25M CE/UKI or $5-10M APAC/LATAM/MEA')
#                 | (df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal $2-10M or $2-5M APAC/LATAM/MEA')
#                 | (df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal <$2M')
# ]


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
                 'Customer_Category__c',
                 'SPO4__OUTCOME_STAGE__C',
                 'SPO4__CSF_CATEGORY__C',
                 'SPO4__CSF__C',
                 'OPPORTUNITY_WON__C',
                 ]

group_columns = named_columns.copy()
group_columns.append('SPO4__OPPORTUNITY__C')
copy_group_columns = group_columns.copy()
copy_group_columns.append('COLOR_NUM')

df_book_with_csf = df_all[copy_group_columns].groupby(group_columns).agg(['min'])

df_book_with_csf.reset_index(inplace=True)
df_book_with_csf.columns = df_book_with_csf.columns.droplevel(1)
df_book_with_csf['COLOR_NUM'].replace([1, 0, -1], ['green', 'grey', 'red'], inplace=True)

print(df_book_with_csf)
df_book_with_csf.to_csv('9_12\cts_9_12_data_cfs_not_group.csv', sep='\t' , index=False)

named_columns.append('COLOR_NUM')
copy_group_columns = named_columns.copy()
copy_group_columns.append('SPO4__OPPORTUNITY__C')

df_book_with_csf = df_book_with_csf[copy_group_columns].groupby(named_columns).agg(['count'])

df_book_with_csf.reset_index(inplace=True)
df_book_with_csf.columns = df_book_with_csf.columns.droplevel(1)
print(df_book_with_csf)


named_columns = ['SPO4__PLAYBOOK_NAME__C',
                 'Customer_Category__c',
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

lists_for_index =[]
for name_col in named_columns:
    data = df_book_with_csf[name_col].values.tolist()
    lists_for_index.append(data)

won_list  = df_book_with_csf['OPPORTUNITY_WON__C'].values.tolist()
# df_book_with_csf['COLOR_NUM'].replace(['green', 'grey', 'red'], [1, 0, -1], inplace=True)
color_list  = df_book_with_csf['COLOR_NUM'].values.tolist()
count_list  = df_book_with_csf['SPO4__OPPORTUNITY__C'].values.tolist()

for i in range(len(won_list)):
    # print(i)
    count = count_list[i]
    st = won_list[i]
    cl = color_list[i]
    # if cl == 1:
    #     cl = 'green'
    # elif cl == -1:
    #     cl = 'red'
    # else:
    #     cl = 'grey'

    data_val = [x[i] for x in lists_for_index]
    ind_cs = ''.join(data_val)
    # print(st, cl)
    df_csf.loc[ind_cs, cl] += count
    df_csf.loc[ind_cs, st] += count

    if (st == 'Won' and cl == 'green') or (st == 'Lost' and cl == 'red'):
        df_csf.loc[ind_cs, st + '_' + cl] += count



# for i, row in df_book_with_csf.iterrows():
#     st = row['OPPORTUNITY_WON__C'].values[0]
#     cl = row['COLOR_NUM']['min']
#     if cl == 1:
#         cl = 'green'
#     elif cl == -1:
#         cl = 'red'
#     else:
#         cl = 'grey'
#     data_val = [row[x].values[0] for x in named_columns]
#     ind_cs = ''.join(data_val)
#     # print(st, cl)
#     df_csf.loc[ind_cs, cl] += 1
#     df_csf.loc[ind_cs, st] += 1
#
#     if (st == 'Won' and cl == 'green') or (st == 'Lost' and cl == 'red'):
#         df_csf.loc[ind_cs, st + '_' + cl] += 1

# df_csf['part_green/(green+red+grey)%'] = (df_csf['green'] * 100.0)/(df_csf['green'] + df_csf['grey'] + df_csf['red'])
# df_csf['part_won/(won+lost) %'] = (df_csf['Won'] * 100.0)/(df_csf['Won'] + df_csf['Lost'])
# df_csf.fillna(0, inplace=True)

# print(df_csf)
df_csf.rename(index=str, columns=rename_dict, inplace=True)
print(df_csf)
writer = pd.ExcelWriter('9_12\cts_9_12_data_cfs.xlsx', engine='xlsxwriter')
df_csf.to_excel(writer, sheet_name='data', index=False)

writer.save()
