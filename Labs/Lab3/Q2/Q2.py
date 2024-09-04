def replace_in_file(filename, search_phrase, replace_phrase):
    try:
        
        with open(filename, 'r') as file:
            content = file.read()
        
        
        modified_content = content.replace(search_phrase, replace_phrase)
        
        
        with open(filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Successfully replaced '{search_phrase}' with '{replace_phrase}' in '{filename}'")
    
    except FileNotFoundError:
        print("Error: File could not be found")
    except IOError:
        print("Error: IO error occurred while reading or writing the file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filename = 'example.txt'
search_phrase = 'rdr2'
replace_phrase = 'new_word'

replace_in_file(filename, search_phrase, replace_phrase)
