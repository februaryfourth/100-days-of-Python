line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? A-C and 1-3")

position1 = position[0].lower()
position2 = int(position[1]) -1
letters = ["a", "b", "c"]
position1 = letters.index(position1)
map[position2][position1] = "X"



print(f"{line1}\n{line2}\n{line3}")