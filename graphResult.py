import tkinter as tk
from tkinter import  ttk
from tkinter import*
from PIL import Image,ImageTk
from node import *
from StartPage import StartPage
class graphResut(tk.Frame):
    def __init__(self,parent,controller,theCanvas,nodelist,start_node,searchType):
        tk.Frame.__init__(self, parent)
        self.searchType=searchType
        self.controller=controller
        self.mycanvas=theCanvas
        self.mycanvas.place(x=600,y=100,height=650,width=700)
        self.nodelist=nodelist
        self.start_node=start_node # list that contain the start node
        #result=self.aySearch(nodelist)
        self.a=algos()
        self.visited=[]
        self.solutionPath=[]
        self.table=[]
        self.newflag=1
        self.last_in_table=False
        img= (Image.open("play.png"))
        #Resize the Image using resize method
        resized_image= img.resize((30,30), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)

        img_1= (Image.open("yellow.png"))
        #Resize the Image using resize method
        resized_image_1= img_1.resize((30,30), Image.ANTIALIAS)
        new_image_1= ImageTk.PhotoImage(resized_image_1)

        img_2= (Image.open("light blue.png"))
        #Resize the Image using resize method
        resized_image_2= img_2.resize((30,30), Image.ANTIALIAS)
        new_image_2= ImageTk.PhotoImage(resized_image_2)
        #photo = PhotoImage(file = r"play.png")
        self.finish_visit=0
        self.goals_list=[]
        button1 = ttk.Button(self, text ="add Nodes",
                            command = lambda : controller.show_frame(StartPage))
        self.label_yellow=ttk.Label(self, text ="visited node",image=new_image_1,compound='left')
        self.label_lightBlue=ttk.Label(self, text ="solution path node",image=new_image_2,compound='left')
        self.label_yellow.image=new_image_1
        self.label_lightBlue.image=new_image_2
        self.label_yellow.place(x=10,y=600)
        self.label_lightBlue.place(x=10,y=630)

        button1.place(x=400,y=500)
        btn_start_searching = ttk.Button(self, text ="start seach",command=self.aySearch)
        btn_start_searching.place(x=10,y=50)
        btn_play = ttk.Button(self,image=new_image,command=self.coloring)
        btn_play.image=new_image
        btn_play.place(x=400,y=300)
        self.label=ttk.Label(self, text ="")
        self.label.place(x=300,y=100)
        #for v in visited:
        #    self.mycanvas.itemconfig(v.circle, fill="yellow") 
        
    def aySearch(self):
        for n in self.nodelist:
            if n.goalflag==True:
                self.goals_list.append(n)
        search_type=self.searchType[0]
        start_node=self.start_node[0]
        print("name of startnode "+self.start_node[0].nodeName)
        print("TYPE OF startnode"+str(type(start_node)))
        print("self.searchType="+self.searchType[0])
        if search_type=="Breadth First search":
            print("breadth first*******")
            result=self.a.BFS(start_node)
            self.visited=result[1]
            self.solutionPath=result[0]
        elif search_type=="uniform cost search":
            result=self.a.uniform_cost_search(self.goals_list,start_node)
            self.visited=result[0]
            self.solutionPath=result[1]
        elif search_type=="A* search":
            print("A* search*******")
            result=self.a.a_star_algorithm(start_node)
            self.visited=result[1]
            self.solutionPath=result[0]
        elif search_type=="Greedy search":
            print("Greedy search*******")
            result=self.a.Greedy(start_node)
            self.visited=result[1]
            self.solutionPath=result[0]
        elif search_type=="Depth first search":
            print("DFS*******")
            result=self.a.DFS(start_node)
            self.visited=result[1]
            self.solutionPath=result[0]
        elif search_type=="iterative deepening search":
            print("Iterative *************")
            self.label.config(text="")
            self.iterator(start_node,self.nodelist)

        """
        visited_names=['a','b','c','d']
        solutionPath_names=['a','b','d']
        visited=[]
        solutionPath=[]
        for name in visited_names:
            for node in self.nodelist:
                if node.nodeName ==name:
                    visited.append(node)
        for name in solutionPath_names:
            for node in self.nodelist:
                if node.nodeName ==name:
                    solutionPath.append(node)      
        #return (visited,solutionPath)
        self.visited=visited
        self.solutionPath=solutionPath
        """
    def coloring(self):
        if self.searchType[0]=="iterative deepening search":
            print("line 117")
            self.coloring_2()
        else:
            if len(self.visited)!=0:
                node=self.visited.pop(0)
                self.mycanvas.itemconfig(node.circle, fill="yellow")
            else :
                node=self.solutionPath.pop(0)
                self.mycanvas.itemconfig(node.circle, fill="light blue")
    def iterator(self,source,nodelist):
        #label=ttk.Label(self, text ="")
        #label.place(x=300,y=100)
        arriveflag=0
        visited=[]
        table=[]
        L=0
        result=None
        while (len(visited)<len(nodelist)):
            result=self.a.iterative_deepening(source,L)
            visited=result[1]
            arriveflag=result[0]
            my_text=""
            visitNames=[]
            if arriveflag==False:
               
                for v in result[1]:
                    
                    visitNames.append(v.nodeName)
                my_text=my_text+"\nvisited of iteration "+str(L)+" is : "+str(visitNames)
                self.table.append([result[1],my_text])
                #label.config(text =my_text)
                print("visited of iteration"+str(L)+"is :"+str(visitNames))
                L=L+1
                for node in nodelist:
                    node.visitflag=False
                    node.parent=None
                    node.mark=False
                
            else:
                
                for v in result[1]:
                    visitNames.append(v.nodeName)
                my_text=my_text+"\nvisited of iteration "+str(L)+" is : "+str(visitNames)
                self.table.append([result[1],my_text,result[2]])
                #label.config(text =my_text)
                print("visited of iteration "+str(L)+" is : "+str(visitNames))
                break
        #return (result[1],result[2])
    def coloring_2(self):
        print(len(self.table))
        row=None
        if self.newflag==1:
            print("line 169")
            row=self.table.pop(0)
            self.visited=row[0]
            self.label.config(text=row[1])
            print("********************* row[1]: "+row[1])
            self.newflag=0
            if len(self.table)==0:
                self.last_in_table=True
                self.solutionPath=row[2]
                self.newflag=0
            
            
            
        if len(self.visited)!=0:
            node=self.visited.pop(0)
            self.mycanvas.itemconfig(node.circle, fill="yellow")
            if len(self.visited)==0:
                if self.last_in_table==False:
                    self.newflag=1
        else:
            if(self.last_in_table==True):
                node=self.solutionPath.pop(0)
                self.mycanvas.itemconfig(node.circle, fill="light blue")
                if len(self.solutionPath)==0:
                    self.last_in_table=False
                    self.newflag=1
               


        