def indexUniGram(text):
 fdist5 = FreqDist(text5)
 fdist5.hapaxes()
 vocabulary = sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])  
 return vocabulary[:50]
 
 def indexBiGram(text):
  V = text.collocations()
  fdist6 = FreqDist([text.count(w) for w in V])
  v = sorted([w for w in set(text) if len(w) > 7 and fdist6[w] > 7])
  return v[:50]
  
