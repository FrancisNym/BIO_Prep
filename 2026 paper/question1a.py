letter_grid = [["A", "B", "C", "D", "E"],
               ["F", "G", "H", "I", "J"],
               ["K", "L", "M", "N", "O"],
               ["P", "Q", "R", "S", "T"],
               ["U", "V", "W", "X", "Y"]]


def find_letter_coords(letter):
    global letter_grid
    for i in range(5):
        if letter in letter_grid[i]:
            return [letter_grid[i].index(letter) + 1, (5-i)]


def Solution():
    text = input("Enter text: ")
    length = len(text)
    xcoord = 0
    ycoord = 0
    for i in range(length):
        coords = find_letter_coords(text[i])
        xcoord += (coords[0]-1)*5**((length-1)-i) 
        ycoord += (coords[1]-1)*5**((length-1)-i)
    return [xcoord+1, ycoord+1]

print(Solution())