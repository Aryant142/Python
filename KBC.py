 
i = 1
while i < 3:
    a = input("Please enter your name: ") 
    print("Now you have to answer three questions.")
    print("If you are wrong, you will be terminated.")
    print("Each question is worth 1000 Rs.")

    # Question 1
    print(f"Q{i}: What is the age of Narendra Modi?")
    print("a. 73  b. 74  c. 75  d. 76") 
    ans = input("Write the correct option: ")

    if ans == 'a':
        print("Good, your answer is correct! You won 1000 Rs.")
    else:
        print("You were wrong, and as per the rules, you are terminated.")
        break
    i+=1
    # Question 2
    print(f"Q{i}: Who was the third Prime Minister of India?")
    print("a. Jawaharlal Nehru  b. Gulzarilal Nanda  "
                  "c. Lal Bahadur Shastri  d. Indira Gandhi")
    ans = input("Write the correct option: ")

    if ans == 'c': 
        print("Good, your answer is correct! You won 2000 Rs.") 
    else:
        print("You were wrong, and as per the rules, you are terminated.")
        break
    i+=1
    # Question 3
    print(f"Q{i}: Which is the oldest river in India?")
    print("a. Narmada  b. Ganga  c. Yamuna  d. Brahmaputra") 
    ans = input("Write the correct option: ")

    if ans == 'a':
        print("Good, your answer is correct! You won 3000 Rs.")
    else:
        print("You were wrong, and as per the rules, you are terminated.")
        break

    # Incrementing `i` for loop progression
    i +=1

        
     
     
