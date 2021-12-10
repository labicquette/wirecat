import PySimpleGUI as sg
import sys
import parser
import protocols

def GUI(file=[]):
    sg.theme('DarkAmber')    # Keep things interesting for your users

    treedata = sg.TreeData() 
    decodedFile = {}

    if file != []:
        parsedFile = parser.parser(file)
        if 'Erreur' in parsedFile:
            dictToTree(treedata, parsedFile, '')
        else:
            decodedFile = protocols.decoder(parsedFile)
            dictToTree(treedata, decodedFile, '')


    layout = [[sg.Text('your files')],
              [sg.Input(key='-FILE-', visible=False, enable_events=True), sg.FileBrowse()],
               [sg.Tree(data=treedata,
                        headings=[],
                        auto_size_columns=True,
                        num_rows=30,
                        col0_width=100,
                        key='-TREE-',
                    show_expanded=False,
                    enable_events=True),
                ],
            [sg.Button('Exit')]]

    window = sg.Window('Wirecat', layout)

    while True:     # Event Loop
        event, values = window.read()
        if event == '-FILE-':
            print(values["-FILE-"])
            treedata = sg.TreeData()
            parsedFile = parser.parser(open(values[event]))
            if 'Erreur' in parsedFile:
                dictToTree(treedata, parsedFile, '')
            else:
                decodedFile = protocols.decoder(parsedFile)
                dictToTree(treedata, decodedFile, '')
            window['-TREE-'].update(values=treedata)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        print(event, values)
    window.close()
    return decodedFile

def noGUI(file=[]):
    if file == []:
        print("problem : no file", file)
    else :
        parsedFile = parser.parser(file)
        if 'Erreur' in parsedFile:
            print(parsedFile)
        else:
            decodedFile = protocols.decoder(parsedFile)
            print(decodedFile)
            return decodedFile


def dictToTree(Treedata, dictChamps, parentname):
    for i in dictChamps.keys():
        if type(dictChamps[i]) == dict:
            Treedata.Insert(parentname, parentname +  str(i), str(i) ,values = [], icon = None)
            dictToTree(Treedata, dictChamps[i], parentname+ str(i) )
        else :
            Treedata.Insert(parentname, parentname + str(i), str(i) + ' : ' + dictChamps[i], values = [], icon = None)

def dictToText(dictChamps, leftSpace, listChamps=[]):
    for i in dictChamps.keys():
        if type(dictChamps[i]) == dict:
            listChamps.append(leftSpace + str(i) +"\n")
            dictToText(dictChamps[i], leftSpace + "\t" , listChamps)
        else :
            listChamps.append(leftSpace + i + " : " +dictChamps[i]+ "\n")

def fileToTxt(decodedFile):
    print("fichier",decodedFile)
    resList = []
    dictToText(decodedFile, '', resList)
    print("resultatlist",resList)
    with open('output.txt', 'w') as f:
        f.writelines(resList)
        f.close()
