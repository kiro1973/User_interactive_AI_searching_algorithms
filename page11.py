#import main_file
from tkinter import Entry, StringVar, messagebox
from node import*
import math
import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 35)
RADUIS=20
class Page11 (tk.Frame):
     
    def __init__(self, parent, controller,list,theCanvas,edgeList,nodelist,goalslist,edgeflag,start_node,searchType):
        self.searchType=searchType
        self.start_node=start_node
        self.controller=controller
        self.edgeflag=edgeflag
        self.goalslist=goalslist 
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Design your edges in the gray area", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        print("self.list fe page1:")
        self.list=list
        self.edgeList=edgeList
        self.nodelist=nodelist
        print(self.list)
        # button to show frame 2 with text
        # layout2
        self.weightLabel=ttk.Label(self, text ="weight of edge")
        self.WeightName= StringVar()
        self.weightEntry=Entry(self,textvariable=self.WeightName)
        self.weightEntry.place(x=123,y=300)
        self.weightLabel.place(x=10,y=300)
        from StartPage import StartPage
        self.mycanvas=theCanvas
        self.mycanvas.place(x=600,y=100,height=650,width=700)
       
        button1 = ttk.Button(self, text ="add Nodes",
        
                            command = lambda : controller.show_frame(StartPage))
        from graphResult import graphResut
        button2 = ttk.Button(self, text ="Search",
                            command = self.btn1_func)
        self.click_number=0
        button_draw_line = ttk.Button(self, text ="draw_edge",command=self.linking)
        button_draw_line.place(x=10, y=200)
       
        button1.place(x=400,y=470)
        button2.place(x=400,y=600)
  
    def btn1_func(self):
        if len(self.start_node[0].children):
            from graphResult import graphResut
            self.controller.show_frame(graphResut)
            #self.button2.destroy()
        else :messagebox.showwarning("wrong choice","the start node must have at least one child")        
    def print(self):
        print(self.list)
    def linking (self):
        self.mycanvas.bind('<Button-1>',self.draw_line)
        print('line 45')
        
        print('line 47')
        #mycanvas.bind('<Button-1>',draw_line)
    def draw_line(self,event):
        #global click_number
        global x1,y1,node1
        # thecanvas.bind('<Button-1>',self.draw_line)
        if (self.click_number==0):
            distanceflag=0
            for node in self.nodelist:
                distance = math.sqrt( (node.Xposition-(event.x))**2+((node.Yposition-(event.y))**2)) 
                if distance<=(40*math.sqrt(2)):
                    node1=node
                    distanceflag=1
                    break
            if distanceflag==1:
                x1=event.x
                y1=event.y
                self.click_number=1
            else :
                messagebox.showwarning("wrong choice","an edge must start from inside a circle") 

            

        else :
            searchflag=0
            distanceflag_2=0
            for node in self.nodelist:
                distance = math.sqrt( (node.Xposition-(event.x))**2+((node.Yposition-(event.y))**2)) 
                if distance<=(40*math.sqrt(2)):
                    node2=node
                    distanceflag_2=1
            if distanceflag_2==1:
                if node1.nodeName==node2.nodeName:
                    messagebox.showwarning("wrong choice","you cannot make an edge from a node to itself")  
                    
                    searchflag=1
                    self.click_number=0
                    self.mycanvas.unbind('<Button-1>',self.draw_line)
                for couple in self.edgeList:
                    if ((couple.node1.nodeName==node1.nodeName) and (couple.node2.nodeName==node2.nodeName)):
                        messagebox.showwarning("wrong choice","edge already exists")
                        
                        searchflag=1
                        self.click_number=0
                        self.mycanvas.unbind('<Button-1>',self.draw_line)
                    
                if searchflag==0:
                    
                    nodeCouple=nodecouples(node1,node2)
                    self.edgeList.append(nodeCouple)
                    if self.weightEntry.get()=="":
                        weight=0
                    else:
                        weight=int(self.weightEntry.get())
                    node1.children.append((node2,weight))
                    x2=event.x
                    y2=event.y
                    """
                    Node_in_x =  node2.Xposition
                    Node_in_y =node2.Yposition
                    Node_out_x  = node1.Xposition
                    Node_out_y=node1.Yposition
                    dy = abs(Node_in_y - Node_out_y)
                    dx = abs(Node_in_x - Node_out_x)
                    if(dx > dy):
                        if(Node_in_y < Node_out_y):
                            self.mycanvas.create_line(Node_out_x,Node_out_y+RADUIS,Node_in_x,Node_in_y+RADUIS,fill='black',width=2,smooth='true',arrow='last')
                        else:
                            self.mycanvas.create_line(Node_out_x,Node_out_y-RADUIS,Node_in_x,Node_in_y-RADUIS,fill='black',width=2,smooth='true',arrow='last')
                    else:
                        if(Node_in_x < Node_out_x):
                            self.mycanvas.create_line(Node_out_x+RADUIS,Node_out_y,Node_in_x+RADUIS,Node_in_y,fill='black',width=2,smooth='true',arrow='last')
                        else:
                            self.mycanvas.create_line(Node_out_x-RADUIS,Node_out_y,Node_in_x-RADUIS,Node_in_y,fill='black',width=2,smooth='true',arrow='last')
                   """
                    self.mycanvas.create_line(x1,y1,x2,y2,fill='black',width=2,arrow='last',arrowshape=(10,20,10),smooth='true')
                    #self.mycanvas.create_oval(x1-50,y1-50,x1,y1,width=1,tags="oval")
                    print ("children of '"+ node1.nodeName+"'are:")
                    print(node1.children)
                    #for n in node1.children:
                        #print (n.nodeName)
                    self.click_number=0
                    self.mycanvas.unbind('<Button-1>',self.draw_line)
            else :
                messagebox.showwarning("wrong choice","an edge must start from inside a node")
                self.click_number=0 
                self.mycanvas.unbind('<Button-1>',self.draw_line)
