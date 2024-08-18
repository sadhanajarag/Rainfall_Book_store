class RainfallCalculator:
    def __init__(self):
        """ Initilizes the RainfallCalculator with default values.
         - total_month : Count the total number of months of data collected
         - totoal_rainfall : Accumalates the total rainfall in inches"""
        
        self.total_month = 0
        self.total_rainfall = 0.0
        self.month_names = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]

                            
    """Collects rainfall data from the user for a specified number of years.
        Uses nested loops to iterate over each year and month.
        Ensures valid input for rainfall amounts."""
    
    def get_data(self):
        while True:
            try:
                num_year = int(input("Enter the number of years:"))
                if num_year <= 0:
                    raise ValueError("Number of year must be positive number")    
                return  num_year                 
            except ValueError as e:
                print(f"invalid input {e}")
                
    def collect_data(self):
        """ Collects rainfall data from the user for a specified number of years.Uses nested loops to iterate over each year and month.
        Ensures valid input for rainfall amounts."""
        num_years = self.get_data()
        # Outer loop for each year
        for year in range(1, num_years + 1):
            print(f"\nYear : {year} :")
            # Inner loop for each month
            for months in self.month_names:
                    while True:
                      try:
                        # Prompt the user for rainfall data
                        rainfall = float(input(f" Enter inches of rainfall for month {months}:"))
                        if rainfall < 0:
                             raise ValueError("Rainfall can not be negative")
                        break
                      except ValueError as e:
                          print (f"Invalid Input : {e }\n Please enter a positive number")
                    # Accumulate total rainfall and count the months
                    self.total_rainfall +=rainfall
                    self.total_month +=1

    def calculate_avg_rainfall(self):
        """Calculates the average rainfall per month.Returns:float: The average rainfall per month."""
        if self.total_month >0:
            average_rainfall = self.total_rainfall/self.total_month
        else :
            average_rainfall = 0.0
        return average_rainfall
        
    def display_results(self):
        """ Displays the total number of months, total inches of rainfall,and the average rainfall per month."""
        avarage_rainfall = self.calculate_avg_rainfall()
        print(f"\nTotal number of months :{self.total_month}")
        print(f"\nTotal inches of rainfall : {self.total_rainfall :.2f} ")
        print(f"\nAverage rainfall per mont : {avarage_rainfall:.2f}")

def main():
    """Main function to run the RainfallCalculator program.
    Creates an instance of RainfallCalculator, collects data, and displays results."""
    calculator = RainfallCalculator()
    calculator.collect_data()
    calculator.display_results()

if __name__ == "__main__":
    main()

                        
                        
              
