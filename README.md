# **Wirecat** 

### *Wirecat is the result of the merging between **Wireshark** and **cat** from unix*
## **How to install ?**
### Requirements :

```
pip install tkinter 
```
#### And python >= 3
### Just clone the repo... And done, everything works out of the box.
#### Compatible with Linux, should be compatible with MACOS. Compatibility with Windows unknown.

### **How to execute ?** 

#### With GUI :
```
python wirecat.py 
```

#### Without GUI :
```
python wirecat.py -ng yourfile.txt
```

#### With file output :
```
python wirecat.py -o yourfile.txt
```


### **Structure of code :**

#### The code is structured with 4 important classes : parser, graphics, protocols, wirecat
#### Parser : Class that parses the original txt file and transforms it in an dictionnary of frames with their array of bytes.
#### Graphics : Class that controls the GUI interface and within the app between the parsing and the actual analyse of the frame.
#### Protocols : Group of classes that all have an analyser method that returns a dictionnary of informations contained in the protocol header.
#### Wirecat : Interface between the terminal and the python code with gestion of multiple args.