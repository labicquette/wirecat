import PySimpleGUI as sg
import sys

def pythonGUI(guiParameters=[]):
    sg.theme('DarkAmber')    # Keep things interesting for your users





    dictionnaire={"chocolat":{"feves": "saucisse","kebab":{"75 paname" : "de ouf"}}, "fallafel" : "nerguez","grec":"cacao"}
    treedata = sg.TreeData() 
    section(treedata, dictionnaire, '')


    layout = [[sg.Text('File and folder browser Test')],
              [sg.Tree(data=treedata,
                        headings=[],
                        auto_size_columns=True,
                        num_rows=20,
                        col0_width=40,
                        key='-TREE-',
                    show_expanded=False,
                    enable_events=True),
                ],
            [sg.Button('Ok'), sg.Button('Cancel')]]

    window = sg.Window('Tree Element Test', layout)

    while True:     # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        print(event, values)
    window.close()


def section(Treedata, dictChamps, parentname):
    for i in dictChamps.keys():
        if type(dictChamps[i]) == dict:
            Treedata.Insert(parentname, parentname +  i, i ,values = [], icon = None)
            section(Treedata, dictChamps[i], parentname+i)
        else :
            Treedata.Insert(parentname, parentname + i, i + ' : ' + dictChamps[i], values = [], icon = None)


def makeTree(dictChamps={}):
    Tree = sg.TreeData()
    for key in dictChamps.keys():
        if type(dictChamps[key] == dict):
            Tree.Insert('', key, key,values=[], icon = None)
            section(Tree, dictChamps, key)
        else :
            Tree.Insert('', key, key, values=[], icon = None)
    #section(Tree, dictChamps)

    return Tree