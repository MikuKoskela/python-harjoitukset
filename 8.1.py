# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
# sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.

import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='S4l4_sana',
         autocommit=True)
def haku():
    icao = input("Anna lentokentän ICAO-koodi: ")
    sql = 'select gps_code,name,continent from airport where gps_code = "'+ icao +'"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    response = kursori.fetchall()
    return(response)
print(haku())
