from pprint import pprint
import pandas as pd


df_all = pd.DataFrame.from_csv('9_12_CompleteJoinedData.csv', index_col=None)

# print('all', len(df_all))
#
# # df_new_logo = df_all[df_all['Customer_Category__c'] == 'Prospect']
# df_new_logo = df_all
# print('new_logo', len(df_new_logo))
# df_new_logo = df_new_logo[df_new_logo['OPPORTUNITY_CLOSED__C'] == True]
# print('new_logo clossed', len(df_new_logo))
# df_new_logo.OPPORTUNITY_WON__C.replace([True, False], ['Won', 'Lost'], inplace=True)
#
# named_columns = ['SPO4__PLAYBOOK_NAME__C',
#                  'Customer_Category__c',
#                  'OPPORTUNITY_WON__C',
#                  ]
#
# group_columns = named_columns.copy()
# group_columns.append('SPO4__OPPORTUNITY__C')
# copy_group_columns = group_columns.copy()
# copy_group_columns.append('CURRENCYISOCODE')
#
# df_calc = df_new_logo[copy_group_columns].groupby(group_columns).agg(['count'])
#
# df_calc.fillna(0,inplace=True)
#
# df_calc.reset_index(inplace=True)
#
# # df_calc.to_csv('new_logo_count_opo.csv')
# # df_calc = df_calc[named_columns].groupby(by= ['SPO4__PLAYBOOK_NAME__C'], group_keys = True).agg(['count'])
# # df_calc.reset_index(inplace=True)
#
# df_calc = df_calc.pivot_table(values='SPO4__OPPORTUNITY__C',index=['SPO4__PLAYBOOK_NAME__C'],columns=['OPPORTUNITY_WON__C', 'Customer_Category__c'],aggfunc='count')
# # print(df_calc)
# df_calc.to_csv('all_count.csv')
# df_calc.to_csv('new_logo_count.csv')

# data = [
# 'Buyer Relationship and Insight', 'Pursuit Team Readiness', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Buyer Relationship and Insight', 'Client Intent to Buy', 'Pursuit Team Readiness', 'Third Party Advisor',
# 'Buyer Relationship and Insight', 'Client Intent to Buy', 'Pursuit Team Readiness', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Buyer Relationship and Insight', 'Pursuit Team Readiness', 'Relevant Past Performances', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Buyer Relationship and Insight', 'Client Intent to Buy', 'Pursuit Team Readiness', 'Relevant Past Performances', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Buyer Relationship and Insight', 'Client Intent to Buy', 'Partner Strategy', 'Pursuit Team Readiness', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Buyer Relationship and Insight', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor',
# 'Buyer Relationship and Insight', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Buyer Relationship and Insight', 'Client Intent to Buy', 'Partner Strategy', 'Pursuit Team Readiness', 'Relevant Past Performances', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Buyer Relationship and Insight', 'Client Intent to Buy', 'Delivery Leadership Team', 'Pursuit Team Readiness', 'Relevant Past Performances', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Buyer Relationship and Insight', 'Delivery Leadership Team', 'Partner Strategy', 'Solution', 'Third Party Advisor', 'Win Themes and Differentiation',
# 'Bid Management Approach', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor',
# 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor',
# 'Bid Management Approach', 'Delivery Leadership Team', 'Partner Strategy', 'Risk Profile', 'Third Party Advisor',
# 'Bid Management Approach', 'Buyer Relationship and Insight', 'Delivery Leadership Team', 'Partner Strategy', 'Risk Profile', 'Solution', 'Third Party Advisor',
# 'Bid Management Approach', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor',
# 'Bid Management Approach', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Risk Profile', 'Third Party Advisor',
# 'Bid Management Approach', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Solution', 'Third Party Advisor',
# 'Bid Management Approach', 'Buyer Relationship and Insight', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Solution', 'Third Party Advisor',
# 'Bid Management Approach', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Risk Profile', 'Solution', 'Third Party Advisor',
#
# ]
#
#
# dict_result = dict()
#
# for csf in data:
#     try:
#         dict_result[csf] +=1
#     except:
#         dict_result[csf] = 1
#
# d_view = [ (v,k) for k,v in dict_result.items() ]
# d_view.sort(reverse=True) # natively sort tuples by first element
# for v,k in d_view:
#     print("%s \t %d" % (k,v))





# check columns
# print(df_all)
# # df_all.fillna(0, inplace=True)
#
# df_result = pd.DataFrame()
# data_dict = dict()
i =0
for col in df_all.columns.values.tolist():
    print(i, col)
    i+=1
#     values = (df_all[col].values.tolist())
#     dict_values = dict()
#     for item in values:
#         try:
#             dict_values[item]+=1
#         except:
#             dict_values[item] = 1
#
#         if len(dict_values) > 1000:
#             break
#
#     values= list(dict_values.keys())
#     # print(len(values))
#     if len(values) < 1000:
#         pprint(dict_values)
#         try:
#             values.sort()
#         except:
#             print('dif data')
#         values.extend(['']*(1001-len(values)))
#         df_result[col] = values
#
# print(df_result)
# df_result.to_csv('values.csv', sep='\t')