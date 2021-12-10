#!/usr/bin/env python3
import parser as p
import graphics
import sys
import argparse

"""to do :
    protocols 
    save file ?
"""




def main(argv):

    argParser = argparse.ArgumentParser(description='Show frame information')
    argParser.add_argument("-ng","--nogui", action="store_true",
                            help="No GUI")
    argParser.add_argument('file', nargs='?', type=argparse.FileType('r'), help="Path to file")

    argParser.add_argument("-o","--output", action="store_true",
                            help="Writes information in new file")

    args = argParser.parse_args()


    returnValue = []
    if args.nogui:
        print("NOGUI")
        if args.file:
            returnValue = graphics.noGUI(args.file)
        else:
            returnValue = argParser.print_help()
    else :
        print("GUI")
        if args.file:
            returnValue = graphics.GUI(args.file )
        else :
            returnValue = graphics.GUI()

    if args.output:
        if returnValue != []:
            graphics.fileToTxt(returnValue)


if __name__ == "__main__":
    main(sys.argv[1:])