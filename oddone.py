text = 'Clustering and Segmentation. Clustering is a data mining technique that is directed towards the goals of identification and classification. Clustering tries to identify a finite set of categories or clusters to which each data object (tuple) can be mapped. The categories may be disjoint or overlapping and may sometimes be organized into trees. For example, one might form categories of customers into the form of a tree and then map each customer to one or more of the categories. A closely related problem is that of estimating multivariate probability density functions of all variables that could be attributes in a relation or from different relations.'
import nltk
from nltk.corpus import wordnet as wn

def indexWordNetSimilarity(txt):
    fdist = nltk.FreqDist(txt)
    total = len(text)
    count = 0;
    # fdist.plot(n, cumulative=True)
    vocabulary = sorted([w for w in fdist.keys() if (len(w) > 5 and fdist[w] > 2)])
    candidates = []
    import itertools
    for i in itertools.product(vocabulary, vocabulary):
        t = i, wn.synsets(i[0])[0].path_similarity(wn.synsets(i[1])[0])
        if (t[1] > 0.2 and t[1] < 1.0):
            candidates.append(t[0][0])
            candidates.append(t[0][1])
        candidates = sorted(set(candidates))
    return candidates

print indexWordNetSimilarity(text.split())
 
def indexBiGram(text, commonwords):
  V = text.collocations()
  fdist6 = FreqDist([text.count(w) for w in V])
  vocabulary = sorted([w for w in set(text) if ( w not in commonwords || (len(w) > 7 and fdist6[w] > 7)])
  return vocabulary[:50]
  
def indexUniGramContextBased(text, commonwords):
 words = sorted([w for w in set(text) if (w not in commonwords)])
 fdist7 = FreqDist([w for w in text.concordance([v for v in words]))
 vocabulary = sorted([w for w in set(words) if ( fdist7[w] > 7))
 return vocabulary[:50]
 
def indexConditionalFreqDist(text, commonwords):
  vocabulary = IndexUniGram(text, commonwords)
  cfd = nltk.ConditionalFreqDist(
            (category, word)
             for category in text.categories()
             for word in text.words(categories=category))
  l = len(text)
  category = [text[1:l/3], text[(l/3)+1:2*l/3], text[(2*1/3)+1, l]]
  return cfd.tabulate(conditions = category, samples = vocabulary)
  
  from nltk.corpus import wordnet as wn
    
  def indexUnstructuredDocument(text, commonwords)
   V =  indexUniGram(text, commonwords)
   fdist = FreqDist([m for t in v if (t != v && m = v.path_similarity(t))])
   l = [ t for v in V if fdist(v).max() ]
   return l[:50]
# view the document as sections
# pick out salient words based on fequency
# use the wordnet to find the common ancestor
# if the ancestor changes on a rolling basis such as in a novel
# adhust the section size and list one word per section.
  
  def indexStructuredDocument(text, commonwords)
    return indexUniGram(textHeading, commonwords).Intersect(indexUniGram(textSubHeadings, commonwords))

