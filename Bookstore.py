class BookStore:
    def __init__(self):
        """
        Initializes the BookStore class with a default number of books purchased set to 0.
        """
        self.number_of_books_purchased = 0
    
    def monthly_purchase(self):
        """
        Prompts the user to enter the number of books purchased this month.
        Ensures the input is a positive integer and either number should be 0,2,4,6,8 or >8
        
        Returns:
            int: The number of books purchased this month.
        """
        valid_values = {0,2,4,6,8}
        while True:
            try:
                # Prompt the user for the number of books purchased this month
                book_purchased_this_month = int(input("Enter the number of books purchased this month: "))
                # Check if the input is a non-negative integer
                if book_purchased_this_month < 0:
                    raise ValueError("The number of books must be a positive number.")
                if book_purchased_this_month not in valid_values and book_purchased_this_month < 8:
                    raise ValueError("The number of books must be 0, 2, 4, 6, 8 or more.")
                # Return the valid input
                return book_purchased_this_month
            except ValueError as e:
                # Handle invalid input and prompt the user again
                print(f"Invalid input: {e}. Please enter a valid number.")

    def display_award(self):
        """
        Determines and displays the points awarded based on the number of books purchased.
        Calls the monthly_purchase method to get the number of books purchased.
        """
        book_purchase = self.monthly_purchase()  # Get the number of books purchased this month
        
        # Determine points based on the number of books purchased
        if book_purchase == 0:
            print(f"Points earned: 0 for books purchased: {book_purchase}")
        elif book_purchase == 2:
            print(f"Points earned: 5 for books purchased: {book_purchase}")
        elif book_purchase == 4:
            print(f"Points earned: 15 for books purchased: {book_purchase}")
        elif book_purchase == 6:
            print(f"Points earned: 30 for books purchased: {book_purchase}")
        elif book_purchase >= 8:
            print(f"Points earned: 60 for books purchased: {book_purchase}")

def main():
    """
    Main function to run the BookStore program.
    Creates an instance of the BookStore class and displays the points awarded.
    """
    bookstore = BookStore()  # Create an instance of the BookStore class
    bookstore.display_award()  # Call the method to display the points awarded

if __name__ == "__main__":
    main()  # Execute the main function

