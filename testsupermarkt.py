# -*- coding: utf-8 -*-
#----------------09/05/2020------
# Author     :   Crayon Noir
# Company    :   Djelfa Algeria 
#--------------------------------
 
from supermarkt import *
# انشاء ثلاث اوبجكت من الكلاس 
productOne = Product()

productOne.setId = 1
productOne.setNam = "Milk"
productOne.setPrice = 10
productOne.setShelfNo = "A"
productOne.setQantuty = 50

productTwo = Product()

productTwo.setId = 2
productTwo.setNam = "Chocolate"
productTwo.setPrice = 7
productTwo.setShelfNo = "B"
productTwo.setQantuty = 200

productThree = Product()

productThree.setId = 3
productThree.setNam = "Chess"
productThree.setPrice = 5
productThree.setShelfNo = "C"
productThree.setQantuty = 150
#----------------------------------
# مصفوفة بها الاوبجكتس
product = [productOne,productTwo,productThree]

print("Waht do you want:\n1-Buy\n2-Search")

choose=int(input("Entre your choise: "))

 #الاختيار الاول وهو الشراء 

if choose == 1:

    totalPrice=0
    invoice =""
    while True:
        print("Chose the product you want: ");
        n =1
        for i in product:
            print(n,"-",i.setNam,"[",i.setPrice," DA", "]")
            n+=1
        print("-1 Finish")
        numberOfproduct=int(input())
        if numberOfproduct==-1:
            break
        tmp=product[numberOfproduct-1]
        print("Entre quantity:  ")
        q = int(input())
        
        invoice+=("Name : "+tmp.setNam+" Unite price is: "+
                  str(tmp.setPrice)+" quantity: "+str(q)+" Totale: "+str(q*tmp.setPrice)+"\n")
        totalPrice+=q*tmp.setPrice;

    print(invoice);
    print("You will buy : ",totalPrice," DA" );

  #الاختيار الثاني  وهو البحث عن العنصر وسعره وكميته   
elif choose == 2:
    print("Entre the nam of product : ")
    pName=input()
    for i in product:
        if i.setNam==pName:
            print("Productname: ",i.setNam ,"\nProduct price: ",i.setPrice,"\nProduct location: ",i.setShelfNo)

#احتمال اختيار اخر غير مصنف
else:
    print("Invalid choose")




















 
