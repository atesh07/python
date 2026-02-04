import random

# Movie List
movieList = [
    "Avatar 2",
    "Titanic",
    "Avengers Endgame",
    "Jurassic World",
    "The Dark Knight"
]

# Create Seat Numbers
rows = ['A','B','C','D','E']
seats = {}

for r in rows:
    for n in range(1,11):
        seats[r+str(n)] = False

# Seat prices
seat_price = {
    "A":100,
    "B":200,
    "C":300,
    "D":600,
    "E":600
}

bookings = []

class Movie:
    def __init__(self, seat_no, movie_name, price, ticket_id):
        self.seat_no = seat_no
        self.movie_name = movie_name
        self.price = price
        self.ticket_id = ticket_id

    def show_ticket(self):
        print("\n🎟️ TICKET GENERATED")
        print("--------------------------")
        print(f"Ticket ID : {self.ticket_id}")
        print(f"Movie Name : {self.movie_name}")
        print(f"Seat Number : {self.seat_no}")
        print(f"Price : ₹{self.price}")
        print("--------------------------")

def generate_ticket_id():
    return random.randint(1000000000, 9999999999)

def show_movies():
    print("\n🎬 Movie List:")
    for i, movie in enumerate(movieList, 1):
        print(f"{i}. {movie}")

def show_seats():
    print("\n🪑 Seats (X = Booked)\n")
    for r in rows:
        for n in range(1,11):
            seat = r + str(n)
            print(" X " if seats[seat] else f" {seat} ", end="")
        print()

def get_seat_price(seat):
    return seat_price[seat[0]]

def book_ticket():
    show_movies()
    choice = int(input("Enter Movie Number: ")) - 1

    if choice not in range(len(movieList)):
        print("❌ Invalid movie!")
        return

    selected_movie = movieList[choice]
    quantity = int(input("How many tickets? "))

    total = 0

    for _ in range(quantity):
        show_seats()
        seat_choice = input("Choose seat (A1,B5,E10): ").upper()

        if seat_choice not in seats:
            print("Invalid seat!")
            continue

        if seats[seat_choice]:
            print("Seat already booked!")
            continue

        price = get_seat_price(seat_choice)
        seats[seat_choice] = True
        total += price

        ticket_id = generate_ticket_id()
        ticket = Movie(seat_choice, selected_movie, price, ticket_id)
        bookings.append(ticket)
        ticket.show_ticket()

    print(f"\n🧾 TOTAL AMOUNT: ₹{total}")

def show_bookings():
    if not bookings:
        print("\nNo tickets booked yet.")
        return
    for ticket in bookings:
        ticket.show_ticket()

def cancel_ticket():
    tid = int(input("Enter Ticket ID to cancel: "))

    for ticket in bookings:
        if ticket.ticket_id == tid:
            seats[ticket.seat_no] = False
            bookings.remove(ticket)
            print("❌ Ticket Cancelled!")
            return

    print("Ticket not found!")

def main():
    while True:
        print("\n====== MOVIE TICKET BOOKING ======")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Show Booking Details")
        print("4. Show Seats")
        print("5. Movie List")
        print("6. Exit")

        num = int(input("Enter Choice: "))

        if num == 1:
            book_ticket()
        elif num == 2:
            cancel_ticket()
        elif num == 3:
            show_bookings()
        elif num == 4:
            show_seats()
        elif num == 5:
            show_movies()
        elif num == 6:
            print("Thank you!")
            break
        else:
            print("Invalid option!")
            
main()