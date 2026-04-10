# display
print("\tManchester City Players")

# positions
print("1.GoalKeeping\n2.Defense\n3.Midfield\n4.Attack")

# first user input
print() # spacing
main_position = input("Select player's position from above? ")
print() # spacing

# main options
def main_options():
    if main_position == "1":
        goalkeepers_function() # call goalkeepers
    elif main_position == "2":
        defenders_function() # call defenders
    elif main_position == "3":
        midfielders_function() # call midfielders
    elif main_position == "4":
        attack_function() # call attack
    else:
        print("Select by typing a number 1 to 4")

# main functions
# goalkeepers
def goalkeepers_function():
    goalkeepers = {
        "GK": ["Gianluigi Donnarumma", "James Trafford","Stefan Ortega","Marcus Bettinelli"]
    }
    output = goalkeepers["GK"]
    print(f"GoalKeepers: {",".join(output)}")


# defenders
def defenders_function():
    # show defenders
    print("1.Right Back(RB)\n2.Left Back(LB)\n3.Center Back(CB)")

    print() # spacing
    minor_position = input("Select player's position from above? ")
    print() # spacing

    defenders = {
        "RB": ["Nunes"],
        "LB": ["Nico"],
        "CB": ["Dias", "Gvardial"]
    }

    if minor_position == "1":
        pass # display right backs
    elif minor_position == "2":
        pass # display left backs
    elif minor_position == "3":
        pass # display center backs
    else:
        print("Select by entering a number")

# midfielders
def midfielders_function():
    # show midfielders
    print("1.Defensive Midfielder(DMF)\n2.Central Midfielder(CMF)\n3.Attacking Midfielder(AMF)")
    minor_position = input("Select player's position from above? ")

    if minor_position == "1":
        pass # display DMF
    elif minor_position == "2":
        pass # display CMF
    elif minor_position == "3":
        pass # display AMF
    else:
        pass 

# attackers
def attack_function():
    # show attackers
    pass

# first function to call
if __name__ == "__main__":
    main_options()


# # output format
# list = ["Goy", "Reagan"]
# print(",".join(list))

