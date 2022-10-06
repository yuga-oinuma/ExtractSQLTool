from convert_sql import convert_sql


def extract_sql(file: str):
    sql = list()
    start_idx = 0
    end_idx = 0
    for index, line in enumerate(file):
        if start_idx == 0 and 'values' in line.lower() and 'from' in line.lower() or 'update' in line.lower() or 'delete' in line.lower() or 'select' in line.lower() or 'insert' in line.lower():
            if 'select case' in line.lower() or 'end select' in line.lower():
                continue
            start_idx = index
        elif start_idx != 0 and '&' not in line and '+=' not in line:
            if '&' in file[index + 1] or '+=' in file[index + 1]:
                continue
            end_idx = index
            for i in range(start_idx, end_idx):
                sql.append(file[i])
            sql.append(file[end_idx])
            start_idx = 0
            end_idx = 0

    for s in sql:
        print(s)

    convert_sql(sql)
