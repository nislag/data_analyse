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


groups = [
    ['1',],
    ['2',],
    ['3',],
    ['4',],
    ['5',],
    ['1', '2',],
    ['3', '4',],
    ['3', '4', '5',],
    ['1', '2', '3', '4',],
    ['1', '2', '3', '4', '5',],

]
df_all['COLOR_NUM'] = df_all['SPO4__COLOR__C']
df_all.COLOR_NUM.replace(['green', 'grey', 'red'], [1, 0, -1], inplace=True)

df_all.SPO4__OUTCOME_STAGE__C.replace([
                    '1. Engagement',
                    '2. Shaping',
                    '3. Solutioning',
                    '4. End-Game',
                    '5. Negotiation'],
    ['1', '2', '3', '4', '5', ], inplace=True)


group_columns = ['SPO4__CSF__C', 'SPO4__OPPORTUNITY__C']
copy_group_columns = group_columns.copy()
copy_group_columns.append('COLOR_NUM')

for group in groups:
    print('!!! group!!!')
    print(group)

    df_group = pd.DataFrame()

    for stage in group:
        df_part = df_all[df_all['SPO4__OUTCOME_STAGE__C'] == stage]
        df_group = df_group.append(df_part)

    print('group grom all len', len(df_group))

    df_book_with_csf = df_group[copy_group_columns].groupby(group_columns).agg(['min'])

    df_book_with_csf.reset_index(inplace=True)
    print('size of groupby',len(df_book_with_csf))

    # df_book_with_csf.to_csv('t.csv')
    df_result = pd.DataFrame()
    opportunities = list(set(df_group['SPO4__OPPORTUNITY__C'].drop_duplicates()))
    df_result['SPO4__OPPORTUNITY__C'] =  opportunities
    df_result.set_index('SPO4__OPPORTUNITY__C', inplace=True)


    # print(df_result)

    results = df_group[['SPO4__OPPORTUNITY__C', 'SPO4__PLAYBOOK_NAME__C', 'OPPORTUNITY_WON__C']].drop_duplicates()

    results.set_index('SPO4__OPPORTUNITY__C', inplace=True)

    df_result = df_result.merge(results, how='left', left_index=True, right_index=True)

    csfs = list(set(df_group['SPO4__CSF__C'].drop_duplicates()))
    print('CSF:', len(csfs))
    csfs.sort()

    for csf in csfs:
        # df_result[csf] = np.nan
        df_result[csf] = 0

    for i, row in df_book_with_csf.iterrows():

        op = row['SPO4__OPPORTUNITY__C'].values[0]
        cs = row['SPO4__CSF__C'].values[0]
        num = row['COLOR_NUM']['min']

        df_result.loc[op, cs] = num

    # df_won = df_result[df_result['OPPORTUNITY_WON__C'] == 'Won']
    # df_won.fillna(1, inplace = True)
    # df_lost = df_result[df_result['OPPORTUNITY_WON__C'] == 'Lost']
    # df_lost.fillna(-1, inplace = True)
    # df_result = df_won.append(df_lost)



    print('group_result_size', df_result.size)
    name_group = "_".join(group)
    df_result.to_csv('csf_data_sets\csf_{}.csv'.format(name_group), index=True,sep='\t')
#
# # df_csf['part_green/(green+red+grey)%'] = (df_csf['green'] * 100.0)/(df_csf['green'] + df_csf['grey'] + df_csf['red'])
# # df_csf['part_won/(won+lost) %'] = (df_csf['Won'] * 100.0)/(df_csf['Won'] + df_csf['Lost'])
# # df_csf.fillna(0, inplace=True)
#
# # print(df_csf)
# df_csf.rename(index=str, columns=rename_dict, inplace=True)
# print(df_csf)
# df_csf.to_excel(writer, sheet_name='data', index=False)

#
#
# df_csf.to_excel('csf.xlsx', index=False)
# df_oc.to_excel('oc.xlsx', index=False)
