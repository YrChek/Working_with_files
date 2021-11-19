import os


def organize(path):
    final_dict = {}
    names_list = os.listdir(path)
    for queue_name in names_list:
        full_path = os.path.join(path, queue_name)
        with open(full_path, encoding='utf=8') as text:
            num_line = 0
            line = ''
            for i in text:
                num_line += 1
                line += i
        final_dict[num_line] = [queue_name, line]
    key_list = sorted(list(final_dict.keys()))
    with open('final_file.txt', 'w', encoding='utf=8'):
        pass
    with open('final_file.txt', 'a', encoding='utf=8') as file:
        for i in key_list:
            file.write(final_dict[i][0] + '\n')
            file.write(str(i) + '\n')
            file.write(final_dict[i][1] + '\n')
            file.write('\n')


organize(os.path.join(os.getcwd(), 'sorted'))