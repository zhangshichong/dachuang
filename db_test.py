import sqlite3
"""
token = '000'
name = 'test'
no = 'test'
info = 'test'
s = ''
with open('ca.jpg', 'rb') as f:
    s=f.read()
    #print s
    f.close()
print s

"""
op = sqlite3.connect("photo.db")
"""
op.execute('''create table test (token nvarchar(40) not null primary key,
name nvarchar(20) not null,
no nvarchar(20) not null,
infomation nvarchar(200) default null,
photo blob not null)''')
op.commit()
"""
#insert , pay attention to buffer
#op.execute("insert into test values(?, ?, ?, ?, ?)",(token, name, no, info,buffer(s)))
#op.execute("delete * from test")
#op.commit()
#
cursor = op.execute("select * from test where name='zhang' ")
for row in cursor:
    print row[0]
    print row[1]
    print row[2]
    print row[3]
    #print row[4]


cursor.close()
op.close()
print 1
