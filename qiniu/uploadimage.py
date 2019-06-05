#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from qiniu import Auth, put_file, etag, BucketManager
import qiniu.config

"""
#需要填写你的 Access Key 和 Secret Key
access_key = 'wNgLCAVA5l2OKvkSvOjXQ4uiIjaOA4y3DV2qcGPe'
secret_key = 'rCfvELeYskvXiqufwBu_upIZnsIohzBFpt-N7ZUG'

#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'wanghaospace'

#上传到七牛后保存的文件名
key = 'my-python-logo.png';

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传文件的本地路径
localfile = '/home/wanghao/桌面/python.jpg'

res_ret, res_info = put_file(token, key, localfile)

#初始化BucketManager
bucket = BucketManager(q)

#获取文件的状态信息
file_ret, file_info = bucket.stat(bucket_name, key)
print("res_info=",res_info)

print("file_info",file_info)
print(file_ret)
assert res_ret['key'] == key
assert res_ret['hash'] == etag(localfile)

#wanghaospace的空间域名为 http://7xavwe.com1.z0.glb.clouddn.com/1994.jpg
#七牛的图片的外链地址为http://7xavwe.com1.z0.glb.clouddn.com加上图片的名字
"""


class QiNiuManager(object):

    def __init__(self):
        self.__access_key = 'wNgLCAVA5l2OKvkSvOjXQ4uiIjaOA4y3DV2qcGPe'
        self.__secret_key = 'rCfvELeYskvXiqufwBu_upIZnsIohzBFpt-N7ZUG'
        self.bucket_name = 'wanghaospace'
        self.auth = Auth(self.__access_key, self.__secret_key)

    def upload_image(self, localfile):
        if localfile is None or len(localfile) == 0:
            return
        str_list = localfile.split('/')
        key = str_list[-1]
        token = self.auth.upload_token(self.bucket_name, key, 3600)
        res_ret, res_info = put_file(token, key, localfile)
        if res_info.ok():
            full_name = "http://7xavwe.com1.z0.glb.clouddn.com/"+key
            print("%s的外链是%s" % (key, full_name))

    def image_stat(self, bucket, image_name):
        # 初始化BucketManager
        bucket_manager = BucketManager(self.auth)
        ret, info = bucket_manager.stat(bucket, image_name)
        print(info)

    def delete_image(self, bucket, image_name):
        bucket_manager = BucketManager(self.auth)
        ret, info = bucket_manager.delete(bucket, image_name)
        if ret == {}:
            print('图片删除成功')


if __name__ == "__main__":
    operate_id = sys.argv[1]
    operate_id = int(operate_id)
    uploader = QiNiuManager()
    if 1 == operate_id:
        #证明是要上传图片
        name = input('请输入图片的路径: ')
        uploader.upload_image(name)
    elif 2 == operate_id:
        #证明是要移动图片到其他bucket
        print('获取文件的基本信息; ')
        bucket = input('文件所在的空间： ')
        image_name = input('图片的名字： ')
        uploader.image_stat(bucket, image_name)
    else:
        #证明是要删除图片
        bucket = input('输入要删除图片的空间： ')
        image_name = input('输入要删除图片的名字： ')
        uploader.delete_image(bucket, image_name)

