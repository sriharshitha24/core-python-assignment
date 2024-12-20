def manage_seats(total_seats, booked_seats, book_seat=None, cancel_seat=None):

    if book_seat:
        if book_seat in booked_seats:
            print(f"Seat {book_seat} is already booked.")
        elif book_seat > total_seats or book_seat < 1:
            print(f"Seat {book_seat} is invalid.")
        else:
            booked_seats.append(book_seat)

    if cancel_seat:
        if cancel_seat in booked_seats:
            booked_seats.remove(cancel_seat)
            #print(f"Seat {cancel_seat} has been successfully cancelled.")
        else:
            print(f"Seat {cancel_seat} is not booked.")
            
    booked_seats.sort()
    available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available_seats, booked_seats

total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5

available_seats, updated_booked_seats = manage_seats(
    total_seats, booked_seats, book_seat=book_seat, cancel_seat=cancel_seat
)

print(f"Available seats: {available_seats}")
