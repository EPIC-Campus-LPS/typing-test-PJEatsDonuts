import time 

sent = "I went to the grocery store"
print(sent)

# Get the epoch 
obj = time.gmtime(0) 
epoch = time.asctime(obj) 
print("starting time:", epoch)
x = input()

i = 0
while i == 0:
    if x == sent:
        i+=1
        print("Good job!")
        # Get the epoch again
        obj2 = time.gmtime(0) 
        epoch2 = time.asctime(obj2) 
        print("epoch is:", epoch2) 
    else:
        print("Nada")
        x = input()

epoch = float(epoch)
epoch2 = float(epoch2)
final_time = epoch-epoch2
print("your time is:", final_time)