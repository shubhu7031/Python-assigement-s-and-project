# create a function that accepts 2 arguments the first argument is list and the second argument is asc,dsc,etc
#if the asc argument is specified return the ascending order of the list
# if the dsc argument is specified return the descending order of the list
# if any argument is not specified  same list


def list1(num,value):

    if "asc" in value:
        num.sort()
        print(num)
    elif "dsc" in value:
        num.sort(reverse=True)
        print(num)

l1=[10,47,485,4,471,1]

list1(l1,"dsc")