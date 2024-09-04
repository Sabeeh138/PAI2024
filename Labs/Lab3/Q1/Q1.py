def counterch(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            charactercount = len(content)
            
            wordcount = len(content.split())  
            
            print(f"Total characters are {charactercount}")
            print(f"Total word count is {wordcount}")
        
    except FileNotFoundError:
        print("Error: File could not be found")
    except IOError:
        print("Error: IO error found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filename = 'idk.txt'
counterch(filename)
