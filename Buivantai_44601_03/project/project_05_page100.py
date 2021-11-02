"""
Authon: Bui Van Tai
Date:18/09/2021

"""
import math
organisms = int(input("enter the initial number of organisms: "))
rateOfGrowth = int(input("enter the rate of growth: "))
num0fhours = int(input("enter the number of hours  to achieve the rate of growth: "))
totalhours =int(input("enter the total hours of growth: "))
hours =0
while (hours <= totalhours):
    organisms *= rateOfGrowth
    hours += num0fhours
    if(hours++totalhours):
        break
print("the total population:" ,organisms )


