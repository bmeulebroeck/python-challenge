import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    voterct = 0

    khan = 0
    correy = 0
    li = 0
    otooley = 0

    candidates = []

    for row in csvreader:
        voterct = voterct + 1
        candidate = row[2]
        candidates.append(candidate)
        if candidate == "Khan":
            khan = khan + 1
        if candidate == "Correy":
            correy = correy + 1
        if candidate == "Li":
            li = li + 1
        if candidate == "O'Tooley":
            otooley = otooley + 1

    khanpct = (khan/voterct)*100
    correypct = (correy/voterct)*100
    lipct = (li/voterct)*100
    otooleypct = (otooley/voterct)*100


    print("Election Results:")
    print("--------------------------------")
    print(f'Total Votes: {voterct}')
    print("--------------------------------")
    print(f'Khan: {round(khanpct, 2)}%, {khan}')
    print(f'Correy: {round(correypct, 2)}%,{correy}')
    print(f'Li: {round(lipct,2)}%, {li}')
    print(f"O'Tooley {round(otooleypct,2)}%, {otooley}")
    print("--------------------------------")


    sorted(candidates)

    # unique_cand = []

    # for cand in candidates:
    #     if cand != unique_cand:
    #         unique_cand.append(cand)

    # this was a bad idea - print(unique_cand)
    # this was a bad idea - print(candidates) 