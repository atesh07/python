import random 

#Movie List 
movieList=["1. Avatar 2","2. Titanic","3. Avengers Endgame","4. Jurassic World","5. The Dark Knight"]
#Create Seat Numbers
rows=['A','B','C','D','E']
seats={}
for r in rows:
    for n in range(1,11):
        seat_name=r+str(n)
        seats[seat_name]=False
# Booking 
bookings=[]
 # seat prise
seat_prise={
    "A":100,
    "B":200,
    "C":300,
    "D":600,    
    "E":600
}

class Movie:
    def __init__(self,seat_no,movie_name,price,ticket_id):
        self.seat_no=seat_no
        self.movie_name=movie_name
        self.price=price
        self.ticket_id=ticket_id

    def show_ticket(self):
        print("\n🎟️ TICKET GENERATED")
        print("--------------------------")
        print(f"Ticket ID : {self.ticket_id}")
        print(f"Movie Name : {self.movie_name}")
        print(f"Seat Number : {self.seat_no}")
        print(f"Price : ₹{self.price}")
        print("--------------------------\n")

#generate Ticket ID
def generate_ticket_id():
    return random.randint(1000000000, 9999999999)
# show movie list
def show_movies():
    print("\n🎬 Movie List:")
    for i , movie in enumerate(movieList,1):
        print(f"{i}. {movie}")
#show movies anavilable
def show_seats():
    print("\n🪑 Seats (X = Booked)\n")
    for r in rows:
        for n in range(1,11):
            seat=f'{r}{n}'
            if seats[seat]:
                print(" X ",end="")
            else :
                print(f" {seat} ",end="")
        print()  # New line after each row


# seat prise
def get_seat_price(seat):
    row=seat[0]
    return seat_prise[row]

# now booking of ticket 

def book_ticket():
    show_movies()
    choice=int(input("Enter Movie Number to Book Ticket : ")) - 1

    if choice not in range(movieList):
        print("Invalid Movie Selection")
        return
    selected_movie=movieList[choice]
    quaqntity=int(input("Enter Number of Tickets to Book : "))
    totel=0
    for _ in range(quaqntity):
        seat_choice=input("Choose seat (A1, B5, E10): ").upper()
        if seat_choice not in seats:
            print("Invalid Seat Selection")
            continue
        if seats[seat_choice]:
            print("Seat Already Booked")
            continue
        price=get_seat_price(seat_choice)
        print(f"💰 Seat {seat_choice} price: ₹{price}")
        seats[seat_choice]=True
        totel += price
        ticket_id=generate_ticket_id()





def main():
    while True:
        print("\n=======Welcome To Ticket Booking======")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Show Booking Details")
        print("4. Seats Available")
        print("5. Movie List")
        print("6. Exit")

        num=int(input("Enter Your Choice : "))
        match num:
            case 1:
                print("You selected 'Book Ticket'")
                #function call
            case 2:
                print("Your Selected 'Cancel Ticket'")
                #function call
            case 3:
                print("You Selected 'Show Booking Details'")
                #function call          
            case 4:
                print("You Selected 'Seats Available'")
                #function call
            case 5:
                print("You Selected 'Movie List'")
                #function call
            case 6:
                print("Thank You for Visiting")
                break
            case _:
                print("Invalid Option. Please try again.")


main()