CO = int(input("What do you have in colombian pesos?  "))
PE = int(input("what do you have in Peruvian soles? "))
BR = int(input("What do you have in Brazilian reais? "))
COUSD = CO*0.00025
PEUSD = PE*0.28
BRUSD = BR*0.21
USD = COUSD + PEUSD + BRUSD
print("The US currency you will have is:")
print(USD)
