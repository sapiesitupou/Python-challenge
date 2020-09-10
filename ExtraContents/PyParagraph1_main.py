import os
from pathlib import Path 

file_path = Path(".." , "ExtraContents", "Resources", "Raw_data_paragraph_1.txt")


with open(file_path) as text:
    paragraph = text.read()

words = len([w for w in paragraph.split(sep=" ")])

sentences = len([w for w in paragraph if w == "."]) + len([w for w in paragraph if w == "?"]) +  len([w for w in paragraph if w == "!"])

letter_avg_per_word = len([c for c in paragraph if c.isalpha()])/words

avg_words_per_sentence = words/sentences

# ----------------------------------------------------------------------------
print(f"Paragraph Analysis")
print(f"---------------------------------------------")
print(f"Approximate Word Count: {words}")
print(f"Approximate Sentence Count: {sentences}")
print(f"Average Letter Count: {letter_avg_per_word}")
print(f"Average Sentence Length: {avg_words_per_sentence}")


output_file = Path("..", "ExtraContents", "Paragraph1_Analysis.txt")

with open(output_file,"w") as file:

    file.write("\n")
    file.write(f"Paragraph Analysis")
    file.write("\n")
    file.write(f"----------------------------------------------")
    file.write("\n")
    file.write(f"Approximate Word Count: {words}")
    file.write("\n")
    file.write(f"Approximate Sentence Count: {sentences}")
    file.write("\n")
    file.write(f"Average Letter Count: {letter_avg_per_word}")
    file.write("\n")
    file.write(f"Average Sentence Length: {avg_words_per_sentence}")