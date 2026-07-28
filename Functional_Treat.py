# Functional Treat

summary = {}

# Welcome Function
def welcome():
    print("=" * 60)
    print("Welcome to the Data Analyzer and Transformer Program")
    print("=" * 60)

# Menu Function
def menu():
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

# Input Data Function (1D + 2D)

def input_data():

    print("\nSelect Array Type")
    print("1. 1D Array")
    print("2. 2D Array")

    arr_choice = input("Enter your choice: ")

    # ---------- 1D ARRAY ----------
    if arr_choice == "1":

        user_input = input("\nEnter data for a 1D array (separated by spaces):\n")

        data = list(map(int, user_input.split()))

        print("\nData has been stored successfully!")

        return data, "1D"

    # ---------- 2D ARRAY ----------
    elif arr_choice == "2":

        rows = int(input("\nEnter number of rows: "))

        data = []

        for i in range(rows):

            row = list(map(int, input(f"Enter row {i+1}: ").split()))

            data.append(row)

        print("\n2D Array has been stored successfully!")

        return data, "2D"

    else:

        print("\nInvalid Choice!")

        return [], "1D"

# Display Summary Function (1D + 2D)

def display_summary(*args, **kwargs):

    global summary

    if len(args) == 0 or len(args[0]) == 0:
        print("No data available!")
        return

    data = args[0]

    # ---------- 1D ARRAY ----------
    if array_type == "1D":

        total = sum(data)
        average = round(total / len(data), 2)

        summary = {
            "Array Type": "1D Array",
            "Total elements": len(data),
            "Minimum value": min(data),
            "Maximum value": max(data),
            "Sum of all values": total,
            "Average value": average
        }

    # ---------- 2D ARRAY ----------
    else:

        flat_data = []

        for row in data:
            for value in row:
                flat_data.append(value)

        total = sum(flat_data)
        average = round(total / len(flat_data), 2)

        summary = {
            "Array Type": "2D Array",
            "Rows": len(data),
            "Columns": len(data[0]),
            "Total elements": len(flat_data),
            "Minimum value": min(flat_data),
            "Maximum value": max(flat_data),
            "Sum of all values": total,
            "Average value": average
        }

    print("\nData Summary:")

    for key, value in summary.items():
        print(f"- {key}: {value}")

    if kwargs:

        print("\nAdditional Characteristics:")

        for key, value in kwargs.items():
            print(f"- {key}: {value}")

def filter_data(data):

    if len(data) == 0:
        print("No data available!")
        return

    limit = int(input("\nEnter a threshold value to filter data:\n"))

    if array_type == "1D":

        new_data = list(filter(lambda x: x >= limit, data))

        print(f"\nFiltered Data (values >= {limit}):")

        if len(new_data) == 0:
            print("No values found.")
        else:
            print(", ".join(map(str, new_data)))

    else:

        print(f"\nFiltered 2D Array (values >= {limit}):")

        found = False

        for row in data:

            new_row = list(filter(lambda x: x >= limit, row))

            if new_row:
                found = True
                print(new_row)

        if not found:
            print("No values found.")

def sort_data(data):

    if len(data) == 0:
        print("No data available!")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("\nEnter your choice: ")

    if array_type == "1D":

        temp = data.copy()

        if choice == "1":
            temp.sort()
            print("\nSorted Data in Ascending Order:")

        elif choice == "2":
            temp.sort(reverse=True)
            print("\nSorted Data in Descending Order:")

        else:
            print("Invalid choice!")
            return

        print(", ".join(map(str, temp)))

    else:

        temp = []

        for row in data:

            if choice == "1":
                temp.append(sorted(row))

            elif choice == "2":
                temp.append(sorted(row, reverse=True))

            else:
                print("Invalid choice!")
                return

        if choice == "1":
            print("\nSorted 2D Array in Ascending Order:")
        else:
            print("\nSorted 2D Array in Descending Order:")

        for row in temp:
            print(row)

def dataset_statistics(data):

    if len(data) == 0:
        return None, None, None, None

    if array_type == "1D":

        minimum = min(data)
        maximum = max(data)
        total = sum(data)
        average = round(total / len(data), 2)

        return minimum, maximum, total, average

    else:

        flat = []

        for row in data:
            flat.extend(row)

        minimum = min(flat)
        maximum = max(flat)
        total = sum(flat)
        average = round(total / len(flat), 2)

        return minimum, maximum, total, average

# ---------------- Main Program ----------------

data = []
array_type = "1D"

welcome()

while True:

    menu()

    choice = input("\nPlease enter your choice: ")

    if choice == "1":

        print("\nStep 1 : Input Data")

        data, array_type = input_data()

    elif choice == "2":

        print("\nStep 2 : Display Data Summary")

        display_summary(
            data,
            dataset_type=array_type + " Array",
            status="Active"
        )

    elif choice == "3":

        print("\nStep 3 : Calculate Factorial")

        number = int(input("Enter a number to calculate its factorial: "))

        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n-1)

        answer = factorial(number)

        print(f"\nFactorial of {number} is : {answer}")

    elif choice == "4":

        print("\nStep 4 : Filter Data")
    

        filter_data(data)

    elif choice == "5":

        print("\nStep 5 : Sort Data")

        sort_data(data)

    elif choice == "6":

        print("\nStep 6 : Dataset Statistics")

        minimum, maximum, total, average = dataset_statistics(data)

        if minimum is not None:

            print("\nDataset Statistics")
            print(f"Minimum Value : {minimum}")
            print(f"Maximum Value : {maximum}")
            print(f"Sum : {total}")
            print(f"Average : {average}")

        else:

            print("No data available!")

    elif choice == "7":

        print("\nStep 7 : Exit Program")
        print("\nThank you for using the Data Analyzer and Transformer Program.")

        break

    else:

        print("\nInvalid Choice! Please Try Again.")
