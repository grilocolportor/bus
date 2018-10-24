from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'bus'

TABLES= {}

TABLES['bus'] = (
    "CREATE TABLE BUS ("
    " ID int(11) not null auto_increment, "
    " MARCA varchar(25) not null, "
    " MODELO varchar(25) not null, "
    " CHASSI varchar(25) not null, "
    " ANO varchar(7) not null, "
    " PRIMARY KEY(ID) "
    ") ENGINE=InnoDB"
)


cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='bus')
cursor = cnx.cursor()

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print('Create table {}: '.format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('already exists!')
        else:
            print(err.msg)
    else:
        print('OK!')

cursor.close()
cnx.close()

