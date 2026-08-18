from config import connect

def update_data(clm,vlu,uvlu):
  '''
  This function is used to update data from the db
  '''
  tablename = "products"
  conn = connect()
  cur = conn.cursor()

  cur.execute(f"update {tablename} set {clm} ='{uvlu}' where id = {vlu};")
  conn.commit()
  print("")
  print("-------------------------- Data Updated Successfully ------------------------------")