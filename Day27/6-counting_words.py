sentence="What is the Airspace Velocity of an Unladen Swallow?"

word_list=sentence.split(' ')

# [word for word in sentence if word==' ']

print(word_list)

word_count={word:len(word) for word in word_list}
print(word_count)