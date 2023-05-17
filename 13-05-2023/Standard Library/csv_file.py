import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["trandaction_id", "product_id","price"])
    writer.writerow([1000,2,5])
    writer.writerow([1001,2,7])
    writer.writerow([1002,2,9])
    

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(reader)
