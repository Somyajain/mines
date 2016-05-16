"""A hackable minesweeper game"""
#MineSweeper

from Tkinter import *
import tkMessageBox
from random import *
import math
frame = Tk()


Label(frame, text="Enter the grid size n:").grid(row=0,column=0)
e1=Entry(frame)
e1.grid(row=1,column=0)


def mine_number(mine_pos,m,size_of_grid):
    mine_number={}

    for p in m:
        neighbours=[]
        if p not in mine_pos:

            i=p[0]
            j=p[1]
            l1=[i]
            l2=[j]
            if i+1<=size_of_grid:
                l1.append(i+1)
            if i-1>0 :
                l1.append(i-1)
            if j+1<=size_of_grid :
                l2.append(j+1)
            if j-1>0 :
                l2.append(j-1)


            for ele in l1:


                for elem in l2:
                    if (l1.index(ele)==0 and l2.index(elem)== 0):
                        pass
                    else:
                        neighbours.append([ele,elem])


            mines=len(list(set(tuple(y) for y in neighbours)& set(tuple(k) for k in mine_pos)))

            mine_number[p]=mines
    return mine_number

def mine_positions(n,m):
    no_of_mines=math.floor((n**2)/4.0)
    print 'no_of_mines',no_of_mines
    pos=[]
    for i in range(0,int(no_of_mines)):
        while True:
            k=randint(0,len(m)-1)


            z=m[k]
            if z not in pos:
                pos.append(z)
                break
    return pos
'''def mine(event):

    x[b[0],b[1]]["text"] = "X"
    x[b[0],b[1]]['state']='disabled'
'''





def fetch_grid_size():
    grid_size = e1.get()
    frame.destroy()
    root=Tk()
    size_of_grid=int(grid_size)
    x={}
    for i in range (1,size_of_grid+1):
        for j in range(1,size_of_grid+1):
            x[i,j]=Button(root,text=str(i)+','+str(j),name=str(i)+','+str(j),height=1,width=1)
            x[i,j].grid(row=i,column=j)

        (x.keys()).sort()

    mine_pos=mine_positions(size_of_grid,x.keys())
    print mine_pos
    def mine(event):

        event.widget["text"] = "X"
        event.widget["bg"] = "red"
        event.widget['state']='disabled'
        event.widget.config(relief=SUNKEN)
        for b in mine_pos:
            f=b[0]
            g=b[1]
            x[f,g]['text']='X'
            x[f,g]['state']='disabled'
        for all in mines_at_pos:
            print 'working'
            num=mines_at_pos[all]
            print 'xall', x[all]
            print 'text',x[all]['text']# why does the last one only show mine, how to change text of the button
            x[all]['state']='disabled'


        pop_up=Tk()
        label=Label(pop_up,text='You loser!')
        label.pack()


    mines_at_pos=mine_number(mine_pos,x.keys(),size_of_grid)
    print 'mines_at_pos', mines_at_pos




    for b in mine_pos:
        f=b[0]
        g=b[1]

        x[f,g]=Button(root,height=1,width=1)
        x[f,g].grid(row=b[0],column=b[1])
        x[f,g].bind("<Button-1>", mine)
    def number(event):
        print 'event.widget',event.widget

        c=(f1,g1)
        print 'c',c
        print 'x,f1,g1',x[f1,g1]
        x[f1,g1]['text']=mines_at_pos[c]
    for b1 in mines_at_pos:
        print 'b1',b1
        f1=b1[0]
        g1=b1[1]


        x[f1,g1]=Button(root,height=1,width=1)
        x[f1,g1].grid(row=b[0],column=b[1])
        print 'this',x[f1,g1]
        x[f1,g1].bind("<Button-1>",number)










Button(frame,text='ok',command=fetch_grid_size).grid(row=2,column=0,sticky=W,pady=4)









#button1['state']='disabled' -------for disabling a button


#main.minsize(height=600,width=400)


frame.mainloop()
