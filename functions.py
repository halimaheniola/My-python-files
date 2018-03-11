"""def even_numbers(startpoint, endpoint):
    even_numbers=[]
    for number in range(startpoint, endpoint):
        if number%2==0:
            even_numbers.append(number)
    return even_numbers


def generatenumber():
    startpoint=input("Enter a start point:")
    endpoint=input("Enter an endpoint:")
    return (even_numbers(int(start), int(endpoint)))#retun won't display result.

generatenumber()


#write a function that accepts a list of numbers and returns the summation of number
#in the list multiplied by the length of the list



list_of_numbers=generatenumber
def sum_list(number_list):
   
    total=0
    for item in number_list:
        total+=item
    return total*len(number_list)
print(sum_list(list_of_numbers))"""



#write a program that creates a variable containing items and displays resulting items as a collection of tuple, dictionary and list







"""vardict={"key":"person","preference":["book","movies","pizza",("fun","games","football")]}
for item in vardict:
    if type(vardict[item])==list or type(vardict[item])==tuple:
        for inneritem in vardict[item]:
            print(inneritem)
    elif type(vardict[item])==dict:
        for dictitem in vardict[item]:
            print(vardict[item][vardict])
    else:
        print(vardict[item])"""



item_list=["person","school",{"number":10,"position":"md"},("mango","fruit","church"),["school","mosque"]]
def extract_items(item_sequence):
    if type(item_sequence)==dict:
        for item in item_sequence:
            if type(item_sequence[item])==dict:
                print (item_sequence[item])
            elif type(item_sequence[item])==list or type(item_sequence[item])==tuple:
                for inneritem in item_sequence[item]:
                    extract_items(inneritem)
            else:
                print(item_sequence[item])
    elif type(item_sequence)==list or type(item_sequence)==tuple:
        for item in item_sequence:
            extract_items(item)

    else:
        print(item_sequence)

extract_items(item_list)


#TKINTER a library Jango pyramid flask frameworks for building websites using python

# a function that calls itself is called a recurssive function a recurssive function requires  recursive statement to terminate else
#it'll keep recalling itself.
#ot all functions accept arguments depending on what the function is meant to work on
