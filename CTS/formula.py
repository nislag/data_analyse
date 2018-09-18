import string


list_letters= list(string.ascii_uppercase)

print(list_letters)

list_columns = []

current_first_letter = ''
current_first_letter_num = -1
num_lists = 3

for num_list in range(num_lists):
    for letter in list_letters:
        list_columns.append(current_first_letter+letter)

    current_first_letter_num+=1
    current_first_letter = list_letters[current_first_letter_num]


num_first_columns = 2
num_first_rows = 3
num_outcomes = 36

print(list_columns[num_first_columns:num_outcomes+num_first_columns])

formula_start = '=FILTER('

formula_won_with_use = formula_start+ 'Data!2:5824,Data!B2:B5824 = "Won"'
formula_lost_with_use = formula_start+ 'Data!2:5824,Data!B2:B5824 = "Lost"'

print(formula_won_with_use)
for i in range(0,num_outcomes):
    col = list_columns[num_first_columns+i]
    row = str(num_first_rows+i+1)
    text_won = ',Data!'+col +'2:'+col+ '5824 <=IF(Competetive2!D' + row + ' = "Yes",Competetive2!C' + row + ',1)'
    text_lost= ',Data!' + col + '2:' + col + '5824 >=IF(Competetive2!D' + row + ' = "Yes",Competetive2!C' + row + ',-1)'
    # print(text)
    formula_won_with_use +=text_won
    formula_lost_with_use +=text_lost

formula_won_with_use+=')'
formula_lost_with_use+=')'
print('Won: ', formula_won_with_use)
print('Lost: ', formula_lost_with_use)