import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
results = os.path.join("Resources", "results.txt")

voterct = 0

candidates = []
cand_totals = {}
pctofvote = {}

winner = ""
winner_tot = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    for row in csvreader:
        voterct = voterct + 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            cand_totals[candidate] = 0 
        cand_totals[candidate] += 1
    
    # used while testing to make sure I was getting the right result from my loop
    # print(voterct)
    # print(candidates)
    # print(cand_totals)

    # print to terminal
    print("Election Results:")
    print("--------------------------")
    print(f'Total Votes: {voterct}')
    print("--------------------------")

# write initial totals to the txt file
with open(results, 'w') as results_txt:
    results_txt.write('Election Results:\n')
    results_txt.write('-----------------------\n')
    results_txt.write(f'Total Votes: {voterct}\n')
    results_txt.write('-----------------------\n')

# loops to calculate pct and find the winner
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)    
    for candidate in cand_totals:
        votesrec = cand_totals.get(candidate)
        votepct = (votesrec/voterct)*100
        pctofvote[candidate] = votepct

        # print each candidate to the terminal 
        print(f'{candidate}: {round(votepct,2)}% ({votesrec})')

        # print each to the txt file
        with open(results, 'a') as results_txt:
            results_txt.write(f'{candidate}: {round(votepct,2)}% ({votesrec})\n')

        if (votesrec > winner_tot):
            winner_tot = votesrec
            winner = candidate
        
        # used these print statements while testing my script
        # print(candidate)
        # print(votepct)
        # print(votesrec)
    # print(pctofvote)

# print winner to the terminal
print("--------------------------")
print(f'Winner is: {winner} with {winner_tot} votes')

# print winner to the txt file
with open(results, 'a') as results_txt:
    results_txt.write('-----------------------\n')
    results_txt.write(f'Winner is: {winner} with {winner_tot} votes')