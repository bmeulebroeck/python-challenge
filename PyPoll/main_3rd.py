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

    print(voterct)
    print(candidates)
    print(cand_totals)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)    
    for candidate in cand_totals:
        votesrec = cand_totals.get(candidate)
        votepct = (votesrec/voterct)*100
        pctofvote[candidate] = votepct

        if (votesrec > winner_tot):
            winner_tot = votesrec
            winner = candidate
        
        # print(candidate)
        # print(votepct)
        # print(votesrec)
        # with open(results, 'w') as results_txt:
        #     results_txt.write(f'{candidate}: {round(votepct,2)}% ({votesrec})')
    print(pctofvote)

with open(results, 'w') as results_txt:
    results_txt.write('Election Results:\n')
    results_txt.write('-----------------------\n')
    results_txt.write(f'Total Votes: {voterct}\n')
    results_txt.write('-----------------------\n')
    results_txt.write(f'{candidate}: {round(votepct,2)}% ({votesrec})\n')
    results_txt.write('-----------------------\n')
    results_txt.write(f'Winner is: {winner} with {winner_tot} votes')


    




#     election_results=(f'Election Results:'
#         f'----------------------------'
#         f'Total Votes: {voterct}'
#         f'----------------------------')


        # if candidate == "Khan":
        #     khan = khan + 1
        # if candidate == "Correy":
        #     correy = correy + 1
        # if candidate == "Li":
        #     li = li + 1
        # if candidate == "O'Tooley":
        #     otooley = otooley + 1

    # khanpct = (khan/voterct)*100
    # correypct = (correy/voterct)*100
    # lipct = (li/voterct)*100
    # otooleypct = (otooley/voterct)*100

    #tallylist = ["Khan":khan, kahnpct, "Correy":correy, correypct, "Li":li, lipct, "O'Tooley":otooley, otooleypct]
    #print(tallylist)


#     print("Election Results:")
#     print("--------------------------------")
#     print(f'Total Votes: {voterct}')
#     print("--------------------------------")
#     print(f'Khan: {round(khanpct, 2)}%, {khan}')
#     print(f'Correy: {round(correypct, 2)}%,{correy}')
#     print(f'Li: {round(lipct,2)}%, {li}')
#     print(f"O'Tooley {round(otooleypct,2)}%, {otooley}")
#     print("--------------------------------")


#     sorted(candidates)


#     unique_cand = []

#     for cand in candidates:
#         if cand not in unique_cand:
#             unique_cand.append(cand)
    
#     print(unique_cand)

# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')

#     csv_header = next(csvfile)
#     #votefor = 0
#     votesfor = []

#     for row in csvfile:
#         ucand = unique_cand[]
#         if str(row[2]) == str(ucand):
#             votefor = votefor + 1
#         votesfor.append(votefor)
#         #votefor = 0


#     print(votesfor)

