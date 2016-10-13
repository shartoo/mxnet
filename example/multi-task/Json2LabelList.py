# -*- coding:utf-8 -*-
'''
将json格式的文件中的信息转换为mxnet所需要的文件和标签列表形式
'''

import json

j = json.loads("D:/data/bot/carTags_Train.json")
i =0
for filename in j.keys():
    if i<5:
        print j[filename]
        i+=1


