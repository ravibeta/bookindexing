def oddone(text):
 fdist5 = FreqDist(text5)
 return sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7])
