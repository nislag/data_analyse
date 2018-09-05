import pandas as pd

# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('SPO_UPDATED_WITHOUT_GREY.csv', index_col=None, sep='\t')

print('all', len(df_all))
main_data = ['SPO4__CSF__C', 'SPO4__OUTCOME__C']

rename_dict = {'SPO4__PLAYBOOK_NAME__C': 'PlayBook', 'SPO4__OUTCOME_STAGE__C': 'Stage','SPO4__CSF__C': 'CSF', 'SPO4__OUTCOME__C': 'Outcome'}

writer = pd.ExcelWriter('cts_data_analise_without_grey.xlsx', engine='xlsxwriter')
for x in main_data:
    df_book_with_csf = df_all[['SPO4__PLAYBOOK_NAME__C', 'SPO4__OUTCOME_STAGE__C', x , 'LAST_STAGE', 'SPO4__COLOR__C', 'SPO4__CHANGE_DATE__C']].groupby(['SPO4__PLAYBOOK_NAME__C', 'SPO4__OUTCOME_STAGE__C', x , 'SPO4__COLOR__C','LAST_STAGE']).agg(['count'])
    print('opo+out', len(df_book_with_csf))
    # print(df_book_with_csf)

    df_book_with_csf.reset_index(inplace=True)
    # print(df_book_with_csf.to_string())
    # df_book_with_csf.to_excel('df_book_with_csf.xlsx')

    # play_books = list(set(df_all['SPO4__PLAYBOOK_NAME__C'].values.tolist()))
    # stages = list(set(df_all['LAST_STAGE'].values.tolist()))
    # colors = list(set(df_all['SPO4__COLOR__C'].values.tolist()))
    # csfs = list(set(df_all[x].values.tolist()))
    # outcomes = list(set(df_all['SPO4__OUTCOME__C'].values.tolist()))
    #
    # print(play_books)
    # print(colors)
    #
    # list_pb_csf = []
    # list_cs_csf = []
    # list_for_num = []
    #
    # for pb in play_books:
    #     for cs in csfs:
    #         list_pb_csf.append(pb)
    #         list_cs_csf.append(cs)
    #         list_for_num.append(0)

    named_columns = ['SPO4__PLAYBOOK_NAME__C', 'SPO4__OUTCOME_STAGE__C', x]
    df_csf = df_all.drop_duplicates(subset=named_columns)[named_columns]
    df_csf.sort_values(named_columns, inplace=True)

    df_csf['green'] = 0
    df_csf['red'] = 0
    df_csf['grey'] = 0
    df_csf['Won'] = 0
    df_csf['Lost'] = 0
    df_csf['Won_green'] = 0
    df_csf['Lost_red'] = 0
    # df_csf['Open'] = list_st_on_csf


    df_csf['ind'] = df_csf[named_columns].apply(lambda x: ''.join(x), axis=1)
    df_csf.set_index('ind', inplace=True)
    # print(df_csf.to_string())
    # continue
    for i, row in df_book_with_csf.iterrows():
        # print(row)
        pl = row['SPO4__PLAYBOOK_NAME__C']
        os = row['SPO4__OUTCOME_STAGE__C']
        st = row['LAST_STAGE']
        cl = row['SPO4__COLOR__C']
        os = row['SPO4__OUTCOME_STAGE__C']
        cs = row[x]
        num = row['SPO4__CHANGE_DATE__C']['count']
        ind_cs = pl + os + cs
        print(ind_cs)
        df_csf.loc[ind_cs, cl] += num
        df_csf.loc[ind_cs, st] += num
        if (st.item() == 'Won' and cl.item() == 'green') or (st.item() == 'Lost' and cl.item() == 'red'):
            df_csf.loc[ind_cs, st + '_' +cl] += num

    # df_csf['part_green/(green+red+grey)%'] = (df_csf['green'] * 100.0)/(df_csf['green'] + df_csf['grey'] + df_csf['red'])
    # df_csf['part_won/(won+lost) %'] = (df_csf['Won'] * 100.0)/(df_csf['Won'] + df_csf['Lost'])
    df_csf.fillna(0, inplace=True)

    df_csf.rename(index=str, columns=rename_dict, inplace=True)
    print(df_csf)
    df_csf.to_excel(writer, sheet_name=x[6:-3], index=False)

writer.save()
#
#
# df_csf.to_excel('csf.xlsx', index=False)
# df_oc.to_excel('oc.xlsx', index=False)