# function for conversion of url
def converturl():
    userint = input("Enter the url in the form of 'https://www. + your input: ")

    if userint.startswith("https://www."):
        userurl = userint[12:]
        convertedurl = userurl + ".com"
        
        print("converted Url is: ", convertedurl)
    else:
        print("Invalid Url format, make sure its correct.")
        
        
converturl()
