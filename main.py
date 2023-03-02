# get input from user
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time in years: "))
rate = float(input("Enter the rate of interest: "))

# calculate simple interest
simple_interest = (principal * time * rate) / 100

# output the result
print("Simple interest = ", simple_interest)
