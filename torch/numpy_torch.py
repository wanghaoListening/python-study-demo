import torch
import numpy as np
import torch.nn.functional as F     # 激励函数都在这
from torch.autograd import Variable

# tensor 与 numpy 互相转换
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
tensor_to_array = torch_data.numpy()

print(np_data)
print(torch_data)
print(tensor_to_array)


# abs ,mean,sin

data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)

print(np.mean(data))
print(torch.mean(tensor))


# 二维 矩阵运算

two_dim_data = [[1, 2], [3, 4]]
two_dim_tensor = torch.FloatTensor(two_dim_data)

print(torch.mm(two_dim_tensor, two_dim_tensor))
print(np.matmul(two_dim_data, two_dim_data))
print(two_dim_data.dot(two_dim_data))


# 变量 变量 (Variable)


# 什么是激励函数 (Activation Function)
# 做一些假数据来观看图像
x = torch.linspace(-5, 5, 200)  # x data (tensor), shape=(100, 1)
x = Variable(x)

x_np = x.data.numpy()   # 换成 numpy array, 出图时用

# 几种常用的 激励函数
y_relu = F.relu(x).data.numpy()
y_sigmoid = F.sigmoid(x).data.numpy()
y_tanh = F.tanh(x).data.numpy()
y_softplus = F.softplus(x).data.numpy()
# y_softmax = F.softmax(x)  softmax 比较特殊, 不能直接显示, 不过他是关于概率的, 用于分类











