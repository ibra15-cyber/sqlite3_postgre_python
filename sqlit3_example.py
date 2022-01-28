import sqlite3

def create_table():
    #connect a database; pass the name of the database
    conn=sqlite3.connect("lite.db")

    #create a cursor obj
    cur=conn.cursor()

    #write a sql query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #create a table store with col item, quantity and price

    #commit changes to database
    conn.commit()

    #close 
    conn.close()

def insert(item, quantity, price):
    conn =sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price)) #insert into the store this values
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store") #using this for terminal print out; select everything from store
    rows=cur.fetchall() #fechall
    conn.close()
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,)) #delete from store where item is the item we will passs
    conn.commit()
    conn.close()

def update(item, quantity, price): 
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("update store set quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()

# insert("tea mug", 10, 53)
# insert("coffe cup", 10, 30)
# delete("coffee cup")
# update('coffee cup', 11, 6 )

print(view())