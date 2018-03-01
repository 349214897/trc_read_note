#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import numpy as np
from argparse import ArgumentParser
from os.path import join
import argparse
import sys
#caffe_root = '/home/yaochuanqi/work/caffe/'  # Change this to the absolute directory to ENet Caffe
caffe_root='/home/liuli/2018trc/autopilot-thirdparty/thirdparty/caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import math

in_path = 'anchor_lane_504.txt'
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
    net = caffe.Net(args.model, args.weights, caffe.TEST)
    input_shape = net.blobs['data'].data.shape
    lines = [line.strip() for line in open(args.list, 'r').readlines()]
    for line in lines:
        image_path = line
        sux = os.path.splitext(line)
        if sux[-1] != '.jpg':
            continue
        image = cv2.imread(image_path)
	print "img.shape:"
	print image_path

        img_row_start = 568
        img_height_in = 640
        resize_height = 1208
        resize_width = 1920

        image_cut = cv2.resize(image, (resize_width, resize_height))
        image_resize = image_cut[img_row_start:img_row_start + img_height_in, :, :]

        input_image = cv2.imread(image_path, 1).astype(np.float32)
        input_image = cv2.resize(input_image, (resize_width, resize_height))
        input_image = input_image[img_row_start:img_row_start + img_height_in, :, :]
        input_image = input_image.transpose((2, 0, 1))

        out = net.forward_all(**{net.inputs[0]: input_image})
        data = net.blobs['conv9_1'].data[0]

        width_fea = data.shape[2]
        height_fea = data.shape[1]
        anchor_width = get_lane_width(in_path, height_fea, img_row_start, img_height_in)


        # find obj max pos
        # data:  x + pt + pt_score + vector + 5 * (to + tw) + 4 * cls  + 3 * group + bollard_x + bollard_score + bollard_type = 24
        pre_obj = np.zeros((height_fea, width_fea), dtype = np.float32)
        index_obj = -1 * np.ones((height_fea, width_fea), dtype = np.uint8)
        index_pt = -1 * np.ones(height_fea, dtype = np.uint8)
        #print("=======obj==========")
        for i in range(0, height_fea):
            for j in range(0, width_fea):
                obj_max = 0
                for a in range(0, len(anchor_width)):
                    obj = sigmoid(data[4 + 2 * a, i, j]) #to
                    if obj > obj_max:
                        obj_max = obj
                        index_obj[i,j]= a
                if obj_max > 0:
                    pre_obj[i,j] = obj_max
                else:
                    index_obj[i,j] = -1
                #print("%.2f" % pre_obj[i,j]),
            #print("")
        #print("==============index=================") 
        for i in range(0, height_fea):
            selected = nms(pre_obj[i,:], 3)
            for j in range(0, width_fea):
                if j not in selected:
                    index_obj[i,j] = -1
                #print(index_obj[i,j]),
            #print("")

        #print("=======pt score =======")
        for i in range(height_fea):
            pt_score  = sigmoid(data[2, i, :])
            selected = nms(pt_score, 5)
            for j in selected:
                pre_px = sigmoid(data[1, i, j]) + j
                if pre_px < 0.0:
                  continue
                x = int(pre_px * resize_width / width_fea)
                y = int (i) * img_height_in / height_fea
                cv2.circle(image_resize ,(x, y), 4 ,(0, 255, 0), 1)
            #print("")

        #find x correspond to max obj
        pre_cx = np.zeros((height_fea, width_fea), dtype = np.float32)
        pre_cw = np.zeros((height_fea, width_fea), dtype = np.float32)
        for i in range(0, height_fea):
            for j in range(0, width_fea):
                for a in range(0, len(anchor_width)):
                    if index_obj[i,j] == a:
                        pre_cw[i, j] = math.exp(data[4 + 2 * a + 1, i, j]) * float(anchor_width[a])  * width_fea
                        #pre_cw[i, j] = float(anchor_width[a])  * width_fea
                        #print(math.exp(data[4 + 2 * a + 1, i, j])),
                        #pre_cw[i, j] = float(anchor_width[a])  * width_fea
                        pre_cx[i, j] = sigmoid(data[0, i, j]) + j
                        break
            #print("")

        # draw pred point and width
        pointx = []
        pointy = []
        #print("===============obj===================")
        for i in range(0, height_fea):
            for j in range(0, width_fea):
                y = int (i) * img_height_in / height_fea
                x = int(pre_cx[i,j] * resize_width / width_fea)
                w = int(pre_cw[i,j] * resize_width / width_fea)
                lx = x - w / 2;
                rx = x + w / 2;
                lx = max(lx, 0)
                rx = min(rx, width_fea * resize_width / width_fea)
                if x == 0 or w == 0:
                    continue
                else:
                    #for a in range(0, len(anchor_width)):
                        #print("%.3f" % sigmoid(data[4 + 2 * a, i, j])),
                    #print("")
                    cv2.line(image_resize, (lx,y), (rx, y), (0, 0, 255), 2)
                    cv2.circle(image_resize ,(x, y), 4 ,(255, 0, 0), 1)
                    cls_start = 2 + 2 + 2 * 5 + 4
                    cls = np.argmax(data[cls_start:cls_start + 3,i,j])
                    cv2.putText(image_resize, str(cls), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0),2)
                    pointx.append(x)
                    pointy.append(y)
            #print("")

        #print("=======bollard pt score =======")
        for i in range(width_fea):
            pt_score = sigmoid(data[22, :, i])
            j = np.argmax(pt_score)
            if pt_score[j] < 0.2:
                continue
            pre_py = j + data[21, j, i]
            #print("%.4f " % data[21, j, i]),
            if pre_py < 0.0:
              continue
            y = int(pre_py * img_height_in / height_fea)
            x = int (i) * resize_width / width_fea
            if sigmoid(data[23, j, i]) > 0.5:
                cv2.circle(image_resize ,(x, y), 3 ,(0, 255, 0), 2)
            else:
                cv2.circle(image_resize ,(x, y), 3 ,(0, 0, 255), 2)
            y2 = int(j * img_height_in / height_fea)
            #print(y - y2)
            #print("")
        cv2.imshow("res", image_resize)
        k = cv2.waitKey(0)
        if k == 27: break

