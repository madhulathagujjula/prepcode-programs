number = int(input("enter the number:"))
starting =2
is_primr = True
while(starting < number):
    if number % starting ==0:
        is_prime = False
    starting += 1
print(is_prime)