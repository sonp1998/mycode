#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""


def main(): 
    #create a list called list1
    list1 = ["crisco_nxos", "artista_eos", "cisco_ios"]

    #display list1
    print(list1)
    
    #display list1[1] which should only display atista_eos
    print(list1[1])
    
    #create a new list containing a single item
    list2= ["juniper"]

    #extend list1 by list2 (combine both lists together into a single list)
    list1.extend(list2)

    print(list1)
    
    #create list3 
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #append operation to append list1 by list3
    list1.append(list3)
    print(list1)
    
    print(list1[4])

    print(list1[4][0])


main()

