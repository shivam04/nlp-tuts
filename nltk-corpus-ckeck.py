import nltk
text_file=nltk.corpus.gutenberg.words('melville-moby_dick.txt')
my_lines_list=[]
for line in text_file:
    my_lines_list.append(line)
print(my_lines_list)