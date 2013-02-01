def oddone(text5):
 fdist5 = FreqDist(text5)
  vocabulary = sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])
  return vocabulary[:50]
  
