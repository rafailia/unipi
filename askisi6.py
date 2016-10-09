"""
Name          :Rafailia
Surname       :Ioannou
Programm Title: Rearrange sentence.
Date          :30/09/16
Description   :
"""
import sys
print("Input your sentence and \" at begin and the end. Separate the words by space. Sample \"This is a sentence input for the program\"");
#Read the sentence
try:
	sentence=str(input());
except Exception:
		print("Oops! Something went wrong. Try again...");
		sys.exit();
words=sentence.split(" ");
output_sentence="";
added_str="argh";
new_word="";
for word in words:
	isWord=True;	
	for letter in word:
		if(letter.isalpha()==False):
			isWord=False;
	if(isWord):
		firstCharacter=word[0];
		new_word+=word[1:] + firstCharacter + added_str + " ";
	else:
		new_word+=word + " ";
print(new_word);
