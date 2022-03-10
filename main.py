import pandas as pd
from itertools import combinations

def flatten_items(tuplesList):
    flattenedList=list(sum(tuplesList,()))
    items = list(set(flattenedList))
    return items


def generateFirstSupportCount(df):
    initialSupportCount = df.apply(pd.value_counts)
    initialSupportCount['total'] = initialSupportCount.sum(axis=1)
    initialSupportCount = initialSupportCount['total'].transpose().to_dict()
    return initialSupportCount

def generateCandidateItemset(itemset, subsetSize):
    candidateItemset=list(combinations(itemset,subsetSize))
    return  candidateItemset

def prune(supportCountDictionary, minimumSupport):
    for key in list(supportCountDictionary.keys()):
        if supportCountDictionary[key] < minimumSupport:
            del supportCountDictionary[key]
    return  supportCountDictionary

def apriori(Datalist, candidateItemset, minSupport, k):
    supporCountDictionary = dict()
    currentFreqItemset = candidateItemset
    while True:

        supporCountDictionary.clear()
        for eachSet in candidateItemset:
            counter = 0
            for eachRow in Datalist:
                if all(x in eachRow for x in eachSet):
                    counter += 1

            supporCountDictionary[tuple(eachSet)] = counter

        supporCountDictionary = prune(supporCountDictionary, minSupport)
        items = flatten_items(supporCountDictionary.keys())
        if len(supporCountDictionary) == 0:
            break

        candidateItemset = generateCandidateItemset(items, k)
        currentFreqItemset=items
        k += 1

    return currentFreqItemset


transactions=[
    ['e','k','m','n','n','o','y'],
    ['d','e','k','n','o','y'],
    ['a','e','k','m'],
    ['c','k','m','u','y'],
    ['c','e','i','k','o','o']
]
Data=pd.DataFrame(transactions)

minSupport=int(input("Enter minimum support:"))

k=2
initialSupportCount=generateFirstSupportCount(Data)
prune(initialSupportCount, minSupport)
items=list(initialSupportCount.keys())

firstCandidateItemset=generateCandidateItemset(items, k)
DataList=Data.to_numpy().tolist()
print('Frequent itemset is:')
print(apriori(DataList,firstCandidateItemset,minSupport,k))










