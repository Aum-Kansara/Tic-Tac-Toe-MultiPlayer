from tkinter import PhotoImage,Label,Button,Tk,messagebox
import socket
from threading import Thread


your_turn=True
game_over=False
count=0
window_closed=False
c1=socket.socket()
c1.connect(('localhost',9999))
name="Aum"
c1.send(bytes(name,'utf-8'))
print(c1.recv(1024).decode())
clicked1=False
clicked2=False
clicked3=False
clicked4=False
clicked5=False
clicked6=False
clicked7=False
clicked8=False
clicked9=False
def on_closing():
    global game_over
    global window_closed
    window_closed=True
    game_over=True
    root.destroy()
def get_restart_msg():
    while window_closed==False and game_over==True:
        restart_msg = c1.recv(1024).decode()
        if restart_msg=="restart":
            restart()
def restart():
    pass
    # global game_over,your_turn,clicked1,clicked2,clicked3,clicked4,clicked5,clicked6,clicked7,clicked8,clicked9,count
    # c1.send(bytes("restart",'utf-8'))
    # count=0
    # game_over=False
    # your_turn=True
    # Thread(target=get_data).start()
    # for i in grids:
    #     i.config(image=defualt)
    #     clicked1 = False
    #     clicked2 = False
    #     clicked3 = False
    #     clicked4 = False
    #     clicked5 = False
    #     clicked6 = False
    #     clicked7 = False
    #     clicked8 = False
    #     clicked9 = False
        
def set_image1():
    global clicked1,count
    global your_turn
    if clicked1 != True and your_turn==True and game_over==False:
        grid_1.config(image=your_image)
        c1.send(bytes("grid-1", 'utf-8'))
        clicked1 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()

def set_image2():
    global clicked2,count
    global your_turn
    if clicked2 != True and your_turn==True and game_over==False:
        grid_2.config(image=your_image)
        c1.send(bytes("grid-2", 'utf-8'))
        clicked2 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()

def set_image3():
    global clicked3,count
    global your_turn
    if clicked3 != True and your_turn==True and game_over==False:
        grid_3.config(image=your_image)
        c1.send(bytes("grid-3", 'utf-8'))
        clicked3 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()
def set_image4():
    global clicked4,count
    global your_turn
    if clicked4 != True and your_turn==True and game_over==False:
        grid_4.config(image=your_image)
        c1.send(bytes("grid-4", 'utf-8'))
        clicked4 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()

def set_image5():
    global clicked5,count
    global your_turn
    if clicked5 != True and your_turn==True and game_over==False:
        grid_5.config(image=your_image)
        c1.send(bytes("grid-5", 'utf-8'))
        clicked5 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()

def set_image6():
    global clicked6,count
    global your_turn
    if clicked6 != True and your_turn==True and game_over==False:
        grid_6.config(image=your_image)
        c1.send(bytes("grid-6", 'utf-8'))
        clicked6 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()
def set_image7():
    global clicked7,count
    global your_turn
    if clicked7 != True and your_turn==True and game_over==False:
        grid_7.config(image=your_image)
        c1.send(bytes("grid-7", 'utf-8'))
        clicked7 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()
def set_image8():
    global clicked8,count
    global your_turn
    if clicked8 != True and your_turn==True and game_over==False:
        grid_8.config(image=your_image)
        c1.send(bytes("grid-8", 'utf-8'))
        clicked8 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()
def set_image9():
    global clicked9,count
    global your_turn
    if clicked9 != True and your_turn==True and game_over==False:
        grid_9.config(image=your_image)
        c1.send(bytes("grid-9", 'utf-8'))
        clicked9 = True
        your_turn=False
        count+=1
        Thread(target=check_win).start()
root=Tk()
root.geometry('680x685')
root.title("Client")

bg=PhotoImage(file='chex1.png')
bg_lable=Label(root,image=bg)
bg_lable.place(x=0,y=0)

cross=PhotoImage(file='image_thumbnai1.png')
round=PhotoImage(file='image1_thumbnai1.png')
defualt=PhotoImage(file='default.png')
restart_img=PhotoImage(file='restart1.png')
a=c1.recv(1024).decode()
if a=="round":
    your_image=cross
    opponent_image=round
elif a=="cross":
    your_image=round
    opponent_image=cross

def show_result(a):
    if a=='win':
        messagebox.showinfo(a,'Congratulation!.. You Won The Match.')
    elif a=='lose':
        messagebox.showinfo(a,'You Lose The Match.')


def check_win():
    global game_over
    if count>=5:
        if grid_1.cget('image')=='pyimage2' and grid_2.cget('image')=='pyimage2' and grid_3.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
                

            elif your_image==round:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_1.cget('image')=='pyimage2' and grid_4.cget('image')=='pyimage2' and grid_7.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==round:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_1.cget('image')=='pyimage2' and grid_5.cget('image')=='pyimage2' and grid_9.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==round:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_2.cget('image')=='pyimage2' and grid_5.cget('image')=='pyimage2' and grid_8.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==round:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_3.cget('image')=='pyimage2' and grid_6.cget('image')=='pyimage2' and grid_9.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==round:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_3.cget('image')=='pyimage2' and grid_5.cget('image')=='pyimage2' and grid_7.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==round:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_4.cget('image')=='pyimage2' and grid_5.cget('image')=='pyimage2' and grid_6.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==round:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_7.cget('image')=='pyimage2' and grid_8.cget('image')=='pyimage2' and grid_9.cget('image')=='pyimage2':
            if your_image==cross:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==round:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        
        elif grid_1.cget('image')=='pyimage3' and grid_2.cget('image')=='pyimage3' and grid_3.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==cross:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_1.cget('image')=='pyimage3' and grid_5.cget('image')=='pyimage3' and grid_7.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==cross:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_1.cget('image')=='pyimage3' and grid_5.cget('image')=='pyimage3' and grid_9.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==cross:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_2.cget('image')=='pyimage3' and grid_4.cget('image')=='pyimage3' and grid_8.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==cross:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_3.cget('image')=='pyimage3' and grid_6.cget('image')=='pyimage3' and grid_9.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==cross:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_3.cget('image')=='pyimage3' and grid_5.cget('image')=='pyimage3' and grid_7.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==cross:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_4.cget('image')=='pyimage3' and grid_5.cget('image')=='pyimage3' and grid_6.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==cross:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
        elif grid_7.cget('image')=='pyimage3' and grid_8.cget('image')=='pyimage3' and grid_9.cget('image')=='pyimage3':
            if your_image==round:
                show_result('win')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
            elif your_image==cross:
                show_result('lose')
                c1.send(bytes("game_over",'utf-8'))
                game_over=True
def get_data():
    global game_over
    while game_over==False:
        global c1,grid_1,grid_2,grid_3,grid_4,grid_5,grid_6,grid_7,grid_8,grid_9,count,opponent_image,your_turn,clicked1,clicked2,clicked3,clicked4,clicked5,clicked6,clicked7,clicked8,clicked9
        msg=c1.recv(1024).decode()
        if msg=="game_over":
            game_over=True
            # Thread(target=get_restart_msg()).start()
            break
        elif msg=="restart":
            restart()
        elif msg!='':
            if msg=="grid-1":
                grid_1.config(image=opponent_image)
                clicked1=True
                your_turn=True
                count+=1
                Thread(target=check_win).start()
            elif msg=="grid-2":
                grid_2.config(image=opponent_image)
                clicked2=True
                your_turn=True
                count+=1
                Thread(target=check_win).start()
            elif msg=="grid-3":
                grid_3.config(image=opponent_image)
                clicked3=True
                your_turn=True
                count+=1
                Thread(target=check_win).start()
            elif msg=="grid-4":
                grid_4.config(image=opponent_image)
                clicked4=True
                your_turn=True
                count+=1
                Thread(target=check_win).start()
            elif msg=="grid-5":
                grid_5.config(image=opponent_image)
                clicked5=True 
                your_turn=True
                count+=1
                Thread(target=check_win).start()
            elif msg=="grid-6":
                grid_6.config(image=opponent_image)
                clicked6=True
                your_turn=True
                count+=1
                Thread(target=check_win).start()
            elif msg=="grid-7":
                grid_7.config(image=opponent_image)
                clicked7=True
                your_turn=True
                count+=1
                Thread(target=check_win).start()
            elif msg=="grid-8":
                grid_8.config(image=opponent_image)
                clicked8=True
                your_turn=True
                count+=1
                Thread(target=check_win).start()
            elif msg=="grid-9":
                grid_9.config(image=opponent_image)
                clicked9=True
                your_turn=True
                count+=1
                Thread(target=check_win).start()
t1=Thread(target=get_data)
t1.start()

grid_1=Button(root,image=defualt,command=set_image1,bd=0)
grid_1.place(x=20,y=23)
grid_2=Button(root,image=defualt,command=set_image2,bd=0)
grid_2.place(x=255,y=23)
grid_3=Button(root,image=defualt,command=set_image3,bd=0)
grid_3.place(x=490,y=23)
grid_4=Button(root,image=defualt,command=set_image4,bd=0)
grid_4.place(x=20,y=255)
grid_5=Button(root,image=defualt,command=set_image5,bd=0)
grid_5.place(x=260,y=255)
grid_6=Button(root,image=defualt,command=set_image6,bd=0)
grid_6.place(x=490,y=255)
grid_7=Button(root,image=defualt,command=set_image7,bd=0)
grid_7.place(x=20,y=480)
grid_8=Button(root,image=defualt,command=set_image8,bd=0)
grid_8.place(x=260,y=480)
grid_9=Button(root,image=defualt,command=set_image9,bd=0)
grid_9.place(x=490,y=480)
# restart_btn=Button(root,image=restart_img,bd=0,command=restart)
# restart_btn.place(x=705,y=23)
grids=[grid_1,grid_2,grid_3,grid_4,grid_5,grid_6,grid_7,grid_8,grid_9]
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
