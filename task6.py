costprice=float(input('enter cost price'))
if costprice > 100000:
        tax_percentage = 15
        print("tax:",tax_percentage)
elif costprice > 50000:
        tax_percentage = 10
        print("tax:",tax_percentage)
else:
        tax_percentage = 5
        print("tax:",tax_percentage)
    
    
