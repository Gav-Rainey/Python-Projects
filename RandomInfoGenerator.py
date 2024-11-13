import csv, time, sys
from faker import Faker

fake, rows = Faker(), int(input("Rows To Create: "))

print("Creating Rows...")

time.sleep(0.5)

Headers = ["FirstName", "LastName", "HouseNum", "Town", "Postcode","Email"]

with open("RandInfo.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(Headers)

    for x in range(0, rows):
        info = ["("+"'"+fake.first_name()+"'",
                "'"+fake.last_name()+"'",
                "'"+fake.building_number()+"'",
                "'"+fake.city()+"'",
                "'"+fake.zipcode()+"'",
                "'"+fake.phone_number()+"'",
                "'"+fake.phone_number()+"'",
                "'"+fake.email()+"'",
                "'"+fake.date()+"')"]
        csv_writer.writerow(info)
print("\n| & ***** Process Complete ***** & |")
