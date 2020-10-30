no = int(input("Enter the total no of sites"))
result_site = int(input("Enter the result site"))
A = [None] * (no+1)
B = []
strategies = []
strategy = 0

# Accept data information for each site(check for availability)

for i in range(1, no+1):
    available = input("Is data for this site available ? Enter y or n")

    if(available == "y"):
        nooftuples = int(input("Enter no of tuples"))
        size = int(input("Enter size of each tuple"))

        data_size = nooftuples*size
        A[i] = data_size

    else:
        A[i] = 0

# Accept result relation data

print("** Enter Result Site Data ***")
nooftuples = int(input("Enter no of tuples"))
size = int(input("Enter size of each tuple"))
result_data  = nooftuples * size

# Find total strategies and calculate data transfer for each strategy
print("** PROCESSING ***")

for i in range(1, no+1):
    (total_data, total_data_transfer) = (0, 0)  

    if(i == result_site):
        for j in range(1, no+1):
            if(j != result_site):
                print("Transfer data from site ",j," to site ",result_site)
                total_data += A[j]
        strategy += 1
        print("Strategy Id:", strategy)
        print("Total Data Transfer:", total_data)
        B.append(total_data)
        strategies.append(strategy)

    else:
        for k in range(1, no+1):
            if(k != i):
                print("Transfer data from site ",k," to site ",i)
                total_data += A[k]

        total_data_transfer = total_data + result_data 
        strategy += 1
        B.append(total_data_transfer)
        strategies.append(strategy)

        print("Strategy Id:", strategy)
        print("Total Data Transfer:", total_data_transfer)

print("** ENDED ***")

print("Min data transfer", min(B))
print("Best strategy", strategies[B.index(min(B))])
