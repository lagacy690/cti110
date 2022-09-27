# Travel Expenses
# 09/26/22
# CTI-110 P1HW2 - Travel Expense
# Karsten Sally
#
print('This program calculates and displayes travel expenses')
budget = int(input())
print('Enter Budget:', budget)
destination = input()
print('Enter your travel destination:', destination)
gas = int(input())
print('How much do you think you will spend on gas?', gas)
hotel = int(input())
print('Approximately, how much will you need for accomodation/hotel?', hotel)
food = int(input())
print('Last, how much do you need for food?', food)
expense = gas + hotel + food
print('Location:', destination)
print('Initial Budget:', budget)
print(' ')
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print(' ')
print('Remaining Balance:', budget - expense)
