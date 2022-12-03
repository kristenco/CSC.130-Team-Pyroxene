def pay_for_courses():
    class_total = 0
    print("You class payment is $", class_total)
    payment_method = input("Pay online or at the cashiers office. Type \"online\" or \"cash\" to proceed:")

    if payment_method == "online":
     try:
        card_holder_name = str(input("Please enter card holders name:"))
        card_num = int(input("Please enter card number(no spaces):"))
        exp_date = input("Please enter expiration date:")
        security_code = int(input("Please enter 3 digit security code:"))
        print("Thank you your payment has been accepted")
     except(ValueError):
        invalid_input = input("Invalid input. To restart enter R. To exit enter any other key.")
        if invalid_input == "r" or invalid_input == "R":
            return pay_for_courses()

    elif payment_method == "cash":
        print("""Thank you. You can pay at Scott Northern Wake Campus. 
The address for the cashiers office is 6600 Louisburg Road Raleigh, NC 27616. 
It is located in Building C, Office 236D.
The phone number of the cashiers office is 919-866-5460. 
Office hours are Monday - Friday: 8 a.m. - 5 p.m. Closed for lunch: 2 p.m. - 3 p.m.""")
    else:
        invalid_input = input("Invalid input. To restart enter R. To exit enter any other key.")
        if invalid_input == "r" or invalid_input == "R":
            return pay_for_courses()
pay_for_courses()