class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class DictionaryADT:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def _hash_function(self, key):
        return sum(ord(char) for char in key) % self.size
    # the hash function used is a simple one that sums the ASCII 
    # values of the characters in the key and takes the modulo of 
    # the sum with the size of the hash table.

    def insert(self, key, value):
        hash_key = self._hash_function(key)
        entry = KeyValuePair(key, value)
        for i in range(self.size):
            if self.hash_table[hash_key] is None :
                self.hash_table[hash_key] = entry
                print("Word added successfully at index", hash_key, ":", entry.key, entry.value)
                return
            else:
                hash_key = (hash_key + 1) % self.size
                #linear probing technique

    def find(self, key):
        hash_key = self._hash_function(key)
        for i in range(self.size):
            if self.hash_table[hash_key] is not None and self.hash_table[hash_key].key == key:
                print("Word:", self.hash_table[hash_key].key, "\tMeaning:", self.hash_table[hash_key].value)
                return
            else:
                hash_key = (hash_key + 1) % self.size
        print("Word not found!")

    def delete(self, key):
        hash_key = self._hash_function(key)
        for i in range(self.size):
            if self.hash_table[hash_key] is not None and self.hash_table[hash_key].key == key:
                print("Word:", self.hash_table[hash_key].key, "\tMeaning:", self.hash_table[hash_key].value, "\tHas been DELETED!!")
                self.hash_table[hash_key] = None
                return
            else:
                hash_key = (hash_key + 1) % self.size
        print("Word doesn't exist!")

def main():
    size = int(input("How many words do you want to enter: "))
    dictionary = DictionaryADT(size)
    for i in range(size):
        word = input("\nEnter the word to be entered: ")
        meaning = input("Enter the meaning of the word: ")
        dictionary.insert(word, meaning)
    while True:
        ch= input("DO you want to search word(y/n): ")
        if(ch=='y'):
            search_word = input("\nEnter the word to be searched: ")
            dictionary.find(search_word)
        else:
            break

main()
