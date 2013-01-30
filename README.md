bookindexing
============

This is the placeholder for automated book indexing with inspiration from python NLTK fràmework.
Here is a NLTK sample:
1 import nltk
2 def extract_entities(text):
3     for sent in nltk.sent_tokenize(text):
4         for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
5             if hasattr(chunk, 'node'):
6                 print chunk.node, ' '.join(c[0] for c in chunk.leaves())
