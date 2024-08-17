#Samuel Awud
#Jan 24 2023

"""
A program that calculate the amount someone saves in 20 years if they
save the same amount each month, including the interest earned. It will
also display the amount that person save for 30 years, and the  amount
they save for 20 years if they double the amount.
"""

#----------------------------------------------------------------------

"""
    The function below calculates the amount they save for N number of years

    input parameters:
        N - represents the number of years
        d - represents the periodic deposit
        r - represents the annual interest rate
        k - represents the compounding frequency

    The formula is
                        PN =  (d *(((1 + (r/k))^(nk)) - 1)) / (r / k)
    
    returns / output:
        a decimal representing the amount saved for N  number of years
"""


def total_balance(N, d, r, k):
    
    # Calculate the balance, PN, after N number of years
    PN = (d*(((1 + (r/k))**(N*k)) - 1))/(r / k)

    return PN

#------------------------------------------------------------------------


"""
    The function below calculates the interest earned after N number
    of years


    input parameters:
        d - represents the periodic deposit amount
        p - represents the number of periods
        b - represents the final balance after N number of years

    The formula ito find the total interest is:
                    Total interest = b - p*d

    returns / output:
        a decimal representing the interest earned after N number of years
    """

def total_interest(b, d, p):

    # calculate the total interest earned
    total_interest = b - p*d

    return total_interest

#------------------------------------------------------------------------

""" 
The function below calculates and displayes the final balance after N number of years 
and the total interest earned through those years. It also displays the 
total balance for 30 years and the total balance for 20 years if they 
double the deposite amount

"""

def display(interest, deposit):
    # Display the recieved interest rate and the deposit rate from the user
    print("Given {0} % annual interest rate and depositing ${1} monthly".format(interest*100, deposit))
    print()
    # display the output in a coloumn
    print("Years\t\tFINAL BALANCE\t\tINTEREST")

    # calculate the balance and interest for
    # periods for 20 years with the given deposit 
    N = 20
    k = 12
    test_balance = total_balance(N, deposit, interest, 12)

    periods = N*k
    test_interest = total_interest(test_balance, deposit, periods)
    # format and print the results  to two decimal places
    print("{0}\t\t${1:.2f}\t\t${2:.2f}".format(N, test_balance, test_interest))

    # calculate the balance and interest for
    # periods for 30 years with the given deposit 
    N = 30
    k = 12
    test_balance = total_balance(N, deposit, interest, 12)

    periods = N*k
    test_interest = total_interest(test_balance, deposit, periods)

    # format and print the result 
    print("{0}\t\t${1:.2f}\t\t${2:.2f}".format(N, test_balance, test_interest))
    print()

    # calculate the balance and interest for
    # periods for 20 years by doubling the deposit 
    print("If you double the amount you deposite, you will get: ")
    deposit = 2*deposit
    N = 20
    k = 12
    test_balance = total_balance(N, deposit, interest, 12)

    periods = N*k
    test_interest = total_interest(test_balance, deposit, periods)
    # format and print the result 
    print("{0}\t\t${1:.2f}\t\t${2:.2f}".format(N, test_balance, test_interest))



#-----------------------------------------------------------------------


'''
 We finally use this main function to recieve the interest rate and the
deposite amount from the user, and display the calculated results.

'''
if __name__ == '__main__':
    # Ask the user for the interest input 
    interest = float(input("Enter the interest rate in percentage (without the % symbol): "))
    # The interest rate here is in percentage and to get the required 
    # interest rate divide it by 100 
    interest = interest / 100

    # Ask the user for deposit amount 
    deposit = float(input("Enter the monthly deposite amount: "))

    # display the Calculated results
    display(interest, deposit)
