import pdb
bike1 = 'yahama'
bike1_price = 25000

bike2 = 'honda'
bike2_price = 50000

pdb.set_trace()

name = input("Enter your name: ")
choose = input('Press 1 for yahama and 2 for honda: ')

if choose == 1:
    print(f"{bike1} will cost you {bike1_price}")
elif choose == 2:
    print(f"{bike2 + 20000} will cost you {bike2_price}")

else:
    print("Press only 1 or 2")