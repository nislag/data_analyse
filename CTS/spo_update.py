import pandas as pd

df_all = pd.DataFrame.from_csv('9_12_CompleteJoinedData.csv', index_col=None)

# print(df_all)
df_all.fillna(0, inplace=True)

data_dict = dict()

# for col in df_all.columns.values.tolist():
#     if col not in not_drop_col:
#         print(col)

drop_col = [
'Unnamed: 0',
'ID',
'ISDELETED',
'NAME',
'CURRENCYISOCODE',
'CREATEDBYID',
'LASTMODIFIEDDATE',
'LASTMODIFIEDBYID',
'CREATEDDATE',
'SYSTEMMODSTAMP',
'SPO4__OPPORTUNITY_PLAYBOOK__C',
'SPO4__PERCENT__C',
'SPO4__SPOOPPORTUNITY__C',
'Deal_Size__c',
'Account_Tagging__c',
'Practice_Area__c,'
'Vertical__c',
'Status__c',
'Type',

]

# "OPPORTUNITY_CLOSED__C","OPPORTUNITY_WON__C"

df_all.drop(drop_col, inplace=True, axis=1, errors='ignore')

print('basis df', len(df_all))

df_all.SPO4__COLOR__C.replace(['exclamation'], ['grey'], inplace=True)
df_all.SPO4__CSF_CATEGORY__C.replace(['Is It Real?'], ['Can We Win?'], inplace=True)
df_update = df_all[df_all['SPO4__PLAYBOOK_NAME__C'] !=0]
df_update = df_update[df_update['SPO4__CSF__C'] !='Trizetto Engagement']
df_update.reset_index(inplace=True)
del df_update['index']
print('removed playbook 0',len(df_update))

# df_update['COLOR_NUM'] = df_update['SPO4__COLOR__C']
# df_update.COLOR_NUM.replace(['green', 'grey', 'red'], [1, 0, -1], inplace=True)
#
# df_update['LAST_STAGE'] = df_update['SPO4__OPPORTUNITY_STAGE__C']
# df_update.LAST_STAGE.replace([
#                     '1. Engagement',
#                     '2. Shaping',
#                     '3. Solutioning',
#                     '4. End-Game',
#                     '5. Negotiation',
#                     'Cognizant Withdraw',
#                     'Lost',
#                     'Duplicate',
#                     'Client Withdraw',
#                     'Won',
#                     ], [
#                     'Open',
#                     'Open',
#                     'Open',
#                     'Open',
#                     'Open',
#                     'Lost',
#                     'Lost',
#                     'Lost',
#                     'Lost',
#                     'Won',
#                     ], inplace=True)

df_update = df_update[df_update['OPPORTUNITY_CLOSED__C'] != False]
print('removed Open ',len(df_update))
df_update.OPPORTUNITY_WON__C.replace([True, False], ['Won', 'Lost'], inplace=True)
# print(df_update)




df_update_50000 = df_update[:50000]
df_update_50000.to_csv('9_12\SPO_9_12_UP_50000.csv', sep='\t', index=False)

df_update.to_csv('9_12\SPO_9_12_UPDATED.csv', sep='\t', index=False)

df_update = df_update[df_update['SPO4__COLOR__C'] !='grey']
print('removed Grey ',len(df_update))

df_update.to_csv('9_12\SPO_9_12_UPDATED_WITHOUT_GREY.csv', sep='\t', index=False)
# df_500_part = pd.DataFrame()
# for i in range(len(df_update)):
#     if (i%500)==0:
#         # print(i)
#         # print(df_all.loc[i])
#         df_500_part = df_500_part.append(df_update.loc[i])

# df_500_part.to_csv('SPO_UP_500.csv', sep='\t')

# print('SPO4__PLAYBOOK_NAME__C', set(df_update['SPO4__PLAYBOOK_NAME__C'].values.tolist()))

# list_opo = list(set(df_update['SPO4__OPPORTUNITY__C'].values.tolist()))

# win_opo = []
# lost_opo = []
# open_opo = []

# df_opo_with_stages = df_update.drop_duplicates(subset=['SPO4__OPPORTUNITY__C', 'SPO4__OPPORTUNITY_STAGE__C'])
# print(df_opo_with_stages[:1000].to_string())

# for opo in list_opo:
#     df = df_opo_with_stages[df_opo_with_stages['SPO4__OPPORTUNITY__C'] == opo]
#     stages = df['SPO4__OPPORTUNITY_STAGE__C'].values.tolist()
#     for stage in stages:
#         if 'Win' or 'Won' in stage:
#             win_opo.append(opo)
#         elif '1' or '2' or '3' or '4' or '5' in stages:
#             open_opo.append(opo)
#         else:
#             lost_opo.append(opo)
#
# print('won', len(win_opo))
# print('lost', len(lost_opo))
# print('open', len(open_opo))


