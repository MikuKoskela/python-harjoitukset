import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='S4l4_sana',
         autocommit=True)

def hae(lentoasema):
    sql = "select type, count(type) from airport where iso_country = '"\
          + lentoasema +"' group by type order by count(type) asc;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(f"{i[0]}:{i[1]}")
x = input("Anna maan lyhenne: ")
hae(x)

