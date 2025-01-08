from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike


niye_jao = RideSharing("Niye Jao")
rahim = Rider("Rahim Uddin", "rahim@gmail.com", 1234, "Mohakhali", 1200)
niye_jao.add_rider(rahim)
kolimuddin = Driver("Kolim Uddin", "kolim@gmail.com", 56, "Gulshan")
niye_jao.add_driver(kolimuddin)
print(niye_jao)