from config import connect

def new_table():
  '''
  This function creates a table.
  '''
  con = connect()
  cur = con.cursor()
  sql = '''
      create table if not exists products(
        id int primary key,
        name varchar(25),
        price int,
        quantity int
      );
    '''
  cur.execute(sql)
  print("")
  print("-------------------------------- New Table created ----------------------------------")