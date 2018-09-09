import pprint

data = [
'Buyer Relationship and Insight', 'Pursuit Team Readiness', 'Third Party Advisor', 'Win Themes and Differentiation',
'Buyer Relationship and Insight', 'Client Intent to Buy', 'Pursuit Team Readiness', 'Third Party Advisor',
'Buyer Relationship and Insight', 'Client Intent to Buy', 'Pursuit Team Readiness', 'Third Party Advisor', 'Win Themes and Differentiation',
'Buyer Relationship and Insight', 'Pursuit Team Readiness', 'Relevant Past Performances', 'Third Party Advisor', 'Win Themes and Differentiation',
'Buyer Relationship and Insight', 'Client Intent to Buy', 'Pursuit Team Readiness', 'Relevant Past Performances', 'Third Party Advisor', 'Win Themes and Differentiation',
'Buyer Relationship and Insight', 'Client Intent to Buy', 'Partner Strategy', 'Pursuit Team Readiness', 'Third Party Advisor', 'Win Themes and Differentiation',
'Buyer Relationship and Insight', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor',
'Buyer Relationship and Insight', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor', 'Win Themes and Differentiation',
'Buyer Relationship and Insight', 'Client Intent to Buy', 'Partner Strategy', 'Pursuit Team Readiness', 'Relevant Past Performances', 'Third Party Advisor', 'Win Themes and Differentiation',
'Buyer Relationship and Insight', 'Client Intent to Buy', 'Delivery Leadership Team', 'Pursuit Team Readiness', 'Relevant Past Performances', 'Third Party Advisor', 'Win Themes and Differentiation',
'Buyer Relationship and Insight', 'Delivery Leadership Team', 'Partner Strategy', 'Solution', 'Third Party Advisor', 'Win Themes and Differentiation',
'Bid Management Approach', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor',
'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor',
'Bid Management Approach', 'Delivery Leadership Team', 'Partner Strategy', 'Risk Profile', 'Third Party Advisor',
'Bid Management Approach', 'Buyer Relationship and Insight', 'Delivery Leadership Team', 'Partner Strategy', 'Risk Profile', 'Solution', 'Third Party Advisor',
'Bid Management Approach', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Third Party Advisor',
'Bid Management Approach', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Risk Profile', 'Third Party Advisor',
'Bid Management Approach', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Solution', 'Third Party Advisor',
'Bid Management Approach', 'Buyer Relationship and Insight', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Solution', 'Third Party Advisor',
'Bid Management Approach', 'Cost, Pricing, & Deal Shaping', 'Delivery Leadership Team', 'Partner Strategy', 'Risk Profile', 'Solution', 'Third Party Advisor',

]


dict_result = dict()

for csf in data:
    try:
        dict_result[csf] +=1
    except:
        dict_result[csf] = 1

d_view = [ (v,k) for k,v in dict_result.items() ]
d_view.sort(reverse=True) # natively sort tuples by first element
for v,k in d_view:
    print("%s \t %d" % (k,v))