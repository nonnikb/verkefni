def open_file(filename):
    try:
        table_file = open(filename, 'r')
        return table_file
    except:
        print("Cannot find file {}".format(filename))
        return ""


def value_to_list(filename):
    states_list = []
    HDDR_list = []
    MVDR_list = []
    TBR_list = []
    AS_list = []
    AO_list = []
    line = 1
    for line in filename:
        field_list = line.strip().split(',')
        states_list.append(field_list[0])
        HDDR_list.append(field_list[1])
        MVDR_list.append(field_list[5])
        TBR_list.append(field_list[7])
        AS_list.append(field_list[11])
        AO_list.append(field_list[13])
    return HDDR_list, MVDR_list, TBR_list, AS_list, AO_list