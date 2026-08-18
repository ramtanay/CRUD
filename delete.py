from config import connect

def delete_data(vlu):
  '''
  This function is used to update data from the db
  '''
  tablename = "products"
  conn = connect()
  cur = conn.cursor()

  cur.execute(f"delete from {tablename} where id = {vlu};")
  conn.commit()
  print("")
  print("--------------------------- Data Deleted Successfully --------------------------------")
