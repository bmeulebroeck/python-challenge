import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
analysis = os.path.join("Resources", "analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    rowcount = 0
    totalpl = 0

    for row in csvreader:
        pl = int(row[1])
        rowcount = rowcount + 1
        totalpl = totalpl + pl

    print("Financial Analysis")
    print("------------------------------")    
    print(f'Total months: {rowcount}')
    print(f'Total: ${totalpl}')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    prevpl = 0
    monthchg = []

    grtinc = 0
    grtdec = 0

    for row in csvreader:
        currentpl = int(row[1])
        netchg = currentpl - prevpl
        monthchg.append(netchg)
        if netchg > grtinc:
            grtinc = netchg
            grtincmth = str(row[0])
        if netchg < grtdec:
            grtdec = netchg
            grtdecmth = str(row[0])
        prevpl = currentpl

    avgchg = sum(monthchg)/len(monthchg)
    # print(sum(monthchg))
    # print(len(monthchg))
    # print(avgchg)

    print(f'Average Change: ${(round(avgchg, 2))}')
    print(f'Greatest Increase in Profits: {grtincmth} ${grtinc}')
    print(f'Greatest Decrease in Profits: {grtdecmth} ${grtdec}')

with open(analysis, 'w') as analysis_txt:
    analysis_txt.write("Financial Analysis\n")
    analysis_txt.write("------------------------------\n")
    analysis_txt.write(f'Total months: {rowcount}\n')
    analysis_txt.write(f'Total: ${totalpl}\n')
    analysis_txt.write(f'Average Change: ${(round(avgchg, 2))}\n')
    analysis_txt.write(f'Greatest Increase in Profits: {grtincmth} ${grtinc}\n')
    analysis_txt.write(f'Greatest Decrease in Profits: {grtdecmth} ${grtdec}\n')
