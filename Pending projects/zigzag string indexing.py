#string = "lorem ipsum us nispant sdajna"

#def get_every_nth_char(s,n):
#    if n < 1:
#       return " "
#    return s[::n]
#print(get_every_nth_char(string, 4))
string = input("enter ur line: ")
rows = int(input("Enter the no. of rows: "))

def zigziag_index(s, num_rows):
    if num_rows == 1:
        return s
    elif num_rows <= 0:
        return "no string given"
    elif num_rows > len(s):
        print("No. of rows cannot be more than the length of the string")
    else:
        


print(zigziag_index(string, rows))

