def get_dup_array(dup_item = 0, array = []):
    dup_array = []
    
    for item in array:
        if item == dup_item:
            dup_array.append(item)

    return dup_array


def get_single_sequence(diff_value = 0, array = []):
    single_seq = []
    single_seq.append(array[0])

    if diff_value == 0:
        single_seq = get_dup_array(array[0], array)

    else:
        found_index = 0
        array_len = len(array)

        for it in range(array_len):
            item = array[found_index]
            next_number = item + diff_value
        
            try:
                #print("Hello: " + str(array) + " next_number = " + str(next_number))
                found_index = array.index(next_number)

            except ValueError:
                found_index = -1 # element is not in the list
                break
            
            if found_index != -1 and it < found_index: # found
                #print ("Found index: " + str(found_index))
                single_seq.append(array[found_index])

    return single_seq

def get_all_seq(diff_value = 0, array = []):
    b_data = []

    index = 0
    array_len = len(array)

    for item in array:
        b_data.append(get_single_sequence(diff_value, array[index:array_len]))
        index += 1
    return b_data


def create_dict_sub(array = []):
    dict_sub = {}
    for index in range(len(array)):
        for s_index in range(index + 1, len(array)):
            dict_sub[abs(array[index] - array[s_index])] = []

    return dict_sub

def build_dict_data(dict_sub, array = []):
    for m_diff in dict_sub:
        all_thing = get_all_seq(m_diff, array)
        dict_sub[m_diff] = all_thing

    return dict_sub


def process_me(array):
    dict_sub = {}
    array.sort()
    print(array)

    dict_sub = create_dict_sub(array)
    print ("All possible step: " + str (dict_sub.keys()))
    print("=============================")
    dict_sub = build_dict_data(dict_sub, array)

    max_len = 0
    for key in dict_sub:
        for sub_list in dict_sub[key]:
            if len(sub_list) >= max_len:
                max_len = len(sub_list)

    print("FINAL RESULT = " + str(max_len))
    print("####################################################################################")
    print("")


# main function

process_me([4, 7, 1, 5, 3])
process_me([12, 12 , 12, 15, 10])
process_me([18, 26, 18, 24, 20, 22])



