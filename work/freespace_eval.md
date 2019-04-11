## 模型448*640,数据从标记数据选出约800张
| 模型 | 注释 | accu | class accu| recall| pt_error| time(在有训练任务的情况) |
| - | :-: | -: |-: | -: | -: | -: |
|sfs_new_rule_addflip_batch20_2gpu_iter_90000.caffemodel| 双显卡batch20 |0.739720690453 | 0.762415841609 | 0.703891359593 | 15.926636053010151 | 9.61 ms|
|sfs_new_rule_addflip_batch2_iter_92000.caffemodel| 双显卡batch2 |0.942311537423 | 0.954305312941 | 0.937420584498 | 3.66420960796239 | 9.61 ms|
|sfs_new_rule_addflip_batch1_iter_118000.caffemodel| 双显卡batch1 |0.910327552255 | 0.941272509374 | 0.888357687421 | 6.526632091187734 | 9.61 ms|
|sfs_new_rule_addflip_batch1_single_iter_82000.caffemodel| 单显卡batch1 |0.924712082757 | 0.936421706524 | 0.89499682338 | 4.790613023757855 | 9.61ms|
|sfs_new_rule_addflip_batch2_2gpu_addfov_iter_50000.caffemodel(hwfinetune)| 双显卡batch2 |0.947077163462 |  0.972177503285 | 0.94498094028 | 3.319283323866174 | 9.61ms|
|sfs_new_rule_addflip_batch2_2gpu_addfov_addjunheng_iter_72000.caffemodel(hwfinetune)| 双显卡batch2 |0.954296051058 | 0.976865133442 | 0.950619440915 | 2.936089405189766 | 9.61 ms|
|sfs_new_rule_addflip_batch2_2gpu_addfov_iter_74000.caffemodel| 双显卡batch2 |0.945505150698 | 0.968828787366 | 0.939421855146 | 3.3211109144045956 | 9.61 ms|

## 模型448*640,数据从标记数据选出约800张(nostop)
| 模型 | 注释 | accu | class accu| recall| pt_error| time(在有训练任务的情况) |
| - | :-: | -: |-: | -: | -: | -: |
|multi_resolution| 双显卡batch2 |0.960169569161 | 0.972040423943 | 0.954038461538 | 2.57588005991584 | 9.58461538462 ms|
|multi_resolution_noconv8| 双显卡batch2 |0.739720690453 | 0.762415841609 | 0.703891359593 | 15.926636053010151 | 9.61 ms|

## 修改模型,添加了新的训练策略,修改了roi,增加了
final performance accu:  0.981325129426
final performance class accu:  0.979042270273
final performance recall:  0.980257556407
final performance pt_eror:  1.936125316595033
final performance time:  9.73052362708 ms

## 20190402
resdual 144点 nofinetune error front data
final performance accu:  0.962307393255
final performance class accu:  0.961841591641
final performance recall:  0.941730523627
final performance pt_eror:  3.798870337683614
final performance time:  14.8991060026 ms

yolo 72点  nofinetune error front data
final performance accu:  0.977760449861
final performance class accu:  0.968085482804
final performance recall:  0.975042571307
final performance pt_eror:  2.1793625572671034
final performance time:  7.30012771392 ms
