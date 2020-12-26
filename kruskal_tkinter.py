import turtle 
from tkinter import *
import tkinter as tk

switch = {
            1:[100,0],
            2:[200,0],
            3:[300,0],
            4:[77,90],
            5:[123,35],
            6:[212,20],
            7:[304,17],
            8:[154,90],
            9:[188,60],

            12:[100,0],
            13:[200,0],
            14:[123,140],
            15:[77,90],
            16:[123,35],
            17:[212,20],
            18:[188,120],
            19:[154,90],

            23:[100,0],
            24:[212,157],
            25:[123,140],
            26:[100,90],
            27:[135,45],
            28:[250,140],
            29:[188,120],

            34:[304,166],
            35:[212,156],
            36:[123,140],
            37:[77,90],
            38:[338,150],
            39:[250,140],

            45:[100,270],
            46:[200,270],
            47:[300,270],
            48:[77,90],
            49:[135,45],
            
            56:[100,310],
            57:[200,0],
            58:[135,136],
            59:[77,90],

            67:[100,290],
            68:[212,157],
            69:[123,140],

            78:[304,163],
            79:[212,164],

            89:[100,270]
         }
def provided_graph():
    a= -600
    B = 220
    counter = 1
    lp = turtle.Turtle()
    lp.penup()
    lp.goto(-610,270)
    lp.write('Provided Graph',font=('Arial', 18, 'normal'))
    for i in range(n):
        if counter <= n:
            o = turtle.Turtle()
            o.penup()
            o.goto(a,B)
            o.pendown()
            o.shape(vertex_name[i])
            a = a + 100
            if counter % 4 == 0:
                B = B - 73
                a = -600 
            counter = counter + 1
    po.penup()
    po.goto(-600,212)
    for i in range(1,n+1):
        square()
        po.right(90)
        po.penup()
        if i%4 == 0 and i != 0:
            po.right(165)
            po.penup()
            po.forward(312)
            po.left(165)
            continue
        if (n+1)-i != 1:
            po.forward(100)

def mst_graph():
    a= -150
    B = 220
    counter = 1
    lp = turtle.Turtle()
    lp.penup()
    lp.goto(-160,270)
    lp.write('Generated MST',font=('Arial', 18, 'normal'))
    for i in range(n):
        if counter <= n:
            o = turtle.Turtle()
            o.penup()
            o.goto(a,B)
            o.pendown()
            o.shape(vertex_name[i])
            a = a + 100
            if counter % 4 == 0:
                B = B - 73
                a = -150 
            counter = counter + 1
    po.penup()
    po.goto(-150,212)
    for i in range(1,n+1):
        square()
        po.right(90)
        po.penup()
        if i%4 == 0 and i != 0:
            po.right(165)
            po.penup()
            po.forward(312)
            po.left(165)
            continue
        if (n+1)-i != 1:
            po.forward(100)

def close_window(event):
    input_window.destroy()
    global adj_matrix
    global cost_matrix
    cost_matrix = [[0 for j in range(n)] for i in range(n)]
    status = []
    e = len(x)
    print("e=",e)
    for i in range(e):
        for j in range(e-i-1):
            if y[j] >= y[j+1]:
                y[j], y[j+1] = y[j+1], y[j]
                x[j], x[j+1] = x[j+1], x[j]

    print('edge list=',x)
    print('cost list=',y)
    for i in range(n):
        status.append(i)

    cost = 0
    print("vertex,edge=",n,e)
    print("source   destination   cost")
    for i in range(e):
        l = x[i] // 10
        k = x[i] % 10
        cost_matrix[l][k] = y[i]
        if status[l] != status[k]:
            print(l,"    ",k,"    ",y[i])
            temp = status[k]
            adj_matrix[l][k] = 999
            cost = cost + y[i]
            for z in range(n):
                if status[z] == temp:
                    status[z] = status[l]
    for i in range(n):
        for j in range(n):
            print(adj_matrix[i][j], end=" ")
        print("\n")

    print("Total cost of MST using Kruskal algo is ", cost)
    provided_graph()
    # draw()
    go_to_vertex_zero(n)
    #.....................provided...................
    for i in range(n):
        for j in range(n):
            if j > i:
                if adj_matrix[i][j] == 1 or adj_matrix[i][j] == 999:
                    v = i*10 + j
                    go_to_desired_vertex_provided_graph(v,adj_matrix[i][j])

    ct = turtle.Turtle()
    cy,cyy = 250,0
    print("complete1")


    #......................mst.......................
    mst_graph()
    go_to_vertex_zero(n)
    for i in range(n):
        for j in range(n):
            if j > i:
                if adj_matrix[i][j] == 1 or adj_matrix[i][j] == 999:
                    v = i*10 + j
                    if adj_matrix[i][j] == 999:
                        ct.penup()
                        ct.goto(300,cy)
                        ct.pencolor("blue")
                        s = f"edge included in MST: {i}-{j} , Cost: {cost_matrix[i][j]}"
                        ct.write(s,font=('Cooper', 14, 'normal'))
                        cy = cy - 25
                    else:
                        ct.penup()
                        ct.goto(300,cyy)
                        ct.pencolor("red")
                        s = f"edge not included in MST: {i}-{j} , Cost: {cost_matrix[i][j]}"
                        ct.write(s,font=('Cooper', 14, 'normal'))
                        cyy = cyy - 25
                    go_to_desired_vertex_mst_graph(v,adj_matrix[i][j])

    
    po.goto(-200,-200)
    s = f"Total cost of MST = {cost}"
    po.pencolor("blue")
    po.write(s, font=('Arial', 18, 'normal'))

def getCost():
    y.clear()
    for costs in list_of_cost_boxes:
        temp_cost = int(costs.get())
        if temp_cost != 0:
            y.append(temp_cost)
    print('current cost array=',y)

def getEdge():
    x.clear()   
    for ed in list_of_edge_boxes:
        temp_edge = int(ed.get())
        i = temp_edge // 10
        j = temp_edge % 10
        if temp_edge != 0:
            adj_matrix[i][j] = 1
            x.append(temp_edge)
    print('current edge array=',x)

def make_screen():
    # window.bgcolor("white")
    po.penup()
    po.forward(-200)
    po.left(90)
    po.forward(200)
    po.right(90)
    po.pendown()

def square():
    po.pendown()
    po.speed(2)
    po.pensize(5)
    po.fillcolor("black")
    po.pencolor("black")
    po.begin_fill()
    po.forward(10)
    po.right(90)
    po.forward(10)
    po.right(90)
    po.forward(10)
    po.right(90)
    po.forward(10)
    po.end_fill()

def go_to_vertex_zero(n):
    lst = switch[(n-1)]
    dis = lst[0]
    angl = lst[1]
    po.right(angl)
    po.penup()
    po.forward(-1*dis)
    po.left(angl)

def go_to_desired_vertex_provided_graph(v,val):
    flag = 0
    temp = 0
    temp_angle = 0
    if v//10 != 0:
        flag = 1
        intermediate_node = v//10
        node = switch[intermediate_node]
        po.penup()
        po.right(node[1])
        po.forward(node[0])
        temp = node[0]
        temp_angle = node[1]
    if val == 1 or val == 999:
        po.pendown()
        po.pencolor("black")
        po.pensize(1)

    node = switch[v]
    print(node)
    po.right(node[1])
    po.forward(node[0])
    go_to_starting_vertex(flag,node[0],node[1],temp,temp_angle)

def go_to_desired_vertex_mst_graph(v,val):
    flag = 0
    temp = 0
    temp_angle = 0
    if v//10 != 0:
        flag = 1
        intermediate_node = v//10
        node = switch[intermediate_node]
        po.penup()
        po.right(node[1])
        po.forward(node[0])
        temp = node[0]
        temp_angle = node[1]
        print("outside yellow") 

    if val == 999:   
        print("yellow") 
        po.pendown()
        po.pencolor("yellow")
        po.pensize(4)

    node = switch[v]
    print(node)
    po.right(node[1])
    po.forward(node[0])
    go_to_starting_vertex(flag,node[0],node[1],temp,temp_angle)

def go_to_starting_vertex(flag,x,y,temp,temp_angle):
    po.penup()
    po.forward(-1*x)
    po.left(y)
    if flag == 1:
        po.forward(-1*temp)
        po.left(temp_angle)

    
#.......................creating check buttons..........................
def create_edge_chk_buttons(event):
    global int_n,n
    global y
    global list_of_chk_boxes
    list_of_chk_boxes = []
    global list_of_cost_boxes
    list_of_cost_boxes = []
    global list_of_cost_btns
    list_of_cost_btns = []
    global cost_box,chk_btn
    global adj_matrix
    global list_of_vars
    list_of_vars = []
    global list_of_edge_boxes
    list_of_edge_boxes = []
    global list_of_edge_btns
    list_of_edge_btns = []

    y = []
    int_n = int(vertex_box.get())
    n = int_n
    adj_matrix = [[0 for j in range(n)] for i in range(n)]

    edge_and_cost_text = tk.Label(input_window, text="edge:                  cost:",font=("Helvetica", 14))
    edge_and_cost_text.place(x=20,y=70)
    x1,y1,temp_y1 = 15,120,100
    ovf = 1
    # create entry boxes
    for i in range(n):
        for j in range(i+1,n):
            edge_box = tk.Entry(input_window,width=4)
            edge_box.place(x=x1+15,y=y1)
            edge_box.insert(0,'0')
            edge_btn = Button(input_window, text="Enter",command=lambda:getEdge(),font=("Helvetica", 10),bg="#726F88")
            edge_btn.place(x=x1+60,y=y1)

            cost_box = tk.Entry(input_window,width=4)
            cost_box.insert(0,'0')
            cost_box.place(x=x1+150,y=y1)
            cost_btn = Button(input_window, text="Enter",command=lambda:getCost(),font=("Helvetica", 10),bg="#33F3FF")
            cost_btn.place(x=x1+200,y=y1)


            list_of_edge_boxes.append(edge_box)
            list_of_edge_btns.append(edge_btn)

            list_of_cost_boxes.append(cost_box)
            list_of_cost_btns.append(cost_btn)
            y1 = y1 + 35
            if ovf % 8 == 0:
                x1 = 300
                temp_y1 = temp_y1 + 35
                y1 = temp_y1 - 20
                edge_and_cost_text = tk.Label(input_window, text="edge:                  cost:",font=("Helvetica", 14))
                edge_and_cost_text.place(x=x1+15,y=70)
            ovf = ovf + 1
    next_btn = Button(input_window, text="Next",font=("Helvetica", 10),bg='yellow')
    next_btn.place(x=700,y=350)
    next_btn.bind('<Button-1>', close_window)

#Start of program........................................
window = turtle.Screen()   
window.setup(width=1.0, height=1.0, startx=None, starty=None)

input_window = tk.Tk()
input_window.geometry("1000x1000")
input_window.resizable(width=False, height=False)
input_window.title("Spanning tree generation")

intro_text = tk.Label(input_window, text="Hello! Generate minimum cost spanning tree with one touch! ",font=("Helvetica", 14))
intro_text.place(x=200,y=0)
vertex_text = tk.Label(input_window, text="Enter how many vertices your graph have (max. 10): ",font=("Helvetica", 12))
vertex_text.place(x=5,y=40)
vertex_box = tk.Entry(input_window,width=4)
vertex_box.place(x=400,y=40)
vertex_btn = Button(input_window, text="Enter",font=("Helvetica", 10),bg='#D82866')
vertex_btn.place(x=480,y=40)
vertex_btn.bind('<Button-1>', create_edge_chk_buttons)
# register images
window.addshape('mzero_gif.gif')
window.addshape('mone_gif.gif')
window.addshape('mtwo_gif.gif')
window.addshape('mthree_gif.gif')
window.addshape('mfour_gif.gif')
window.addshape('mfive_gif.gif')
window.addshape('msix_gif.gif')
window.addshape('mseven_gif.gif')
window.addshape('meight_gif.gif')
window.addshape('mnine_gif.gif')
vertex_name = ['mzero_gif.gif','mone_gif.gif','mtwo_gif.gif','mthree_gif.gif','mfour_gif.gif','mfive_gif.gif','msix_gif.gif','mseven_gif.gif','meight_gif.gif','mnine_gif.gif']   

po = turtle.Turtle()

x = []
y = []
e = 0

input_window.mainloop()