class HashTable:
    # Initialize a new hash table.
    def __init__(self):
        # Store all key-value pairs in a dictionary.
        #
        # The outer dictionary uses the computed hash value as its key.
        # Each hash value points to an inner dictionary that stores the
        # original key-value pairs.
        #
        # Example:
        # {
        #     424: {
        #         'golf': 'sport'
        #     }
        # }
        self.collection = {}

    # Compute a simple hash value for a string key.
    def hash(self, string):
        # ord(char) returns the Unicode value of one character.
        #
        # Example:
        # 'golf' -> ord('g') + ord('o') + ord('l') + ord('f')
        #        -> 103 + 111 + 108 + 102
        #        -> 424
        return sum(ord(char) for char in string)

    # Add a key-value pair to the hash table.
    def add(self, key, value):
        # Convert the original key into a numeric hash value.
        hashed_key = self.hash(key)

        # If this hash value does not exist yet, create a new bucket.
        #
        # A bucket is an inner dictionary that stores all original keys
        # that produce the same hash value.
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        # Store the original key and its value inside the bucket.
        #
        # This design handles collisions because different keys can have
        # the same hash value.
        #
        # Example:
        # hash('fcc') == 300
        # hash('cfc') == 300
        #
        # {
        #     300: {
        #         'fcc': 'coding',
        #         'cfc': 'chemical'
        #     }
        # }
        self.collection[hashed_key][key] = value

    # Remove a key-value pair from the hash table.
    def remove(self, key):
        # Compute the hash value for the key that should be removed.
        hashed_key = self.hash(key)

        # Only remove the key if:
        # 1. the hash bucket exists, and
        # 2. the original key exists inside that bucket.
        #
        # This prevents KeyError when the key does not exist.
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            # Delete only the specific key-value pair.
            #
            # Do not delete the whole bucket, because another key may have
            # the same hash value.
            del self.collection[hashed_key][key]

    # Look up a value by its original key.
    def lookup(self, key):
        # Compute the hash value for the lookup key.
        hashed_key = self.hash(key)

        # Return the stored value only if both the bucket and the original
        # key exist.
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]

        # Return None when the key is not found.
        #
        # This also handles collision cases correctly. For example, if
        # 'fcc' exists but 'cfc' does not, lookup('cfc') should still
        # return None even though both keys produce the same hash value.
        return None
