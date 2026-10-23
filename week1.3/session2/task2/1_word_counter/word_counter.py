# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file
with open("week1.3/session2/task2/1_word_counter/story.txt", "r") as f:
    text = f.read()
# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

words = text.split()
wordcount = len(words)
print(f"Word count for story.txt: {wordcount}")

# Another way. to do this 
with open("week1.3/session2/task2/1_word_counter/story.txt", "r") as files:
    total_words = 0
    for line in files:
        words = line.split()
        total_words += len(words)

print(f"Total word count: {total_words}")

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210