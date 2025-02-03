input_file_path = r"C:\Users\reema\Desktop\python\Basics\Text_file_for_testing.txt" ## WE added r before path to convert normal string into raw string 
output_file_path = r"C:\Users\reema\Desktop\python\Basics\Text_file_for_testing.txt"

with open(input_file_path, "r") as file: #Opening the file in read mode
    sentence = file.read().strip() #Reading the file and removing and leading and trailing whitespaces
    words = sentence.split()       #splitting the string sentence into a list called words at whitespaces 
    word_count = len(words)        # counting the number of words present in our text file
    reverse_sentence = " ".join(words[::-1]) #reversing the list of words and putting them back together into a string
    output_content = f"Reverse Sentence: {reverse_sentence}\nwords: {word_count}"
with open(output_file_path, "w") as file:  #Opening the file in write mode
    file.write(output_content)
print("Done successfully! Please check output page")
print(output_file_path)