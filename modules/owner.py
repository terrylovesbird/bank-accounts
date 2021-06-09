import csv

class Owner():
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    @classmethod
    def all_owners(cls):
        owners = []
        with open("./support/owners.csv") as owners_file:
            data = csv.reader(owners_file)
            for line in data:
                id = int(line[0])
                name = line [2] + line[1]
                address = line[3] + ", " + line[4] + ", " + line[5]

                owner = cls(id, name, address)
                owners.append(owner)
            
        return owners