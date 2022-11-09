from libUtlis.db_interface import *
from libUtlis.excel_interface import *
from libUtlis.input_parser import *


def main():
    r=read_config()
    #db=input("Enter databaseCC Name:")
    #print(r[db]["HOST"])
    print(r["CCER"])

    """
    connect_database(host='localhost', port='1521', username='system', password='orcl', service_name='orcl')
    rows = get_table_data("CodeSpeedy")
    

    cols = list(map(list, zip(*rows)))
    heders = ["id", "name"]
    record = dict(zip(heders, cols))
    write_exel(record, 'output.xlsx')

    """

if __name__ == '__main__':
    main()