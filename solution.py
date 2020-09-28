def Minimum_Price(N, goodies, list1):
    
    result = +2147483647
    lim = +2147483647
    
    len1 = len(list1)
    list1.sort()
    res = []
    
    for i in range(len1 - N + 1): 
        result = int(min(result, list1[i + N - 1] - list1[i])) 
        
        if(result != lim):
            lim = result
            res = list1[i : (i + N - 1) + 1 ]
    
    print("The goodies selected for distribution are:")   
    
    for i in res:
        item = goodies.get(i)
        print(item, ":", i)
        
    print("And the difference between the chosen goodie with highest price and the lowest price is ", result)
    
    
if __name__ == "__main__":
    
    print("Enter the number of Employees: ", end = "")
    N = int(input())

    list1 = []
    goodies = {}
    list2 = ["Fitbit Plus", "IPods", "MI Band", "Cult Pass", "Macbook Pro","Digital Camera","Alexa","Sandwich Toaster","Microwave Oven", "Scale"]

    for i in range(len(list2)):
        print(list2[i],":", end = "")
        num = int(input())
        list1.append(num)

        goodies[num] = list2[i]

    Minimum_Price(N, goodies, list1)

'''
Input:
Goodies and Prices:
Fitbit Plus: 7980
IPods: 22349
MI Band: 999
Cult Pass: 2799
Macbook Pro: 229900
Digital Camera: 11101
Alexa: 9999
Sandwich Toaster: 2195
Microwave Oven: 9800
Scale: 4999
'''

    
