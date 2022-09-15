import mysql.connector
from geopy import distance
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='S4l4_sana',
         autocommit=True)
def haku():
    icao = input("Syötä lentokentän ICAO-koodi: ")
    sql = 'select latitude_deg, longitude_deg from airport where gps_code = "' +icao + '"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    response = kursori.fetchall()
    if kursori.rowcount > 0:
        return response[0]
    else:
        print("kenttää ei löydy.")

loc1 = haku()
print(loc1)
loc2 = haku()
print(loc2)
gap = distance.distance(loc1,loc2).km
print(gap)
print(f"Lentokenttien välinen etäisyys on {gap:.2f} km.")
