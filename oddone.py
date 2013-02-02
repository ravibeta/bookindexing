def indexUniGram(text, commonwords):
 fdist5 = FreqDist(text5)
 fdist5.hapaxes()
 vocabulary = sorted([w for w in set(text5) if ( w not in commonwords || (len(w) > 7 and fdist5[w] > 7))])  
 return vocabulary[:50]
 
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

  
