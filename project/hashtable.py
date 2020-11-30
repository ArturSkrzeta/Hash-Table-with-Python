from random import randrange

class Hashtable:
    # Assumption: table_length is a prime number (for example, 5, 701, or 30011)
    def __init__(self, table_length):
        self.table = [None] * table_length # when table_length = 5 then [None,None,None,None.None]

    def __repr__(self):
        return f'{self.table}'

    def _search(self, key):
        hash1 = hash(key)                   # e.g. 743047066
        # print(f'{key} has been hashed with {hash1} during first hashing')
        m = len(self.table)                 # m = table_length = 5
        initial_i = hash1 % m               # initial_i's range: [0, m - 1] (inclusive) # e.g. [0, 4] inclusive
        # print(self.table[initial_i])      # None - when no key-value element
        # print(self.table[initial_i][0])   # key - when key-value element

        if not self.table[initial_i]: # if not None then true - there is no key-valye element but None
            return (False, initial_i) # it doesn't find the given key, it returns (False, the index where it would be inserted)
        elif self.table[initial_i][0] == key:
            return (True, initial_i) # it finds the given key in the table - True, and gives its index - initial_i

        # element collistion when index is taken => double-hashing.
        hash2 = hash(key + 'new')   # creating new hash
        # print(f'{key} has been hashed with {hash2} during second hashing')
        c = hash2 % (m - 1) + 1     # calculating step for searching free node
        i = (initial_i + c) % m     # index of node to check if free

        # searching for free node
        while i != initial_i:
            if not self.table[i]:
                return (False, i) # free node
            elif self.table[i][0] == key:
                return (True, i) # key-value element at node
            else:
                i = (i + c) % m

        return (False, -1) # The table is full when all nodes taken


    def insert(self, key, value):
        result = self._search(key)

        if result[1] == -1:
            msg = "Table is full"
            print(msg)
            return msg

        # If the key already exists, update the value.
        if result[0]:
            i = result[1] # taking index of existing key
            self.table[i][1] = value
            return

        # If key doesn't exit, it inserts it.
        i = result[1] # result[1] is the index where the new key-value pair should be inserted
        self.table[i] = [key, value]
        print(self.table)


    def search(self, key):
        result = self._search(key)

        # When key doesn't exist
        if not result[0]: # not False
            msg = "Given key doesn't exist."
            print(msg)
            return msg

        i = result[1]
        return self.table[i][1]


    def delete(self, key):
        result = self._search(key)

        # When key doesn't exist
        if not result[0]: # not False
            msg = "Given key doesn't exist."
            print(msg)
            return msg

        if result[0]:
            i = result[1]
            self.table[i] = None
            return


def main():

    table_size = 7
    keys = ['key' + str(i) for i in range(1,table_size+1)]
    vals = [randrange(100) for i in range(1,table_size+1)]

    ht = Hashtable(table_size)

    print("")
    print("Inserting data to Hash Table:")
    for key, val in zip(keys, vals):
        ht.insert(key, val)

    print("")
    print("Retrieving data from Hash Table:")
    for i in range(table_size):
        print(ht.search(keys[i]))

    print("")
    print("Testing Hash Table:")
    ht.insert('key11',99)   # --> table is full
    ht.insert('key12',199)  # --> table is full
    ht.search('key9')       # --> given key doesn't exist
    ht.delete('key9')       # --> given key doesn't exist


if __name__ == "__main__":
    main()
