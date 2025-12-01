class hashset:
    def __init__(self):
        self.hash_table_size = 7
        self.bucket = [None for _ in range(self.hash_table_size)]
        self.total_insertions = 0
        self.total_collisions = 0
        self.total_rehashing = 0

    # Helper functions for finding prime numbers
    def isPrime(self, n):
        i = 2
        while (i * i <= n):
            if (n % i == 0):
                return False
            i = i + 1
        return True

    def nextPrime(self, n):
        while (not self.isPrime(n)):
            n = n + 1
        return n

    def formerPrime(self, n):
        while n >= 2:
            n -= 1
            if self.isPrime(n):
                return n
        return 2

    # Hash function
    def hashCode(self, key):
        keylength = len(key)
        constant = 31
        hashcode = 0
        for i in range(keylength):
            hashcode += ord(key[i]) * constant**(keylength - i - 1)
        return hashcode

    # Compression function
    def compression(self, key):
        if ((self.hash_table_size % 2 == 0) and self.hash_table_size != 0):
            hashvalue = self.hashCode(key) & (self.hash_table_size - 1)
            return hashvalue
        else:
            hashvalue = self.hashCode(key) % self.hash_table_size
        return hashvalue

    def doubleHashingCompression(self, key):
        prime = self.formerPrime(self.hash_table_size)
        hashvalue = self.hashCode(key) % prime
        return hashvalue

    # Rehashing
    def rehash(self):
        old_table = self.bucket
        self.hash_table_size = self.nextPrime(self.hash_table_size * 2)
        self.bucket = [None for _ in range(self.hash_table_size)]
        self.total_insertions = 0

        for bucket in old_table:
            if bucket is not None:
                self.insert(bucket)
        self.total_rehashing += 1

    # Collision resolution
    def linearProbing(self, bucketIndex):
        initialIndex = bucketIndex
        i = 1
        while self.bucket[bucketIndex] is not None:
            self.total_collisions += 1
            bucketIndex = (initialIndex + i) % self.hash_table_size
            if bucketIndex == initialIndex:
                break
            i += 1
        return bucketIndex

    def quadraticProbing(self, bucketIndex):
        initialIndex = bucketIndex
        i = 1
        while self.bucket[bucketIndex] is not None:
            self.total_collisions += 1
            bucketIndex = (initialIndex + (i ** 2)) % self.hash_table_size
            i += 1
        return bucketIndex

    def doubleHashing(self, bucketIndex, value):
        initialIndex = bucketIndex
        i = 1
        while self.bucket[bucketIndex] is not None:
            self.total_collisions += 1
            bucketIndex = (initialIndex + (i * self.doubleHashingCompression(value))) % self.hash_table_size
            i += 1
        return bucketIndex

    # Insert
    def insert(self, value):
        if self.total_insertions >= self.hash_table_size * 0.5:
            self.rehash()

        bucketIndex = self.compression(value)

        if self.bucket[bucketIndex] is None or not self.find(value):
            if (self.mode == HashingModes.HASH_1_COLLISION_1.value):
                bucketIndex = self.linearProbing(bucketIndex)
            elif (self.mode == HashingModes.HASH_1_COLLISION_2.value):
                bucketIndex = self.quadraticProbing(bucketIndex)
            elif (self.mode == HashingModes.HASH_1_COLLISION_3.value):
                bucketIndex = self.doubleHashing(bucketIndex, value)
            self.bucket[bucketIndex] = value
            self.total_insertions += 1

    # Find
    def find(self, value):
        bucketIndex = self.compression(value)
        initialIndex = bucketIndex

        i = 1
        while self.bucket[bucketIndex] is not None:
            if self.bucket[bucketIndex] == value:
                return True
            bucketIndex = (initialIndex + i) % self.hash_table_size
            if bucketIndex == initialIndex:
                return True
            i += 1
        return False

    # Print functions
    def print_set(self):
        print("Hashset:\n")
        for i in range(len(self.bucket)):
            if self.bucket[i] is not None:
                print(f"\t{i}: {self.bucket[i]}")

    def print_stats(self):
        print(f"Total number of collisions: {self.total_collisions}")
        print(f"Total number of rehashing: {self.total_rehashing}")
        if self.total_rehashing == 0:
            print("Average number of collision per rehash: 0")
        else:
            print(f"Average number of collision per rehash: {self.total_collisions / self.total_rehashing:.2f}")



if __name__ == "__main__":
    hs = hashset()
    hs.insert("apple")
    hs.insert("banana")
    hs.insert("cherry")
    hs.insert("orange")

    hs.print_set()
    hs.print_stats()

    print("Find apple:", hs.find("apple"))
    print("Find grape:", hs.find("grape"))
