import sys # DO NOT EDIT THIS OR YOU WILL GET A ZERO


def translate(word):
    '''
    This function should return the Pig Latin translation of the word passed in,
    i.e. translate('python') should return 'ythonpay'
    '''
    ok = ""
    if word.endswith("\n"):
        word = word[:-1]

    line = list(word)
    line.append(line[0])
    line.remove(line[0])
    line.append("a")
    line.append("y")
    for i in line:
        ok += i
    return ok


if __name__ == '__main__':
    # file_name is the name of the English input file, passed in via the first command line argument
    if len(sys.argv) < 2:
        raise Exception('you should have used one command line argument, i.e, python3 main.py argument')
    
    # Start out by reading in the input file
    file1 = open('gay.txt',"r")
    file2 = open('ok.txt', "w")
    # Then iterate over each word in the file and translate
    for line in file1:
        file2.write(translate(line))
        file2.write("\n")
    
    file1.close()
    file2.close()

    # Finally, write your translation to a file called my_out.igpay
    # One line of English input should correspond to one line of Pig Latin output