# I am going to give up and do the
# #"assume you get every possible combination of rolls and add them up" thing instead.

# What is the chance that
    # k dice with
    # M sides each(INCLUDING ZERO)
    # add up to H exactly 

k = 2
m = 7   # seven sided die {0,1,2,3,4,5,6}
h = 7

'''
for i in range(1,k+1):
    print(i)
d'''
frequencies = {}
def sum_dice(dice_count, side_count, running_total = 0):
    if dice_count == 0:
        frequencies[running_total] = frequencies.setdefault(running_total, 0) + 1
        #print( "Base Case Reached with running total = " + str(running_total))
        return
    #print("dice left: " + str(dice_count))
    for outcome in range(side_count):
        #print("adding outcome of " + str(outcome) + " for die number : " + str(dice_count))
        sum_dice(dice_count - 1, side_count, running_total + outcome)
        print("Dice Left: " + str(dice_count))


final_hit_freq = {}
def final_hit_calc(hp, side_count, previous_hit = 0, total_damage = 0):
    if total_damage >= hp:
        killing_blow = previous_hit - (total_damage - hp)
        final_hit_freq[killing_blow] = final_hit_freq.setdefault(killing_blow, 0) + 1
        print(final_hit_freq.values())
        return
    for outcome in range(1, side_count + 1):
        #print("Damage =  " + str(outcome))
        final_hit_calc(hp , side_count, outcome, total_damage + outcome)
        #print("Damage Done: " + str(outcome + total_damage))

# a version of final_hit_calc that uses memoization to reduce computation time
    # When we call a return, we add the return value to a dictionary, with the total_damage as the key
memos = {}
def m_final_hit_calc(hp, side_count, previous_hit = 0, total_damage = 0):
    # Base Case: You've killed the monster (total damage > hp)
    if total_damage >= hp:
        killing_blow = previous_hit - (total_damage - hp)
        new_dict = {killing_blow: 1}
        return new_dict
    # Common Case 1: Check to see if you've done this calculation already
    if total_damage in memos:
        return memos[total_damage]
    # Common Case 2: Do the actual calculation
    result_dict = {}
    for outcome in range(1, side_count + 1):
        dict2 = m_final_hit_calc(hp, side_count, outcome, total_damage + outcome)
        result_dict = add_dictionary_values(result_dict, dict2)
        # if result_dict[1] % 100000 == 0:
            # print(result_dict)
    memos[total_damage] = result_dict
    return result_dict
# adds the values stored in two dictionaries together, and returns a new dictionary with the sums
def add_dictionary_values(dict1, dict2):
    for key in dict2:
        dict1[key] = dict1.setdefault(key, 0) + dict2[key]
    return dict1

# Pseudo-catan distribution with zero included
def catan_dist():
    catan_freq = {}
    for outcome1 in range(7):
        for outcome2 in range(7):
            dice_sum = outcome1 + outcome2
            catan_freq[dice_sum] = catan_freq.setdefault(dice_sum, 0) + 1
    return catan_freq.values()


# normalizes the values of the dictionary so that the sum of the values is 1
def normalize_dict(dict):
    total = sum((value for value in dict.values()))
    for key in dict:
        dict[key] = dict[key] / total
    return dict

'''
sum_dice(5, 15)
print(frequencies.values())
print(catan_dist())
'''
'''
dic = {}
dic[12] = 5
dic[4] = 3
my_sum = sum(dic.values())
p_12_is_last_hit = dic[12] / my_sum
for key in dic:
    dic[key] = dic[key]/my_sum
'''

#final_hit_calc(50, 8)
#print(final_hit_freq.values())

first = {'a' : 10,
         'b': 10}
second = {'b' : 10,
          'c' : 10}

#final_hit_calc(20, 4)
#print(final_hit_freq)
f = m_final_hit_calc(200, 60)
print(f)
print(normalize_dict(f))


