import tkinter as tk
import random
import math

root = tk.Tk()

root.title("ビュフォンの針")
root.geometry("900x900")

##描画領域
h = 900
w = 900

canvas = tk.Canvas(root, bg="white", height=h, width=w)

#平行線
d = 50##平行線の幅
for j in range(h//50):
   canvas.create_line(0,j*d,w,j*d)

#針が線にかかるかの判定
def CheckLine(y_1, y_2):
   if y_1 // d == y_2 // d:
       return 0 ##線にかからない
   else:
       return 1 ##線にかかる

n = int(input("針の数:")) ##針の数
l = d/2 ##針の長さ　簡単のため 2l=d
line_cross = [] ##針が線にかかるかからないの結果を格納

i=0
while i < n:
   x = random.uniform(d,w-d) ##針の片方の端点を落とす場所
   y = random.uniform(d,h-d) ##針の片方の端点を落とす場所
   theta = random.uniform(0, 2*math.pi) ##落とした針が倒れる方向
   line_cross.append(CheckLine(y, y + l*math.cos(theta)))
   if CheckLine(y, y + l*math.cos(theta)) == 0:
       canvas.create_line(x, y, x + l*math.sin(theta), y + l*math.cos(theta))
   else:#針が先にかかった場合針を赤く表示
       canvas.create_line(x, y, x + l*math.sin(theta), y + l*math.cos(theta), fill = 'blue')
   i += 1

canvas.place(x=0, y=900-h)

m = sum(line_cross)
print('交差した針の数:' + str(m))
print('π近似値 :' + str(n/m))

root.mainloop()
