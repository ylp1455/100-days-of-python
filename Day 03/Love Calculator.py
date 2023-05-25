# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1 = name1.lower()
name2 = name2.lower()

# Count the occurrences of letters in "TRUE" in both names
true_count = name1.count('t') + name2.count('t')
true_count += name1.count('r') + name2.count('r')
true_count += name1.count('u') + name2.count('u')
true_count += name1.count('e') + name2.count('e')

# Count the occurrences of letters in "LOVE" in both names
love_count = name1.count('l') + name2.count('l')
love_count += name1.count('o') + name2.count('o')
love_count += name1.count('v') + name2.count('v')
love_count += name1.count('e') + name2.count('e')

# Calculate the love score
love_score = int(str(true_count) + str(love_count))

# Determine the message based on the love score
if love_score < 10 or love_score > 90:
    message = f"Your score is {love_score}, you go together like coke and mentos."
elif 40 <= love_score <= 50:
    message = f"Your score is {love_score}, you are alright together."
else:
    message = f"Your score is {love_score}."

# Print the final message
print(message)