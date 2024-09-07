def write_ques_to_file():
    try:
        sentence = input("Please Enter A Question: ")
        if sentence.strip().endswith('?'): 
            with open('Qs.txt', 'a') as fileObj:
                fileObj.write(sentence + "\n") 
            print("Question has been added to the file")
        else:
            print("NO QUESTION HENCE REMOVED")
    except:
        print("Error: unable to open file")
        
write_ques_to_file()
