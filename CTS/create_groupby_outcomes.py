import pandas as pd

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

group_columns = ['SPO4__PLAYBOOK_NAME__C', 'Customer_Category__c', 'SPO4__OUTCOME_STAGE__C', 'SPO4__CSF_CATEGORY__C', 'SPO4__CSF__C', 'SPO4__OUTCOME__C', 'OPPORTUNITY_WON__C', 'SPO4__COLOR__C']
copy_group_columns= group_columns.copy()
copy_group_columns.append('SPO4__CHANGE_DATE__C')
print(copy_group_columns)
df_book_with_csf = df_all[copy_group_columns].groupby(group_columns).agg(['count'])
print('opo+out', len(df_book_with_csf))
# print(df_book_with_csf)

df_book_with_csf.reset_index(inplace=True)


named_columns = ['SPO4__PLAYBOOK_NAME__C',
                 'Customer_Category__c',
                 'SPO4__OUTCOME_STAGE__C',
                 'SPO4__CSF_CATEGORY__C',
                 'SPO4__CSF__C',
                 'SPO4__OUTCOME__C',
                 ]
df_result = df_all.drop_duplicates(subset=named_columns)[named_columns]
df_result.sort_values(named_columns, inplace=True)

df_result['green'] = 0
df_result['red'] = 0
df_result['grey'] = 0
df_result['Won'] = 0
df_result['Lost'] = 0
df_result['Won_green'] = 0
df_result['Lost_red'] = 0
# df_result['Open'] = list_st_on_csf


df_result['ind'] = df_result[named_columns].apply(lambda x: ''.join(x), axis=1)
df_result.set_index('ind', inplace=True)
# print(df_result.to_string())
# print(df_result.to_string())
# continue
for i, row in df_book_with_csf.iterrows():
    # print(row)
    # pl = row['SPO4__PLAYBOOK_NAME__C']
    # os = row['SPO4__OUTCOME_STAGE__C'].values[0]
    st = row['OPPORTUNITY_WON__C'].values[0]
    cl = row['SPO4__COLOR__C'].values[0]
    # cc = row['SPO4__CSF_CATEGORY__C']
    # cs = row['SPO4__CSF__C']
    # oc = row['SPO4__OUTCOME__C']

    num = row['SPO4__CHANGE_DATE__C']['count']
    data_val = [row[x].values[0] for x in named_columns]
    # print(data_val)
    ind_cs = ''.join(data_val)
    # print(st, cl)
    df_result.loc[ind_cs, cl] += num
    df_result.loc[ind_cs, st] += num

    if (st == 'Won' and cl == 'green') or (st == 'Lost' and cl == 'red'):
        df_result.loc[ind_cs, st + '_' + cl] += num

# df_result['part_green/(green+red+grey)%'] = (df_result['green'] * 100.0)/(df_result['green'] + df_result['grey'] + df_result['red'])
# df_result['part_won/(won+lost) %'] = (df_result['Won'] * 100.0)/(df_result['Won'] + df_result['Lost'])
# df_result.fillna(0, inplace=True)

# print(df_result)
df_result.rename(index=str, columns=rename_dict, inplace=True)

not_used_out = [
    'DOA Executive agrees to move to Stage 2',
    'DOA Executive agrees DEAL is QUALIFIED to move to Stage 3',
    'Proposal Submitted to client - Move to Stage 4',
    'Final Down-selection made by client - Move to Stage 5',
    'BAFO Submitted',
    'Stage 4 Gate : Go / No-Go discussed and decided',
    'Proposal Completed & Approved',
    'Final Cost and price approved by BU finance leadership',
    'Contract Execution Go / No-Go discussed and decided (internal)',
    'Client confirmed Contract Accepted',
    'Contract formally executed',
    'Proposal Submitted to client - Move to Stage 4',
    'Contract formally executed - Move to Stage WON',
]
print('resut before removing outcomes', len(df_result))
for out in not_used_out:
    df_result = df_result[df_result['Outcome'] != out]
    print('after removing', out, len(df_result))


print(df_result)
writer = pd.ExcelWriter('9_12\cts_9_12_data_outcomes.xlsx', engine='xlsxwriter')
df_result.to_excel(writer, sheet_name='data', index=False)

writer.save()
