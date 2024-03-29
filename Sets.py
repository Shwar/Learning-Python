#Unordered- no element position
#Have only unique items- one item of a particular type

#method set() converts list to set

set1 =set([1,3.5,'John'])

#Methods add and remove

set1.add("Ndere")

set1.remove(1)

'John' in set1  #To verify if an element is in the set

set2 = {1,3.5,'Daniel'}

set3 = set1 & set2

#Perform various operations on sets: `union`, `intersection`, `difference`, symmetric difference

unions = set2.union(set1)
 
intersect = set1.intersection(set2)

unique_set = set2.difference(set1)

#Subset and superset checking methods
is_subset = set1.issubset(set2)

is_superset = set2.issuperset(set1)

#Method discard used to remove specific item from the set it ignores if element not found

set2.discard(1)

#Remove method used to remove specific item but raises a KeyError if not found

set1.remove("James")  # Raises an error