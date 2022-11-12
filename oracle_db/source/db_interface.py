import cx_Oracle
cur=None
def connect_database(username,password,host,port,service_name):
    try:
        global cur
        conn_str = f"{username}/{password}@{host}:{port}/{service_name}"
        print(f"Connection to the db... : {conn_str}")
        conn = cx_Oracle.connect(conn_str)
        cur = conn.cursor()
    except Exception as e:
        print(f"Unable to connect the db service {service_name}")
        print(str(e))
def get_table_data(table_name):
    try:
        global cur
        query = f"SELECT * FROM {table_name}"
        cur.execute(query)
        for row in cur:
            print(f"Information about customer:{row}")
        cur.close()
    except Exception as e:
        print(f"Table doesn't exit in given database: {table_name}")
        print(str(e))
def get_table_headers(table_name):
    try:
        global cur
        query = f"SELECT * FROM {table_name} WHERE ROWNUM = 0"
        cur.execute(query)
        col_names = [row[0] for row in cur.description]
        print(col_names)
        cur.close()
    except Exception as e:
        print(f"table doesn't exit in given database: {table_name}")
        print(str(e))

if __name__ == "__main__":
    connect_database(host='localhost', port='1521', username='system', password='Murali777@', service_name='orclpdb')
    #get_table_data("customer_1")
    get_table_headers("customer_1")

