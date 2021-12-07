import PySimpleGUI as sg
import sys
import parser
import protocols

def GUI(file=[]):
    sg.theme('DarkAmber')    # Keep things interesting for your users





    #dictionnaire={"chocolat":{"feves": "saucisse","kebab":{"75 paname" : "de ouf"}}, "fallafel" : "nerguez","grec":"cacao"}
    if file != []:
        treedata = sg.TreeData() 
        dictToTree(treedata, protocols.decoder(parser.parser(file)), '')


    layout = [[sg.Text('your files')],
              [sg.Input(key='-FILE-', visible=False, enable_events=True), sg.FileBrowse()],
               [sg.Tree(data=treedata,
                        headings=[],
                        auto_size_columns=True,
                        num_rows=20,
                        col0_width=40,
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
            dictToTree(treedata, protocols.decoder(parser.parser(open(values[event]))), '')
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        print(event, values)
    window.close()

def noGUI(file=[]):
    if file == []:
        print("problem : no file", file)
    else :
        print(protocols.decoder(parser.parser(file)))

def dictToTree(Treedata, dictChamps, parentname):
    print(dictChamps)
    for i in dictChamps.keys():
        if type(dictChamps[i]) == dict:
            print(i)
            Treedata.Insert(parentname, parentname +  str(i), str(i) ,values = [], icon = None)
            dictToTree(Treedata, dictChamps[i], parentname+ str(i) )
        else :
            print(i)
            Treedata.Insert(parentname, parentname + str(i), str(i) + ' : ' + dictChamps[i], values = [], icon = None)

