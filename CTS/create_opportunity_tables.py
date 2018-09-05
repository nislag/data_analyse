import pandas as pd

# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('SPO_UPDATED_WITHOUT_GREY.csv', index_col=None, sep='\t')

print('all', len(df_all))
main_data = ['SPO4__CSF__C', 'SPO4__OUTCOME__C']

rename_dict = {'SPO4__PLAYBOOK_NAME__C': 'PlayBook',
               'SPO4__OUTCOME_STAGE__C': 'Stage',
               'SPO4__CSF_CATEGORY__C': 'CSF_category',
               'SPO4__CSF__C': 'CSF',
               'SPO4__OUTCOME__C': 'Outcome'
               }


df_all.SPO4__COLOR__C.replace(['green', 'grey', 'red'], [1, 0, -1], inplace=True)

playbooks = list(set(df_all['SPO4__PLAYBOOK_NAME__C'].drop_duplicates()))
print(playbooks)

for playbook in playbooks:
    # if playbook == 'Noncompetitive':
    # if playbook != 'Competitive deal >$50M >$25M CE/UKI or >$10M APAC/LATAM/MEA':
    #     continue

    df_pb = df_all[df_all['SPO4__PLAYBOOK_NAME__C'] == playbook]
    print(playbook, len(df_pb))
    # print(df_pb)
    # continue

    group_columns = ['SPO4__OUTCOME_STAGE__C', 'SPO4__CSF_CATEGORY__C', 'SPO4__CSF__C', 'SPO4__OUTCOME__C']

    named_columns = [
                     'SPO4__OUTCOME_STAGE__C',
                     'SPO4__CSF_CATEGORY__C',
                     'SPO4__CSF__C',
                     'SPO4__OUTCOME__C',
                     ]

    df_csf = df_pb.drop_duplicates(subset=named_columns)[named_columns]
    df_csf.sort_values(named_columns, inplace=True)
    df_csf['Opportunities'] = df_csf[named_columns].apply(lambda x: ''.join(x), axis=1)
    df_csf.set_index('Opportunities', inplace=True)
    df_T = df_csf.transpose()

    # df_T.to_excel('tt.xlsx')

    df_O = pd.DataFrame()
    opportunities = list(set(df_pb['SPO4__OPPORTUNITY__C'].drop_duplicates()))
    df_O['Opportunities'] =  opportunities
    df_O.set_index('Opportunities', inplace=True)

    df_result = df_T.append(df_O)
    df_result.rename(index={'SPO4__OUTCOME__C':'Opportunity'}, inplace=True)

    results = df_pb[['SPO4__OPPORTUNITY__C', 'OPPORTUNITY_WON__C']].drop_duplicates()
    results.rename(index=str, columns={'SPO4__OPPORTUNITY__C':'Opportunities', 'OPPORTUNITY_WON__C':'Opportunity_status'}, inplace=True)
    results.set_index('Opportunities', inplace=True)

    # print(results)
    # print(df_result)

    # df_result['Opportunity_status'] = 'Opportunity_status'
    df_result.fillna(0, inplace=True)

    df_result = df_result.merge(results, how='left', left_index=True, right_index=True)
    # print(df_result)

    list_for_index =[df_pb[x].values.tolist() for x in named_columns]
    list_op = df_pb['SPO4__OPPORTUNITY__C'].values.tolist()
    list_st = df_pb['OPPORTUNITY_WON__C'].values.tolist()
    list_cl = df_pb['SPO4__COLOR__C'].values.tolist()

    for i in range(len(df_pb)):
        # print(i)
        # op = row['SPO4__OPPORTUNITY__C']
        op = list_op[i]
        # st = row['OPPORTUNITY_WON__C']
        st = list_st[i]
        # cl = row['SPO4__COLOR__C']
        cl = list_cl[i]

        col_cs = ''
        for x in list_for_index:
            col_cs = col_cs+ x[i]
        # data_val = [x[i] for x in list_for_index]
        # print(data_val)
        # col_cs = ''.join(data_val)
        # print(st, cl)
        df_result.loc[op, col_cs] = cl
        # df_result.loc[op, 'Opportunity_status'] = st

    playbook_name = playbook
    playbook_name = playbook_name.replace('$', '')
    playbook_name = playbook_name.replace('<', '')
    playbook_name = playbook_name.replace('>', '')
    playbook_name = playbook_name.split(' ')
    if len(playbook_name) > 2:
        playbook_name = playbook_name[0] + '_' + playbook_name[1] + '_' + playbook_name[2]
    else:
        playbook_name = playbook
    # df_result.to_csv('cts_{}.csv'.format(playbook_name), sep=';')
    cols = df_result.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df_result = df_result[cols]
    df_result.to_excel('cts_{}.xlsx'.format(playbook_name))
#
#
# df_csf.to_excel('csf.xlsx', index=False)
# df_oc.to_excel('oc.xlsx', index=False)
