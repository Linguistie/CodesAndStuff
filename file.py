def second_sentence_word_average(randomtext): 
    print('q1') 
    sentences = [] 
    char_num = 0 
    word_num = 0
    print('q')
    for sentence in randomtext.split("."): 
        if len(sentence) > 0: 
            sentences.append(sentence.strip(" "))
    print("sentences of text:")         
    for i in range(len(sentences)):
        print(sentences[i])
    print("second sentence of text:")    
    print(sentences[1])
    for word in sentences[1].split():
        word_num += 1
        for char in word:
            char_num+=1            
    print("number of words in 2nd sentence = "+str(word_num))
    print("number of chars in 2nd sentence = "+str(char_num))
    ave = float(char_num)/ float(word_num)
    print("Average word length in 2nd sentence = "+str(ave))    


##    file = open("text1.txt",'w') 
##    file.write(randomtext + "\n") 
##    file.write("Average word length in 2nd sentence: %s" % (ave)) 
##    file.close() 
##    print(randomtext)
    
file = open("text.txt") 
text = file.read()
file.close()
print("text: ")
print(text)
print("q2") 
second_sentence_word_average(text)
