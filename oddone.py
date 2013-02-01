def indexUniGram(text, commonwords):
 fdist5 = FreqDist(text5)
 fdist5.hapaxes()
 vocabulary = sorted([w for w in set(text5) if ( w not in commonwords || (len(w) > 7 and fdist5[w] > 7))])  
 return vocabulary[:50]
 
 def indexBiGram(text):
  V = text.collocations()
  fdist6 = FreqDist([text.count(w) for w in V])
  vocabulary = sorted([w for w in set(text) if ( w not in commonwords || (len(w) > 7 and fdist6[w] > 7)])
  return vocabulary[:50]
  
def IndexUniGramContextBased(text, commonwords):
 words = sorted([w for w in set(text) if (w not in commonwords)]);
 fdist7 = FreqDist([w for w in text.concordance([v for v in words]))
 vocabulary = sorted([w for w in set(words) if ( fdist7[w] > 7))
 return vocabulary[:50]
 
 
