# import the library


import json
import requests
import multiprocessing
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# variable


color = '#7ab8f5'
tag = ['灯', '风扇', '门']
value_tag = ['开', '关']

# process


def update_label():
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'get', 'tag': '未到教室的名单'}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    label_name.config(text=s['未到教室的名单'])
    root.after(1000, update_label)


def click_light_open():
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': tag[0], 'value': value_tag[0]}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    global img
    global label
    img = Image.open('Image/light_open.png')
    img = ImageTk.PhotoImage(img)
    label.configure(image=img)
    label.image = img
    print(tag[0] + ' 的数据更新成功，更新为 ' + value_tag[0], flush=True)


def click_light_close():
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': tag[0], 'value': value_tag[1]}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    global img
    global label
    img = Image.open('Image/light_close.png')
    img = ImageTk.PhotoImage(img)
    label.configure(image=img)
    label.image = img
    print(tag[0] + ' 的数据更新成功，更新为 ' + value_tag[1], flush=True)


def click_fan_open():
    global img_fan
    global label_fan
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': tag[1], 'value': value_tag[0]}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    img_fan = Image.open('Image/fan_open.png')
    img_fan = ImageTk.PhotoImage(img_fan)
    label_fan.configure(image=img_fan)
    label_fan.image = img_fan
    print(tag[1] + ' 的数据更新成功，更新为 ' + value_tag[0], flush=True)


def click_fan_close():
    global img_fan
    global label_fan
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': tag[1], 'value': value_tag[1]}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    img_fan = Image.open('Image/fan_close.png')
    img_fan = ImageTk.PhotoImage(img_fan)
    label_fan.configure(image=img_fan)
    label_fan.image = img_fan
    print(tag[1] + ' 的数据更新成功，更新为 ' + value_tag[1], flush=True)


def click_door_open():
    global img_door
    global label_door
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': tag[2], 'value': value_tag[0]}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    img_door = Image.open('Image/door_open.png')
    img_door = ImageTk.PhotoImage(img_door)
    label_door.configure(image=img_door)
    label_door.image = img_door
    print(tag[2] + ' 的数据更新成功，更新为 ' + value_tag[0], flush=True)


def click_door_close():
    global img_door
    global label_door
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': tag[2], 'value': value_tag[1]}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    img_door = Image.open('Image/door_close.png')
    img_door = ImageTk.PhotoImage(img_door)
    label_door.configure(image=img_door)
    label_door.image = img_door
    print(tag[2] + ' 的数据更新成功，更新为 ' + value_tag[1], flush=True)


def on_enter(event):
    text_enter = text_var.get()
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': '通知', 'value': text_enter}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)


def main():

    global root

    root = Tk()
    root.geometry('700x550+80+80')
    root.resizable(0, 0)
    root.title('智学天地 智能管理系统')
    # root.iconphoto(False, PhotoImage(file='Image/icon.png'))
    root.configure(bg=color)

    style = ttk.Style()
    style.theme_use('vista')
    style.configure('TButton', background=color)    
    global text_var
    text_var = StringVar()  
    label_xx = Label(root,text = "消息通知",font=("华文中宋",15),bg = color)
    label_xx.place(x = 220,y = 400)
    global entry

    entry = ttk.Entry(root, textvariable=text_var,font=('华文中宋',15))
    entry.place(x=220,y = 450)

    global label_xxx

    label_xxx = Label(root, text="未到教室的名单", bg=color, font=('华文中宋', 15))
    label_xxx.place(x=270, y=300)
    global label_name
    label_name = Label(root, text="请求数据中……", bg=color, font=('华文中宋', 15))
    label_name.place(x=270, y=330)

    lable_title = Label(root, text='智学天地 智能管理系统',
                        font=('华文中宋', 20), bg=color)
    lable_title.place(x=220, y=20)

    button_light_open = ttk.Button(root, text='打开 灯', command=click_light_open)
    button_light_open.place(x=100, y=200)
    button_light_close = ttk.Button(
        root, text='关闭 灯', command=click_light_close)
    button_light_close.place(x=100, y=250)

    button_fan_open = ttk.Button(root, text="打开风扇", command=click_fan_open)
    button_fan_open.place(x=295, y=200)

    button_fan_close = ttk.Button(root, text='关闭风扇', command=click_fan_close)
    button_fan_close.place(x=295, y=250)

    button_door_open = ttk.Button(root, text="打开 门", command=click_door_open)
    button_door_open.place(x=490, y=200)

    button_door_close = ttk.Button(root, text='关闭 门', command=click_door_close)
    button_door_close.place(x=490, y=250)

    img = Image.open('Image/light_close.png')
    img = ImageTk.PhotoImage(img)

    img_fan = Image.open('Image/fan_close.png')
    img_fan = ImageTk.PhotoImage(img_fan)

    img_door = Image.open('Image/door_close.png')
    img_door = ImageTk.PhotoImage(img_door)

    global label

    label = Label(root, image=img)
    label.place(x=105, y=90)

    global label_fan

    label_fan = Label(root, image=img_fan)
    label_fan.place(x=300, y=90)

    global label_door

    label_door = Label(root, image=img_door)
    label_door.place(x=495, y=90)


    entry.bind("<Return>", on_enter)

    update_label()

    root.mainloop()


def get_data():
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': '门', 'value': '关'}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    print('门 的数据更新成功，更新为 关', flush=True)
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': '灯', 'value': '关'}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    print('灯 的数据更新成功，更新为 关', flush=True)
    postdata = {'user': 'zm111123', 'secret': 'a46a5f05',
                'action': 'update', 'tag': '风扇', 'value': '关'}
    r = requests.post('http://tinywebdb.appinventor.space/api', data=postdata)
    s = json.loads(r.text)
    print('风扇 的数据更新成功，更新为 关', flush=True)


if __name__ == '__main__':
    get_data_process = multiprocessing.Process(target=get_data)
    main_process = multiprocessing.Process(target=main)

    get_data_process.start()
    main_process.start()
