import csv

def write_csv(file_name,rows,heders=None):

    with open(file_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=',')
        csvwriter.writerow(heders)
        csvwriter.writerows(rows)

if __name__ == "__main__":
    rows = [(101, 'Ravi'), (102, 'Mavi'), (103, 'Pavi')]
    heders = ["id", "name" ]
    write_csv(rows,heders)


