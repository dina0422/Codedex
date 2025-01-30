FILE_NAME = 'Intermediate Python/File Input Output/08. Uncharted Files/sent_message.txt'
sent_message = 'Hey there! This is a secret message.'

with open(FILE_NAME, 'w') as file:
  file.write(sent_message)
  
with open(FILE_NAME, 'r+') as file:
    #read the file
    original_message = file.read()
    
    #move cursor to the start of the file
    file.seek(0)
    
    #modify message to simulate unsending   
    unsent_message = 'This message has been unsent.'

    file.truncate(len(unsent_message))
    file.write(unsent_message)
    
    print(f'Original message: {original_message}')
    print(f'Unsent message: {unsent_message}')