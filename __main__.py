import glob
import sys

from extract_sql import extract_sql


def read_file(file: str):
    f = open(file, 'r', encoding='UTF-8')
    data = f.readlines()
    extract_sql(data)


if __name__ == '__main__':
    files = glob.glob("ExtractSQLTool/file/*.txt")

    if not files:
        sys.exit("ファイルが存在しません")

    for file in files:
        read_file(file)
