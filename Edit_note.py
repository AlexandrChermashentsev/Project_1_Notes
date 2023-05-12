import sys
import fileinput

def Replace_text_in_note():




    
    x = input("Enter text to be replaced:")
    y = input("Enter replacement text")
 
    for l in fileinput.input(files = "file.txt"):
        l = l.replace(x, y)
        sys.stdout.write(l)