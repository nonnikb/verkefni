import random
words = ['foo', 'biology', 'sequence']
words = [''.join(random.sample(word, len(word))) for word in words]