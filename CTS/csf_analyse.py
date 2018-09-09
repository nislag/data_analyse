import pandas as pd

# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('csf_data_sets\csf_combinations_4_to_7_result.csv', sep='\t')

# print(df_all)
group_check  = '3_4'

dict_result = dict()
df_result = pd.DataFrame()
parts = ['Won_green', 'Lost_red', 'res']

min_size = 4
max_size = 7

top_to_check = 3


for size in range(min_size, max_size+1):
    df_by_size = df_all[df_all['size_combination'] == size]
    df_by_size[group_check + '_res'] = df_by_size[group_check + '_'+'Won_green'] + df_by_size[group_check + '_'+'Lost_red']
    for part in parts:
        # df_by_size.reset_index(inplace=True)
        df_by_size.sort_values(by=[group_check + '_' + part], ascending=False, inplace=True)

        df_part = df_by_size[:top_to_check]

        comment = str(size)+'s' + '_' + group_check + '_' + part
        comment = str(comment)
        df_part['comment'] = comment
        # print(df_part.tos)
        df_result = df_result.append(df_part)

        for combination in df_part.index.values.tolist():
            comb = str(combination)
            # print(comb, comment)
            try:
                dict_result[comb] = str(dict_result[comb]) + ',' + comment
            except:
                dict_result[comb] = comment
        # print(df_part)

# print(dict_result)

# print(df_result)


combinations = dict_result.keys()
data = []
for combination in combinations:
    # print(combination)
    comb = combination.split("', '")
    # comb = combination.replace("'", "")
    # comb = comb.split(", ")
    # print(type(comb))
    data.extend(comb)

dict_num = dict()

for item in data:
    csf = item.replace("'", "")
    print(csf)
    try:
        dict_num[csf] +=1
    except:
        dict_num[csf] = 1

dict_analyse = {'csf': [], 'number_from_top_{}'.format(top_to_check):[]}

for key,value in dict_num.items():
    dict_analyse['csf'].append(key)
    dict_analyse['number_from_top_{}'.format(top_to_check)].append(value)

df_analyse = pd.DataFrame(dict_analyse)
df_analyse.sort_values(by=['number_from_top_{}'.format(top_to_check)], ascending=False, inplace=True)

writer = pd.ExcelWriter('csf_data_sets\csf_analyse_{}.xlsx'.format(group_check), engine='xlsxwriter')

df_result.to_excel(writer, sheet_name='data', index=True)
df_analyse.to_excel(writer, sheet_name='analyse', index=False)

writer.save()



# df_all = df_all[(df_all['SPO4__OUTCOME_STAGE__C'] == '1. Engagement')
#                 | (df_all['SPO4__OUTCOME_STAGE__C'] == '2. Shaping')
# ]
# df_all = df_all[(df_all['SPO4__OPPORTUNITY__C'] == '0066100000F5C9NAAV')
# ]
#
#
# df_all = df_all[(df_all['SPO4__CSF__C'] == 'Buyer Relationship and Insight')
#                 | (df_all['SPO4__CSF__C'] == 'Client Intent to Buy')
#                 | (df_all['SPO4__CSF__C'] == 'Pursuit Team Readiness')
#                 | (df_all['SPO4__CSF__C'] == 'Win Themes and Differentiation')
# ]
#
# df_all.to_csv('t.csv')


# 1
# 2
# 3
# 4
# 5
# 1, 2
# 3, 4
# 3, 4, 5
# 1, 2, 3, 4
# 1, 2, 3, 4, 5