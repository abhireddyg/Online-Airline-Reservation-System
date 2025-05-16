import csv
import os
import time

os.system('cls')
FLIGHTS = [
    {"Flight No": "AI101", "From": "Delhi", "To": "Mumbai", "Seats": 50},
    {"Flight No": "AI202", "From": "Hyderabad", "To": "Bangalore", "Seats": 60},
    {"Flight No": "AI303", "From": "Chennai", "To": "Delhi", "Seats": 70},
]

BOOKINGS_FILE = "bookings.csv"

def initialize_bookings_file():
    if not os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Flight No", "From", "To"])

def view_flights():
    print("\nAvailable Flights:")
    for flight in FLIGHTS:
        print(f"{flight['Flight No']}: {flight['From']} -> {flight['To']} | Seats: {flight['Seats']}")

def book_flight():
    name = input("Enter your name: ")
    flight_no = input("Enter flight number to book: ").upper()
    
    for flight in FLIGHTS:
        if flight['Flight No'] == flight_no:
            with open(BOOKINGS_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, flight["Flight No"], flight["From"], flight["To"]])
            print("✅ Booking successful!\n")
            return
    print("❌ Invalid flight number. Try again.\n")
    a = int(input("Do you want to see availabe flights\n\t1. Yes  2. No\t:"))
    # (a==1)?view_flights():(a==2)?initialize_bookings_file():
    while(a!=1 and a!=2):
        print("Choose Valid Option")
        time.sleep(1.5)
        a = int(input("Do you want to see availabe flights 1. Yes  2. No\t:"))
    if(a==1):
        os.system('cls')
        view_flights()
        book_flight()
        print("Now You can book your flight...\n ")
    elif(a==2):
        time.sleep(1)
        main()
    
        

    
    

def view_bookings():
    print("\nYour Bookings:")
    with open(BOOKINGS_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        found = False
        for row in reader:
            print(f"Passenger: {row[0]} | Flight: {row[1]} | From: {row[2]} -> {row[3]}")
            found = True
        if not found:
            print("No bookings found.\n")

def cancel_booking():
    name = input("Enter your name to cancel booking: ")
    flight_no = input("Enter your flight number: ").upper()
    
    bookings = []
    canceled = False
    
    with open(BOOKINGS_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == name and row[1] == flight_no:
                canceled = True
                continue
            bookings.append(row)

    with open(BOOKINGS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(bookings)
    
    if canceled:
        print("✅ Booking canceled successfully.\n")
    else:
        print("❌ No matching booking found.\n")

def main():
    initialize_bookings_file()
    while True:
        print("\n--- Online Airline Reservation System ---")
        print("1. View Available Flights")
        print("2. Book a Flight")
        print("3. View Bookings")
        print("4. Cancel Booking")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            view_flights()
            time.sleep(2)
        elif choice == '2':
            book_flight()
            time.sleep(2)
        elif choice == '3':
            view_bookings()
            time.sleep(2)
        elif choice == '4':
            cancel_booking()
            time.sleep(2)
        elif choice == '5':
            print("Thank you for using our system! ✈️")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
