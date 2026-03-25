def total_score(scores: list):
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i]
    return sum
def average(scores: list):
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i]
    if len(scores) > 0:
        return sum / len(scores)
    else: 
        return 0
def best_score(scores: list):
    if len(scores) > 0:
        maximum = 0
        for i in range(0, len(scores)):
            if scores[i] > maximum:
                maximum = scores[i]
        return maximum
    else:
        return None
def worst_score(scores: list):
    if len(scores) > 0:
        minimum = 100
        for i in range(0, len(scores)):
            if scores[i] < minimum:
                minimum = scores[i]
        return minimum
    else:
        return None
def rank_label(scores: list):
    total = total_score(scores)
    for i in range(0, len(scores)):
        if total >= 40:
            return "Legend"
        elif total >= 25 and total < 40:
            return "Elite"
        elif total >= 10 and total < 25:
            return "Fighter"
        elif total >= 0 and total < 10:
            return "Rookie"
        else:
            return "Fallen"
    if len(scores) == 0:
        return "Rookie"
def stability(scores: list):
    negative_score = False
    for i in range(0, len(scores)):
        if scores[i] < 0:
            negative_score = True
    if negative_score == False:
        return "Stable"
    else:
        return "Unstable"
def summary(monster: dict):
    monster_summary = {}
    for i in monster.keys():
        if i != "scores":
            monster_summary.update({i: monster[i]})
        else:
            monster_summary.update({"total": total_score(monster[i])})
            monster_summary.update({"average": average(monster[i])})
            monster_summary.update({"best": best_score(monster[i])})
            monster_summary.update({"worst": worst_score(monster[i])})
            monster_summary.update({"rank": rank_label(monster[i])})
            monster_summary.update({"stability": stability(monster[i])})
    return monster_summary
def print_tournament_report(monsters: list):
    for i in range(0, len(monsters)):
        print(summary(monsters[i]))
def print_average_tournament_score(monsters: list):
    tournament_score = 0
    for i in range(0, len(monsters)):
        tournament_score += total_score(monsters[i]["scores"]) if total_score(monsters[i]["scores"]) != None else 0
    print(f"Average tournament score is {tournament_score / len(monsters)}.")
def print_highest_scoring_monster(monsters: list):
    monster_score = {}
    maximum_score = 0
    for i in range(0, len(monsters)):
        monster_score.update({monsters[i]["name"]: total_score(monsters[i]["scores"])})
    for i in monster_score.keys():
        if monster_score[i] > maximum_score and monster_score[i] != None:
            maximum_score = monster_score[i]
    for i in monster_score.keys():
        if monster_score[i] == maximum_score:
            monster = i
    print(f"The highest scoring monster is {monster} with {maximum_score} points.")
def print_lowest_scoring_monster(monsters: list):
    monster_score = {}
    minimum_score = 1000
    for i in range(0, len(monsters)):
        monster_score.update({monsters[i]["name"]: total_score(monsters[i]["scores"])})
    for i in monster_score.keys():
        if monster_score[i] < minimum_score and monster_score[i] != None:
            minimum_score = monster_score[i]
    for i in monster_score.keys():
        if monster_score[i] == minimum_score:
            monster = i
    print(f"The lowest scoring monster is {monster} with {minimum_score} points.")
def monsters_per_rank(monsters: list):
    legend = 0
    elite = 0
    fighter = 0
    rookie = 0
    fallen = 0
    for i in range(0, len(monsters)):
        rank = rank_label(monsters[i]["scores"])
        if rank == "Legend":
            legend += 1
        elif rank == "Elite":
            elite += 1
        elif rank == "Fighter":
            fighter += 1
        elif rank == "Rookie":
            rookie += 1
        elif rank == "Fallen":
            fallen += 1
    print(f"There are {legend} Legend monsters, {elite} Elite monsters, {fighter} Fighter monsters, {rookie} Rookie monsters and {fallen} Fallen monsters.")
def monsters_per_stability(monsters: list):
    stable = 0
    unstable = 0
    for i in range(0, len(monsters)):
        monster_stability = stability(monsters[i]["scores"])
        if monster_stability == "Stable":
            stable += 1
        elif monster_stability == "Unstable":
            unstable += 1
    print(f"There are {stable} stable monsters and {unstable} unstable monsters.")
def monsters_by_element(monsters: list, element):
    element_monsters = list()
    for i in range(0, len(monsters)):
        if monsters[i]["element"] == element:
            element_monsters.append(monsters[i]["name"])
    print(f"Monsters with the {element} element are {element_monsters}.")
def best_round_minimum_20(monsters: list):
    minimum_20_monsters = list()
    for i in range(0, len(monsters)):
        if best_score(monsters[i]["scores"]) != None:
            if best_score(monsters[i]["scores"]) >= 20:
                minimum_20_monsters.append(monsters[i]["name"])
    print(f"Monsters with the best round of minimum 20 points are {minimum_20_monsters}.")
def find_monsters_by_rank(monsters: list, rank: str):
    rank_monsters = list()
    for i in range(0, len(monsters)):
        if rank_label(monsters[i]["scores"]) == rank:
            rank_monsters.append(monsters[i]["name"])
    print(f"The monsters with the {rank} rank are {rank_monsters}.")
monsters = [
    {"name": "Pytofang", "scores": [12, 18, -5, 20], "element": "fire"},
    {"name": "Aquanox", "scores": [10, 0, 8, 15], "element": "water"},
    {"name": "Stoneclaw", "scores": [25, -10, 5], "element": "earth"},
    {"name": "Zephyra", "scores": [9, 14, 11, 13, 10], "element": "air"},
    {"name": "Shadowbite", "scores": [], "element": "air"},
    {"name": "Voltaris", "scores": [30, -20, 25, -5], "element": "lightning"}
]
elements = ["fire", "water", "earth", "air", "lightning"]
ranks = ["Legend", "Elite", "Fighter", "Rookie", "Fallen"]
print_tournament_report(monsters)
print(f"Total number of monsters: {len(monsters)}.")
print_average_tournament_score(monsters)
print_highest_scoring_monster(monsters)
print_lowest_scoring_monster(monsters)
monsters_per_rank(monsters)
monsters_per_stability(monsters)
while True:
    try:
        print("The elements are: fire, water, air, earth, lightning")
        element = input("Enter the element: ")
        if element not in elements:
            raise ValueError("Invalid value")
        break
    except ValueError as e:
        print(e)
        print("Try again.")
monsters_by_element(monsters, element)
best_round_minimum_20(monsters)
while True:
    try:
        print("The ranks are: Legend, Elite, Fighter, Rookie, Fallen")
        rank = input("Enter the rank: ")
        if rank not in ranks:
            raise ValueError("Invalid value")
        break
    except ValueError as e:
        print(e)
        print("Try again")
find_monsters_by_rank(monsters, rank)