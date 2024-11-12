percentage=1
# percentage=2
# percentage=4
n=49522
# n=600000
# n=100000
# n=200000
i=0
prev=0
amount=n
tax_after_year=152
year=5
count=0
time=1000
while i<time and n<160000000:
    # if i>=50 and i<=100:
    #     percentage=10
    # else:
    #     percentage=2.80
    #     print(i)
    #     break
    count+=1
    # if i%20==0:
    
    #     amount+=13000
    #     n+=13000
    if i==tax_after_year:
    #     40% tax on intraday gains 
    #     n=n*0.60+capital
        # print("Before Tax ",n/10000000)
        # n=((n-amount)*0.70)+amount
        if n>250000:
            b_a=n-(amount+250000)
            n=(b_a*0.70)+amount+250000
            print("|-----------------------------------------------|")
            print(" After 1st Year","after tax :",n/10000000)
            prev=n/10000000
            
    if (i-20)%20==0:
        print("|-----------------------------------------------|")
        print(" Month :",(i//20)+1,"| Rupees: ",n/10000000)
    if n>1:
        #Trading before 2cr
        p=n/100
        #% per day
        n+=p*percentage
        # if i==500:
        #     print("Here 3 lakhs will be Deducted ", n/10000000)
        #     n-=200000
        #     print("Here 3 lakhs is  Deducted ", n/10000000)
        # # print(n/1000)
    i+=1
print("|-----------------------------------------------|")
print("     Before Tax   :",n/10000000,"cr")
print("|-----------------------------------------------|")
print("     After Tax    :",(((n//10000000)-prev)*0.60)+prev,"cr")
print("|-----------------------------------------------|")
print("    ",percentage,"% For Every:",252*year//time,"Days")
print("|-----------------------------------------------|")
# print(count)