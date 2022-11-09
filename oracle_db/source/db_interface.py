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
    cur.execute("create table customer_1(Emp_id integer, Customer_name varchar(30), Salary number(10) ,City varchar(20) )")
    res=cur.close()
    return res

def get_table_headers(table_name):
    global cur
    conn_str = u'system/Murali777@@localhost:1521/orclpdb'
    conn = cx_Oracle.connect(conn_str)
    cur = conn.cursor()
    cur.execute("insert into customer_1 values(1001, 'Nani', 72000,'Vishakapattanam')")
    cur.execute("insert into customer_1 values(1002, 'Mahesh', 42000,'Kasmir')")
    cur.execute("insert into customer_1 values(1003, 'Rajesh', 76000,'Hyderabad')")
    cur.execute("insert into customer_1 values(1004, 'Ramesh', 76000,'Banglore')")
    cur.execute("insert into customer_1 values(1005, 'Rohit', 76000,'Kolkata')")
    conn.commit()
    res = cur.close()
    return res

if __name__ == "__main__":
    pass
    #connect_database(host='localhost', port='1521', username='system', password='Murali777@', service_name='orclpdb')
    #r=get_table_data("customer_1")
    #print(r)
    #h=get_table_headers('customer_1')
    #print(h)

