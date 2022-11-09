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
    global cur
    query = f"SELECT * FROM {table_name}"
    cur.execute(query)
    res=cur.fetchall()
    return res

def get_table_headers(table_name):
    pass

if __name__ == "__main__":
    pass
    #connect_database(host='localhost', port='1521', username='system', password='orcl', service_name='orcl')
    #r=get_table_data("CodeSpeedy")
    #print(r)


