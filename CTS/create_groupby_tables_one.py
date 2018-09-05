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

writer = pd.ExcelWriter('cts_data_analise_without_grey.xlsx', engine='xlsxwriter')
group_columns = ['SPO4__PLAYBOOK_NAME__C', 'SPO4__OUTCOME_STAGE__C', 'SPO4__CSF_CATEGORY__C', 'SPO4__CSF__C', 'SPO4__OUTCOME__C', 'OPPORTUNITY_WON__C', 'SPO4__COLOR__C']
copy_group_columns= group_columns.copy()
copy_group_columns.append('SPO4__CHANGE_DATE__C')
print(copy_group_columns)
df_book_with_csf = df_all[copy_group_columns].groupby(group_columns).agg(['count'])
print('opo+out', len(df_book_with_csf))
# print(df_book_with_csf)

df_book_with_csf.reset_index(inplace=True)


named_columns = ['SPO4__PLAYBOOK_NAME__C',
                 'SPO4__OUTCOME_STAGE__C',
                 'SPO4__CSF_CATEGORY__C',
                 'SPO4__CSF__C',
                 'SPO4__OUTCOME__C',
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
    cl = row['SPO4__COLOR__C'].values[0]
    # cc = row['SPO4__CSF_CATEGORY__C']
    # cs = row['SPO4__CSF__C']
    # oc = row['SPO4__OUTCOME__C']

    num = row['SPO4__CHANGE_DATE__C']['count']
    data_val = [row[x].values[0] for x in named_columns]
    # print(data_val)
    ind_cs = ''.join(data_val)
    # print(st, cl)
    df_csf.loc[ind_cs, cl] += num
    df_csf.loc[ind_cs, st] += num

    if (st == 'Won' and cl == 'green') or (st == 'Lost' and cl == 'red'):
        df_csf.loc[ind_cs, st + '_' + cl] += num

# df_csf['part_green/(green+red+grey)%'] = (df_csf['green'] * 100.0)/(df_csf['green'] + df_csf['grey'] + df_csf['red'])
# df_csf['part_won/(won+lost) %'] = (df_csf['Won'] * 100.0)/(df_csf['Won'] + df_csf['Lost'])
# df_csf.fillna(0, inplace=True)

# print(df_csf)
df_csf.rename(index=str, columns=rename_dict, inplace=True)
print(df_csf)
df_csf.to_excel(writer, sheet_name='data', index=False)

writer.save()
#
#
# df_csf.to_excel('csf.xlsx', index=False)
# df_oc.to_excel('oc.xlsx', index=False)

bytearray(b'{"definition":{"tournament_id":211418,"is_branded":true,"booster_mode":1,"is_tutorial":false,"is_advanced":false,"validating_results":false,"version":27,"title":"STR_TOURNAMENT_211418_TITLE","description":"STR_TOURNAMENT_211418_DESC","start_date":"2018-08-29 22:00:00","end_date":"2018-09-05 22:00:00","priority":1,"image":{"default":"tournament_110406_banner_3"},"background_color":"#FFB60000","booster_ad_asset":{"default":"fair_10_default"},"font_color":"#13131300","country_filter":{"include":["FR"]},"rewards":[{"prize_data":[{"car_tuning_state":"STOCK","car_id":81,"type":"car"},{"credit_amount":100000,"type":"credits"}],"conditions":[{"type":"leaderboard_at_least_in_position","value":3,"affected_events":"ANY"}]},{"prize_data":[{"hard_currency_amount":300,"type":"hard_currency"}],"conditions":[{"type":"leaderboard_at_least_in_position","value":100,"affected_events":"ANY"}]},{"prize_data":[{"card_box_amount":2,"card_box_id":24,"type":"card_box"}],"conditions":[{"type":"leaderboard_at_least_in_position","value":500,"affected_events":"ANY"}]},{"prize_data":[{"credit_amount":30000,"type":"credits"}],"conditions":[{"type":"leaderboard_at_least_in_position","value":3000,"affected_events":"ANY"}]},{"prize_data":[{"boost_amount":2,"boost_type":"NITRO","type":"booster"}],"conditions":[{"type":"leaderboard_at_least_in_position","value":5000,"affected_events":"ANY"}]},{"prize_data":[{"card_box_amount":1,"card_box_id":50,"type":"card_box"}],"conditions":[{"type":"race_time_under_value","value":65000,"affected_events":"ANY"}]},{"prize_data":[{"hard_currency_amount":25,"type":"hard_currency"}],"conditions":[{"type":"finish_race_at_least_in_position","value":1,"affected_events":"ANY"}]},{"prize_data":[{"boost_amount":1,"boost_type":"PERFORMANCE","type":"booster"}],"conditions":[{"type":"finish_race_at_least_in_position","value":3,"affected_events":"ANY"}]},{"prize_data":[{"hard_currency_amount":10,"type":"hard_currency"}],"conditions":[{"type":"finish_race","affected_events":"ANY"}]}],"events":[{"event_id":234564,"title":"","image":{"default":""},"start_date":"2018-08-29 22:00:00","end_date":"2018-09-05 22:00:00","location":"TENERIFE_TRACK","game_mode":"Normal","game_mode_modification":"NONE","type":"timeAttackSP","forced_billboard_asset":"","energy_price":1,"grace_period":600}]},"localization_data":{"STR_TOURNAMENT_211418_TITLE":{"ar":"ORANGE ASPHALT CUP","de":"ORANGE ASPHALT CUP","en":"ORANGE ASPHALT CUP","es":"ORANGE ASPHALT CUP","fr":"ORANGE ASPHALT CUP","id":"ORANGE ASPHALT CUP","it":"ORANGE ASPHALT CUP","ja":"ORANGE ASPHALT CUP","ko":"ORANGE ASPHALT CUP","pt":"ORANGE ASPHALT CUP","ru":"ORANGE ASPHALT CUP","th":"ORANGE ASPHALT CUP","tr":"ORANGE ASPHALT CUP","zh":"ORANGE ASPHALT CUP","zh_hant":"ORANGE ASPHALT CUP"},"STR_TOURNAMENT_211418_DESC":{"ar":"NOT USED","de":"NOT USED","en":"NOT USED","es":"NOT USED","fr":"NOT USED","id":"NOT USED","it":"NOT USED","ja":"NOT USED","ko":"NOT USED","pt":"NOT USED","ru":"NOT USED","th":"NOT USED","tr":"NOT USED","zh":"NOT USED","zh_hant":"NOT USED"},"STR_MENU_PROKITS_PROBOX_302_DESCRIPTION":{"en":"Grants 3 cards for the McLaren MP4/8!","fr":"Donne 3 cartes pour la McLaren MP4/8 !","de":"Enth\xc3\xa4lt 3 Karten f\xc3\xbcr den McLaren MP4/8!","it":"Offre 3 carte per la McLaren MP4/8!","es":"\xc2\xa1Contiene 3 cartas para el McLaren MP4/8!","ja":"McLaren MP4/8|\xe5\x90\x91\x00\xe3\x81\x91|\xe3\x82\xab\xe3\x00\x83\xbc\xe3\x83\x00\x89\xe3\x81\x8c\x00|3\xe6\x9e\x00\x9a|\xe5\xb0\x00\x81\xe5\x85\xa5\x00","pt":"Garante 3 cartas para McLaren MP4/8!","ko":"McLaren MP4/8 \xea\xb4\x00\x80\xeb\xa0\xa8\x00 \xec\xb9\xb4\x00\xeb\x93\x9c 3\xec\x9e\xa5\x00\xec\x9d\x84 \xec\xa4\x8d\xeb\x00\x8b\x88\xeb\x8b\x00\xa4!","zh":"\xe5\x86\x00\x85\xe6\x9c\x89\x003\xe5\xbc\xa0\x00\xe7\x94\xa8\xe4\x00\xba\x8eMcLaren MP4/8\xe7\x00\x9a\x84\xe5\x8d\x00\xa1\xe7\x89\x8c\x00\xef\xbc\x81","ru":"\xd0\x00\xa1\xd0\xbe\xd0\x00\xb4\xd0\xb5\xd1\x00\x80\xd0\xb6\xd0\x00\xb8\xd1\x82 3 \xd0\xba\x00\xd0\xb0\xd1\x80\x00\xd1\x82\xd1\x8b\x00 \xd0\xb4\xd0\x00\xbb\xd1\x8f McLaren MP4/8!","tr":"McLaren MP4/8 i\xc3\xa7in 3 kart kazand\xc4\x00\xb1r\xc4\xb1\x00r!","ar":"Grants 3 cards for the McLaren MP4/8!","th":"\xe0\x00\xb9\x83\xe0\xb8\x00\xab\xe0\xb9\x89\x00|\xe0\xb8\x81\x00\xe0\xb8\xb2\xe0\x00\xb8\xa3\xe0\xb9\x00\x8c\xe0\xb8\x94\x00 |3 |\xe0\xb9\x83\x00\xe0\xb8\x9a|\xe0\xb8\xaa\xe0\x00\xb8\xb3\xe0\xb8\x00\xab\xe0\xb8\xa3\x00\xe0\xb8\xb1\xe0\x00\xb8\x9a |McLaren MP4/8!","zh_hant":"\xe7\x00\xb5\xa6\xe4\xba\x00\x883\xe5\xbc\x00\xb5\xe7\x94\xa8\x00\xe6\x96\xbc McLaren MP4/8 \xe7\x9a\x00\x84\xe5\x8d\xa1\x00\xe7\x89\x8c\xef\x00\xbc\x81","id":"Memberikan 3 kartu untuk McLaren MP4/8!"}},"events_data":[{"event_id":234564,"location":"TENERIFE_TRACK","forced_billboard_asset":"","event_def":["EventDef_Ten_04_Reverse"],"game_mode":"Normal","game_mode_modification":"NONE","gm_param_1":1,"gm_param_2":0,"gm_param_3":0,"gm_param_4":0,"gm_param_5":0,"racers":1,"traffic":false,"ghost":true,"worst_race_time_to_submit_ghost":61000,"min_lb_position_to_submit_ghost":500,"maxed":false,"extra":0,"car_filter_for_player":"CarFilter_Individual_Koenigsegg_One1","worst_time_delta_percent":30,"delta_1_best":2,"delta_1_worst":2,"delta_2nd_to_1st":1,"delta_3rd_to_1st":3,"rank_delta_points":50,"rubber_band_delta_time_1st":3,"rank":1768,"car_filter_for_ai":"CarFilter_Individual_Koenigsegg_One1","best_allowed_race_time":41000,"decal_id_for_car_filter_for_player":"-1","decal_id_for_car_filter_for_ai":"-1","car_rental":[{"car_id":81,"forced_rental_decal_id":-1,"car_tuning_state":"PRO_MAXED","rent_price":0,"forced_rental":true}],"condition_for_score_3":{"condition_type":"POSITION_IN_LEADERBOARD","condition_value":1000},"condition_for_score_2":{"condition_type":"POSITION_IN_LEADERBOARD","condition_value":10000},"condition_for_score_1":{"condition_type":"POSITION_IN_LEADERBOARD","condition_value":50000}}]}')