import psycopg2

def create_table():
    #connect a database; pass the name of the database
    conn=psycopg2.connect("dbname='database1' user='postgres' password='nyars150' host='localhost' port='5432'")
 
    #create a cursor obj
    cur=conn.cursor()

    #write a sql query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #create a table store with col item, quantity and price

    #commit changes to database
    conn.commit()

    #close 
    conn.close()

def insert(item, quantity, price):
    conn =psycopg2.connect("dbname='database1' user='postgres' password='nyars150' host='localhost' port='5432'")
    cur =conn.cursor()
    # cur.execute("INSERT INTO store VALUES('%s', '%s', '%s')" %(item, quantity, price)) #insert into the store this values
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price)) #more secured
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='nyars150' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store") #using this for terminal print out; select everything from store
    rows=cur.fetchall() #fechall
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='nyars150' host='localhost' port='5432'")
    cur=conn.cursor()
    # cur.execute("DELETE FROM store WHERE item='%s'" %(item,)) #delete from store where item is the item we will passs
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price): 
    conn=psycopg2.connect("dbname='database1' user='postgres' password='nyars150' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("update store set quantity='%s', price='%s' WHERE item='%s'" %(quantity, price, item))
    conn.commit()
    conn.close()


create_table()

# insert("yellow", 10, 33)
# delete("coffe cup")
update('yellow', 11, 333 )
# update ("coffee cup", 25, 253)

print(view())