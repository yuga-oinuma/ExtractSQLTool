def convert_sql(pre_convert_sql_list: list):

    converted_sql_list = []
    converted_sql = []
    start_idx = -1
    end_idx = -1
    pre_convert_sql_list.append('endpoint')

    for line in pre_convert_sql_list:
        line = ''.join(line)
        if 'select' in line.lower() or 'update' in line.lower() or 'delete' in line.lower() or 'insert' in line.lower() or 'endpoint' in line:
            converted_sql.append('\n')
            converted_sql = ''.join(converted_sql)
            converted_sql_list.append(converted_sql)
            converted_sql = []

        for index, ch in enumerate(''.join(line)):
            if start_idx == -1 and ch == '\"':
                start_idx = index

            if start_idx != -1 and ch == '\"':
                end_idx = index
                converted_sql.append(''.join(line)[start_idx + 1: end_idx])
                start_idx = end_idx

    idx = 0
    for s in converted_sql_list:
        if len(s) == 1:

            continue
        else:
            idx += 1
            f = open('./SQLTool/file/sqls/sql'+str(idx)+'.txt', 'w')
            f.write(s)
            f.close()
