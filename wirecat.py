import parser as p
import graphics
import sys
import argparse

"""to do :
    protocols 
    save file ?
    noGui 
    get file through gui
"""




def main(argv):

    argParser = argparse.ArgumentParser(description='Show frame information')
    argParser.add_argument("-ng","--nogui", action="store_true",
                            help="No GUI")
    #argParser.add_argument('-f', "--file", dest="file" ,action="store_const",
    #const=f,help="Path to file of you frame")
    argParser.add_argument('file', nargs='?', type=argparse.FileType('r'), help="Path to file")



    args = argParser.parse_args()


    #file = "tramedns.txt"
    #Bytes = p.parser(file)

    if args.nogui:
        print("NOGUI")
        if args.file:
            graphics.noGUI(args.file)
        else:
            argParser.print_help()
    else :
        print("GUI")
        if args.file:
            graphics.GUI(args.file)
        else :
            graphics.GUI()


if __name__ == "__main__":
    main(sys.argv[1:])