import tkinter as tk

root = tk.Tk()
root.title('ストップウォッチ')

label = tk.Label(root, text='0:00')

label.grid(row=0, columnspan=3)

flg = True
second = 0
minutes = 0

def start():

  global flg

  if flg:
    global second
    global minutes
    if second == 60:
      minutes += 1
      second = 0

    if second < 10:
      label['text'] = str(minutes) + ':0' + str(second)
    else:
      label['text'] = str(minutes) + ':' + str(second)

    second += 1

    root.after(1000, start)

  else:
    flg = True

def stop():

  global flg
  global second

  second -= 1
  flg = False

def reset():
  flg = False

  global second
  global minutes

  second = 0
  minutes = 0

  label['text'] = str(minutes) + ':0' + str(second)

start_btn = tk.Button(root, text='スタート', command=start)
stop_btn = tk.Button(root, text='ストップ', command=stop)
reset_btn= tk.Button(root, text='リセット', command=reset)

start_btn.grid(row=1, column=0)
stop_btn.grid(row=1, column=1)
reset_btn.grid(row=1, column=2)

root.mainloop()