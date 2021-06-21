
# This program takes a user input (retail price) and returns a sale price, tax and final price
# --------------------------------------------------------------------------
# Variable Name         Data Type           Purpose
# --------------------------------------------------------------------------
# sofaRetail               float              declare retail price of sofa
# salePrice                  float              calculate/declare sales price of sofa
# tax                           float             calculate/declare sales tax of sofa
# finalPrice                float              calculate/declare final price of sofa


print("********************************************************")
print("SOFA EMPORIUM")
print("********************************************************")
# initializing and declaring variables
sofaRetail = float(input("Enter the retail price of the sofa: "))
salePrice = sofaRetail - (sofaRetail * .32)
tax = salePrice * .06
finalPrice = salePrice + tax
print("------------------------------------------------------------------------")
print("RETAIL PRICE: " + str(sofaRetail))
print("SALE PRICE: " + str(round(salePrice, 2)))
print("TAX: " + str(round(tax, 2)))
print("FINAL PRICE: " + str(round(finalPrice, 2)))

# This is the output from the program
# ********************************************************
# SOFA EMPORIUM
# ********************************************************
# Enter the retail price of the sofa: 325.99
# ------------------------------------------------------------------------
# RETAIL PRICE: 325.99
# SALE PRICE: 221.67
# TAX: 13.3
# FINAL PRICE: 234.97
# Process finished with exit code 0
