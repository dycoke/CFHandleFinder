import json

with open("config.json", "r") as f:
    config = json.load(f)

clauses = config["clauses"]

with open("contest.json", "r") as f:
    submissions = json.load(f)

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

handles = []
found = False
for clause in clauses:
    possible_handles = []
    for submission in submissions:
        problem_id = submission["problem"]["index"]
        if "verdict" not in submission:
            continue
        verdict = submission["verdict"]
        if problem_id == clause[0] and verdict == clause[1]:
            possible_handles.append(submission["author"]["members"][0]["handle"])
    if not found:
        handles = possible_handles
        found = True
    else:
        handles = intersection(handles, possible_handles)
print(handles)