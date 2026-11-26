def sense(room, position):
    return room[position]

def reflex_agent(percept):
    if percept == "Dirty":
        return "Suck"
    else:
        return "Move"

def run_reflex():
    room = ["Dirty", "Clean", "Dirty", "Clean", "Dirty"]
    position = 0

    while position < len(room):
        percept = sense(room, position)
        action = reflex_agent(percept)

        if action == "Suck":
            room[position] = "Clean"

        print("Position:", position,
              "Percept:", percept,
              "Action:", action)

        position += 1

    goal = all(tile == "Clean" for tile in room)
    print("Final Room:", room)
    print("Goal Reached:", goal)

if __name__ == "__main__":
    run_reflex()
