
dict={  0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
mobile=input("enter the mobile nuber:")
for i in mobile:
    word_format=dict[int(i)]
    print(word_format , end="")