def final_amount(p, r, n, t):
    """
Apply the compound interest to produce the
final amount
"""
    amount = p*(1+(r/n))**(n*t)
    return amount           #return the amount


#n = 2 #the interest i spaid out twice every year
#rate = 0.01 #interest of 1%

#Now let's use our function to generate amount

def main():
    toInvest = float(input("How much do you want to invest?"))
    fnl = final_amount(toInvest, 0.01, 2, 2)
    print("the amount you'll receive on an initial investement of",
      toInvest, "is: ", fnl)

main()      #call the main function




                  
