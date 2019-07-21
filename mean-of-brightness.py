import cv2
import matplotlib.pyplot as plt
import numpy as np

register=[0]*600
i=0

cam = cv2.VideoCapture(0)
while True:

    _, im = cam.read()

    cv2.imshow('PUSH ENTER KEY', im)
    mean=im.mean()
    print(mean)
    register[i]=mean
    i+=1
    if cv2.waitKey(1) == 13: break
cam.release()
cv2.destroyAllWindows()


plt.figure(figsize=(5,5)) # プロットのサイズ（plotより前に実行する）

x = np.linspace(1, 600, 600)
y = register
regmean=np.mean(register[20:i])

plt.plot(x, y) # プロット
plt.xlabel("time") # 横軸のラベル
plt.ylabel("brightness") # 縦軸のラベル
plt.xlim(0, i+10) # 横軸の表示範囲
plt.ylim(regmean-5,regmean+5) # 縦軸の表示範囲
