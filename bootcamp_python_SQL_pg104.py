

import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
conn = sqlite3.connect('myDB.db')

with conn :
    cur = conn.cursor()
    #create table
    cur.execute("CREATE TABLE IF NOT EXISTS myTbl( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    myCol TEXT \
    )")
    conn.commit()
    txt_list = []

    
    # insert data into table
    for i in fileList:
        if i.endswith('txt'):
            cur.execute('INSERT INTO myTbl (myCol) VALUES (?)', (i,))
    conn.commit()
    
    #query db and print to the console
    cur.execute('SELECT myCol FROM myTbl')
    output = cur.fetchall()
    print('text files in database: ' + str(output).strip('[]'))

            
conn.close()

