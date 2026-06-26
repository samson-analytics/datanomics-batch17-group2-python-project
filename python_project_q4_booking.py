# 4)	 Movie Ticket Booking Simulation
# -	Simulate a movie theater booking system that:
# •	Shows a list of available movie titles, showtimes, and seat prices.
# •	Asks the user to choose a movie and number of tickets.
# •	 Confirms total price and asks if they want to book another movie.
# •	 Ends when they say "no" and displays total bookings and cost.

def movie_ticket_booking():
    movies = {
        "inception": {
            "showtime": "7:00 PM",
            "price": 10.0,
            "total_bookings": 0
        },
        "the matrix": {
            "showtime": "9:00 PM",
            "price": 12.0,
            "total_bookings": 0
        },
        "interstellar": {
            "showtime": "6:00 PM",
            "price": 15.0,
            "total_bookings": 0
        }
    }

    total_cost = 0

    print("Welcome to the Movie Ticket Booking System!")

    while True:
        print("\nAvailable movies:")
        for movie in movies:
            print(f"- {movie}: {movies[movie]['showtime']} - ${movies[movie]['price']:.2f}")

        customer_choice = input(
            "\nEnter movie name (or type 'exit' to finish): "
        ).lower()

        if customer_choice == "exit":
            break

        if customer_choice in movies:
            num_tickets = int(
                input(f"How many tickets for {customer_choice}? ")
            )

            if num_tickets > 0:
                cost = num_tickets * movies[customer_choice]["price"]
                total_cost += cost
                movies[customer_choice]["total_bookings"] += num_tickets

                print(
                    f"Total cost for {num_tickets} tickets to "
                    f"{customer_choice}: ${cost:.2f}"
                )
            else:
                print("Number of tickets must be greater than 0.")
        else:
            print("Movie not found. Please try again.")

    print("\nBooking Summary:")
    total_bookings = 0

    for movie in movies:
        if movies[movie]["total_bookings"] > 0:
            print(
                f"{movie}: "
                f"{movies[movie]['total_bookings']} tickets booked."
            )
            total_bookings += movies[movie]["total_bookings"]

    print(f"\nTotal tickets booked: {total_bookings}")
    print(f"Total Cost: ${total_cost:.2f}")


movie_ticket_booking()