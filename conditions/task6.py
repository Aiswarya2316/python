costprice=float(input('enter cost price'))
if costprice > 100000:
        tax_percentage = 0.15 * costprice
        print("tax:",tax_percentage)
elif costprice > 50000:
        tax_percentage = 0.10 * costprice
        print("tax:",tax_percentage)
else:
        tax_percentage = 0.05 * costprice
        print("tax:",tax_percentage)
    
    
