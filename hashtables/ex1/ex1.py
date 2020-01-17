#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    
    weights is a list of item weights
    limit is a weight limit. 
    this will check the list of items to see if 2 
    of the items in the weights list can equal the limit
    
    """
    # for each item in weights less than the limit, at it to the table as a linked pair with the index as the key.
    for i in range(length):
        if weights[i] < limit:
             hash_table_insert(ht, weights[i], i)

    # loop through again, search the hash table for the limit minus the weight to see if we can find a matching number
    for index, weight in enumerate(weights):
        #defines what we're searching for
        need = limit - weight
        #searches for it
        found = hash_table_retrieve(ht, need)
        #organizes the results in the way the spec asks.
        if found:
            if index>found:
                return (index,found)
            else:
                return (found,index)
    #if we find nothing, returns None.
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
