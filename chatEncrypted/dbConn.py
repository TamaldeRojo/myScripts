import psycopg2


try:
  psycopg2.connect(
      host="",
      user="",
      password="",
      database=""
  )
  print("Conn ist richtig")
except Exception as e:
  print(f'An exception occurred: {e}')