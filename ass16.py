def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    five_needed=rupees_to_make//5
    one_needed=rupees_to_make%5
    if five_needed<=no_of_five and one_needed<=no_of_one:
        print("no_of_five",five_needed)
        print("no_of_one",one_needed)
    elif five_needed>no_of_five:
        five_needed=no_of_five
        one_needed=rupees_to_make-(five_needed*5)
        if one_needed<=no_of_one:
            print("no_of_five",five_needed)
            print("no_of_one",one_needed)
        else:
            print(-1)
    else:
        print(-1)
    


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)
