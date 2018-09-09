import pandas as pd
import itertools
import time


class class_df_check():

    def __init__(self):
        self.csf_missed = 0
        self.comb_num = 0
        self.min_size_combinations = 4
        self.max_size_combinations = 7
        self.result_dict = {
            'size_combination': [],
            'combination': [],
        }

    #  df_won, df_lost,
    def recursive_df_check(self, size_combination, cur_step , csf_list, combination, df_won, df_lost):
        filtered_df_won = filtered_df_lost = pd.DataFrame()
        if cur_step == size_combination:
            if self.start:
                combination_name = str(combination[1:])[1:-1]
                self.result_dict['size_combination'].append(size_combination)
                self.result_dict['combination'].append(combination_name)
            else:
                self.result_dict[self.name_group + '_Won_green'].append(len(df_won))
                self.result_dict[self.name_group + '_Lost_red'].append(len(df_lost))
            self.comb_num +=1
            # print(combination_name)
            return

        for i in range(len(csf_list)):
            csf = csf_list[i]
            new_combination = combination.copy()
            new_combination.append(csf)
            new_csf_list = csf_list[i+1:]
            if len(new_csf_list) < size_combination - 1 - cur_step:
                return

            if not self.start:
                try:
                    filtered_df_won = df_won[df_won[csf] == 1]
                except:
                    self.csf_missed +=1

                try:
                    filtered_df_lost = df_lost[df_lost[csf] == -1]
                except:
                    self.csf_missed += 1

            self.recursive_df_check(size_combination, cur_step+1, new_csf_list, new_combination, filtered_df_won, filtered_df_lost)

    def check(self, start, name_group = '' , df = pd.DataFrame()):
        if not start:
            df_won = df[df['OPPORTUNITY_WON__C'] == 'Won']
            df_lost = df[df['OPPORTUNITY_WON__C'] == 'Lost']
        else:
            df_won = df_lost = pd.DataFrame()
        self.start = start
        self.name_group = name_group
        time_start = time.time()
        for size_combination in range(self.min_size_combinations, self.max_size_combinations + 1):
            print(size_combination)
            check.recursive_df_check(size_combination, 0, csfs, [size_combination], df_won, df_lost)
            print(check.comb_num)
            check.comb_num = 0

        print(time.time() - time_start)


# df_all = pd.DataFrame.from_csv('SPO_UP_50000.csv', index_col=None, sep='\t')
df_all = pd.DataFrame.from_csv('SPO_UPDATED.csv', index_col=None, sep='\t')

# df_book_with_csf = df_all[['SPO4__OUTCOME_STAGE__C', 'SPO4__CSF__C', 'SPO4__OUTCOME__C','SPO4__CHANGE_DATE__C']].groupby(['SPO4__OUTCOME_STAGE__C', 'SPO4__CSF__C', 'SPO4__OUTCOME__C',]).agg(['count'])
# print(df_book_with_csf.to_string())

df_all = df_all[(df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal >$50M >$25M CE/UKI or >$10M APAC/LATAM/MEA')
                | (df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal $10-50M $10-25M CE/UKI or $5-10M APAC/LATAM/MEA')
                | (df_all['SPO4__PLAYBOOK_NAME__C'] == 'Competitive deal $2-10M or $2-5M APAC/LATAM/MEA')
]


csfs = list(set(df_all['SPO4__CSF__C'].drop_duplicates()))
csfs.sort()

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

# min_size_combinations = 4
# max_size_combinations = 7
check = class_df_check()
check.check(True)
for group in groups:
    name_group = "_".join(group)
    df_group = pd.DataFrame.from_csv('csf_data_sets\csf_{}.csv'.format(name_group), sep='\t')
    print('\n')
    print('!!!Group!!!')
    print(name_group)
    # print(df_group)
    #
    check.result_dict[name_group + '_Won_green'] = []
    check.result_dict[name_group + '_Lost_red'] = []
    #
    #
    # time_start = time.time()
    # for size_combination in range(min_size_combinations, max_size_combinations+1):
    #     print(size_combination)
    #     check.recursive_df_check(size_combination, 0, csfs, [size_combination])
    #
    #     # for subset in itertools.combinations(csfs, size_combination):
    #     #     combination = str(subset)[1:-1]
    #     #     result_dict['size_combination'].append(size_combination)
    #     #     result_dict['combination'].append(combination)
    #         # print(combination)
    #         # comb_num+=1
    #     print(check.comb_num)
    #     check.comb_num = 0
    #
    # print(time.time() - time_start)
    check.check(False, name_group, df_group)

df_result = pd.DataFrame(check.result_dict)
df_result.set_index('combination', inplace=True)
print(df_result)
    #

print(check.csf_missed)

df_result.to_csv('csf_data_sets\csf_combinations_{}_to_{}_result.csv'.format(check.min_size_combinations, check.max_size_combinations), index=True,sep='\t')

