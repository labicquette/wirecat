import parser as p
import graphics
import sys
import time 
def main(argv):
    timer = time.process_time()
    file = "tramedns.txt"
    Bytes = p.parser(file)
    graphical = True
    if len(sys.argv) == 2 :

    if 

    if graphical :
        print("graphics")
        #graphics.pythonGUI()
        graphics.pythonGUI()
    else :
        print("noGraphics")
    print(Bytes)
    print(time.process_time()- timer)

if __name__ == "__main__":
    main(sys.argv[1:])