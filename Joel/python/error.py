try:
    # code that may raise an error
    result = 10 / 2 # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # code to handle the specific error (ZeroDivisionError in this case)4
    print("Error: Division by zero occurred!")
except Exception as e:
    # Code to handle any other type of error
    print("An error occurred:", else)
else:
    # Code that executes if no exception occurred
    print("No errors occurred.")
finally:
    # Code that always executes, regardless of whether an exception occurred
    print("End of error handling.")