## python3 的 matplotlib绘图库的使用

**figure函数，创建图表**

```python
import matplotlib.pyplot as plt
plt.figure(1,dpi=80)   #创建图表1
plt.figure(2)   #创建图表2
plt.show()      #显示所有图表
```

**subplot函数，创建子图**

```python
import matplotlib.pyplot as plt
plt.figure(1)       #创建图表1
plt.subplot(233)    #创建2*3的图表矩阵（2行，3列），绘制的子图为矩阵中的3序号
plt.show()          #显示所有图表
```

**在多个表中创建子图**

```python
import matplotlib.pyplot as plt
plt.figure(1,dpi=80)    #创建图表1
plt.subplot(111)        #在图表1中创建子图
plt.figure(2,dpi=80)    #创建图表2
plt.subplot(221)        #在图表2中创建子图
plt.show()              #显示所有图表
```

**plot函数，画函数图像**

```python
import numpy as np
import matplotlib.pyplot as plt
 
plt.figure(1,dpi=50)
x= np.linspace(-np.pi,np.pi,100)  # x轴的定义域为 -3.14~3.14，中间间隔100个元素
plt.plot(x,np.sin(x))
plt.show()
```

**sca函数，选择子图**

```python
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1,dpi=50)
ax1 = plt.subplot(211)      #创建子图 ax1
ax2 = plt.subplot(212)      #创建子图 ax2

x = np.linspace(0,10,100)   # x轴定义域

plt.sca(ax1)                #选择子图ax1
plt.plot(x,np.exp(x))       #在子图ax1 中绘制函数 exp(x)

plt.sca(ax2)                #选择子图ax2
plt.plot(x,np.sin(x))       #在子图ax2 中绘制函数 sin(x)
plt.show()                  #展示所有图表
```

**使用hist函数，画直方图**

```python
import matplotlib.pyplot as plt

plt.figure(1, dpi=50)   # 创建图表1
data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
plt.hist(data, 20)      # 只要传入数据，直方图就会统计数据出现的次数，第二个参数控制宽度
plt.show()
```

**用scatter绘制散点图**

```python
import numpy as np
import matplotlib.pyplot as plt
 
plt.figure(1,dpi=50)
x= np.linspace(-np.pi,np.pi,100)  # x轴的定义域为 -3.14~3.14，中间间隔100个元素
plt.scatter(x,np.sin(x))
plt.show()
```

**用pie绘制饼图**

```python
import matplotlib.pyplot as plt
data = [200,700,100]                    #饼图中的数据
fig = plt.figure(dpi=80)
plt.pie(data,                               # 每个饼块的实际数据，如果大于1，会进行归一化，计算percentage
        explode=[0.0,0.0,0.0],              # 每个饼块离中心的距离
        colors=['y','r','g'],               # 每个饼块的颜色,黄红绿
        labels=['Best','Normal','Worst'],   # 每个饼块的标签
        labeldistance=1.2,                  # 每个饼块标签到中心的距离
        autopct='%1.1f%%',                  # 百分比的显示格式
        pctdistance=0.4,                    # 百分比到中心的距离
        shadow=True,                        # 每个饼块是否显示阴影
        startangle=0,                       # 默认从x轴正半轴逆时针起
        radius=1                            # 饼块的半径
        )
plt.show()
```

**图表的注释与标识**

```python
import numpy as np  
import matplotlib.pyplot as plt
fig = plt.figure(dpi=80)
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x),label="sin(x)")    #先设置一个label用于显示图例
plt.xlabel("X axe")     #设置X轴的文字
plt.ylabel("Y axe")     #设置Y轴的文字
plt.title("sin(x) function")    #设置图的标题
plt.legend()                        #显示图例。
plt.show()
```