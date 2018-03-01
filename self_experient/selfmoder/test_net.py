#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
from argparse import ArgumentParser
from os.path import join
import argparse
import sys
#caffe_root = '/home/yaochuanqi/work/caffe/'  # Change this to the absolute directory to ENet Caffe
#caffe_root='/home/liuli/liuli/trc/baidu/chihiro/caffe/cmake-build-release/'
caffe_root='/home/liuli/2018trc/autopilot-thirdparty/thirdparty/caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import math

#in_path = 'anchor_lane_504.txt'
in_path='/home/liuli/Desktop/trcsegdata/file.txt'
__author__ = 'Timo Samann'
__university__ = 'Aschaffenburg University of Applied Sciences'
__email__ = 'Timo.Saemann@gmx.de'
__data__ = '24th May, 2017'

#def sigmoid(x):
#    return 1 / (1 + math.exp(-x))
def sigmoid(x):
    x = np.array(x)
    return 1 / (1 + np.exp(-x))

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True, help='.prototxt file for inference')
    parser.add_argument('--weights', type=str, required=True, help='.caffemodel file')
    parser.add_argument('--out_dir', type=str, default=None, help='output directory in which the segmented images '
                                                                   'should be stored')
    parser.add_argument('--list', type=str, default='', help='input image list for processing')
    parser.add_argument('--gpu', type=str, default='0', help='0: gpu mode active, else gpu mode inactive')

    return parser
def sub_mean(input_image, vb, vg, vr):
    #substract mean
    b_channel =vb *  np.ones((input_shape[2], input_shape[3]),dtype = np.uint8)
    g_channel =vg *  np.ones((input_shape[2], input_shape[3]),dtype = np.uint8)
    r_channel =vr *  np.ones((input_shape[2], input_shape[3]),dtype = np.uint8)
    input_image[0,:,:] = input_image[0, :, :] - b_channel
    input_image[1,:,:] = input_image[1, :, :] - g_channel
    input_image[2,:,:] = input_image[2, :, :] - r_channel
    return input_image

def get_lane_width(path, height, row_start, cut_height):
    anchor_lane_width_ = [0.06611046,0.22281804,0.39531998,0.56504091,0.73476184]
    return anchor_lane_width_

def nms(scores, max_gap):
    selected = []
    current = {"index":0, "score":0}
    threshold = 0.15
    for i,s in enumerate(scores):
       if i - current['index'] > max_gap:
           if current['score'] > threshold:
               selected.append(current) 
               current = {"index":i, "score":s}
       if s > current['score']:
           current = {"index":i, "score":s}
    if len(selected) > 0 and current['score'] > threshold:
        selected.append(current) 
    return [ x['index'] for x in selected ]

if __name__ == '__main__':
    threshold = 0.
    parser1 = make_parser()
    args = parser1.parse_args()

    caffe.set_mode_gpu()
    print 'ok1'
    net = caffe.Net(args.model, args.weights, caffe.TEST)

    
    input_shape = net.blobs['data'].data.shape
    print input_shape
    lines = [line.strip() for line in open(args.list, 'r').readlines()]
    for line in lines:
	line=line.split(' ')[0]	
        image_path = '/home/liuli/Desktop/trcsegdata'+line
	print line
        sux = os.path.splitext(line)
        if sux[-1] != '.jpg':
            continue
        image = cv2.imread(image_path)
	print "img.shape:"
	print image_path

        img_row_start = 0
        img_height_in = 1280
        resize_height = 1280
        resize_width = 1920

        image_cut = cv2.resize(image, (resize_width, resize_height))
        image_resize = image_cut[img_row_start:img_row_start + img_height_in, :, :]

        #input_image = cv2.imread(image_path, 1).astype(np.float32)
	input_image = cv2.imread(image_path, 1).astype(np.uint8)
        input_image = cv2.resize(input_image, (resize_width, resize_height))
        input_image = input_image[img_row_start:img_row_start + img_height_in, :, :]
        input_image = input_image.transpose((2, 0, 1))
	
        #out = net.forward_all(**{net.inputs[0]: input_image})
	out = net.forward_all(**{net.inputs[0]: input_image})
        #data = net.blobs['conv9_1_us'].data[0]
	data = net.blobs['conv9_1_us'].data[0]
	img=np.zeros((resize_height,resize_width),dtype=np.uint8)
	for i in range(0,resize_height):
		for j in range(0,resize_width):
			if(data[0,i,j]>data[1,i,j]):
				img[i,j]=0
			else:
				img[i,j]=50
			

        width_fea = data.shape[2]
        height_fea = data.shape[1]

        cv2.imshow("res", img)
        k = cv2.waitKey(0)
        if k == 27: break

