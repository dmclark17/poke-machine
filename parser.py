pokes = []
mark = 'id=\"poke_live_item_'
mark_len = len(mark)

name_mark = 'aria-label=\"'
name_end_mark = '\"'

id_mark = 'poke_target='
id_end_mark = '&'

with open('response.txt','r') as f:
    for line in f:
        remaining_string = str(line)
        while(remaining_string.count(mark)):
            index = remaining_string.index(mark)
            name_start_index = remaining_string.index(name_mark, index) + len(name_mark)
            name_end_index = remaining_string.index(name_end_mark, name_start_index)
            name = remaining_string[name_start_index:name_end_index]
            print(name)

            id_start_index = remaining_string.index(id_mark, index) + len(id_mark)
            id_end_index = remaining_string.index(id_end_mark, id_start_index)
            id_num = remaining_string[id_start_index:id_end_index]

            remaining_string = remaining_string[index+mark_len:]

            pokes.append(id_num)

with open('targets.txt',  'w') as f:
    f.write('\n'.join(pokes) + '\n')
