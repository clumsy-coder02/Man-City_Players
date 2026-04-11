# display
print("\tManchester City Players")

# positions
print("1.GoalKeeping\n2.Defense\n3.Midfield\n4.Attack")

# first user input
print() # spacing
try:
    main_position = input("Select player's position from above? ")
except:
    print("Select by typing a number 1 to 4")
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
    try:
        minor_position = input("Select player's position from above? ")
    except:
        print("Select by typing a number 1 to 4")
    print() # spacing

    defenders = {
        "RB": ["John Stones","Abdukodir Khusanov","Rico Lewis","Issa Kaboré","Matheus Nunes"],
        "LB": ["Nico O'Reilly","Rayan Aït-Nouri","Joško Gvardiol","Nathan Aké",],
        "CB": ["Rúben Dias","John Stones","Nathan Aké","Marc Guéhi","Joško Gvardiol",
            "Abdukodir Khusanov","Max Alleyne","Kaden Braithwaite","Kian Noble"]
    }

    if minor_position == "1":
        output = defenders["RB"]
        print(f"Right Back(RB): {",".join(output)}")
    elif minor_position == "2":
        output = defenders["LB"]
        print(f"Left Back(LB): {",".join(output)}")
    elif minor_position == "3":
        output = defenders["CB"]
        print(f"Center Back(CB): {",".join(output)}")

# midfielders
def midfielders_function():
    # show midfielders
    print("1.Defensive Midfielder(DMF)\n2.Central Midfielder(CMF)\n3.Attacking Midfielder(AMF)")

    print() # spacing
    try:
        minor_position = input("Select player's position from above? ")
    except:
        print("Select by entering a number")
    print()

    midfielders = {
        "AMF": ["Bernardo Silva","Phil Foden","Rayan Cherki","Oscar Bobb",
                "Divine Mukasa","Tijjani Reijnders","Matheus Nunes"],
        "CMF": ["Rodri","Nico González","Mateo Kovačić","Tijjani Reijnders",
                "Matheus Nunes","Bernardo Silva","Sverre Nypan","Charlie Gray"],
        "DMF": ["Rodri","Nico González","Mateo Kovačić","Tijjani Reijnders"]
    }

    if minor_position == "1":
        output = midfielders["DMF"]
        print(f"Defensive Midfielders: {",".join(output)}")
    elif minor_position == "2":
        output = midfielders["CMF"]
        print(f"Central Midfielders: {",".join(output)}")
    elif minor_position == "3":
        output = midfielders["AMF"]
        print(f"Attacking Midfielders: {",".join(output)}")

# attackers
def attack_function():
        # show midfielders
    print("1.Left Wing Forward(LWF)\n2.Center Forward(CF)\n3.Right Wing Forward(RWF)")

    print() # spacing
    try:
        minor_position = input("Select player's position from above? ")
    except:
        print("Select by entering a number 1 to 3")
    print()

    attack = {
        "LWF": ["Omar Marmoush","Jérémy Doku ","Savinho","Antoine Semenyo"],
        "CF": ["Erling Haaland","Omar Marmoush","Divin Mubama","Reigan Heskey","Jaden Heskey"],
        "RWF": ["Omar Marmoush","Jérémy Doku","Savinho","Antoine Semenyo"]
    }


    if minor_position == "1":
        output = attack["LWF"]
        print(f"Left Wingers: {",".join(output)}")
    elif minor_position == "2":
        output = attack["CF"]
        print(f"Center Forwards: {",".join(output)}")
    elif minor_position == "3":
        output = attack["RWF"]
        print(f"Right Wingers: {",".join(output)}")
    

# first function to call
if __name__ == "__main__":
    main_options()

