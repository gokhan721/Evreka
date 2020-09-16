from model import Collections

def getCollectionFrequencies():
    collection_frequencies = Collections.objects.values_list('collection_frequency', flat=True)
    return list(collection_frequencies)
