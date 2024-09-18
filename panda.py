import os
import tqdm
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import scipy.ndimage as ndi
from skimage import measure, color
import pandas as pd

import cv2
from easydict import EasyDict as edict

configs = {
    'THRESHOLD': 15,
    'INPUT_DIR': './1All', #
    'OUTPUT_DIR': './out-r',
    'AREA_LOW': 20,
    'LENGTH_WIDTH_RATIO': 0.8,  # 长宽比不能低于0.7，此参数用于过滤非圆形目标
    'COLOR_LIST': [(255,0,0),(0,255,0),(0,0,255)]
}


if __name__ == '__main__':

    cfg = edict(configs)

    images = os.listdir(cfg.INPUT_DIR)
    if not os.path.exists(cfg.OUTPUT_DIR):
        os.mkdir(cfg.OUTPUT_DIR)

    input_images = []
    nums = []
    nums_single = []
    nums_dense = []
    
    for fname in tqdm.tqdm(images):
        
        pump = 0
        single = 0
        dense = 0
                
        img = cv2.imread(os.path.join(cfg.INPUT_DIR, fname), flags=0)
        
        #! 二值化, numpy array
        img = np.where(img>cfg.THRESHOLD, 255, 0)
        
        rgb = Image.fromarray(np.uint8(img)).convert('RGB')
        draw = ImageDraw.Draw(rgb)
        
        label = measure.label(img)
        a = measure.regionprops(label)
        
        for (j, i) in enumerate(a):
            if cfg.AREA_LOW < i.area:
                min_row, min_col, max_row, max_col = i.bbox
                h, w = max_row-min_row, max_col-min_col
                color = (255,0,0)
                if cfg.LENGTH_WIDTH_RATIO < w/h < 1/cfg.LENGTH_WIDTH_RATIO:
                    #! 长宽比过大时，对数据进行切割
                    draw.rectangle([min_col, min_row, max_col, max_row],
                                width=2, outline=color)
                    pump += 1
                    single += 1
                else:
                    if w > h: #! 纵向切割
                        spilt_nums = int(w / h + 0.5)
                        color = (0,255,0)
                        for step in range(spilt_nums):
                            draw.rectangle([min_col+(step)*h, min_row, min_col+(step+1)*h, max_row],
                                width=2, outline=color)
                        
                    else: #! 横向切割
                        spilt_nums = int(w / h + 0.5)
                        color = (0,255,0)
                        for step in range(spilt_nums):
                            draw.rectangle([min_col, min_row+(step)*w, max_col, min_row+(step+1)*w],
                                width=2, outline=color)
                    pump += spilt_nums
                    dense += spilt_nums
        #! 保存图像
        input_images.append(f'{cfg.OUTPUT_DIR}/{fname}')
        nums.append(pump)
        nums_single.append(single)
        nums_dense.append(dense)
        rgb.save('./{}/{}.png'.format(cfg.INPUT_DIR, fname.split('.')[0]))


dataframe = pd.DataFrame({'Image_name': input_images,
                          'single_nums': nums_single,
                          'dense_nums': nums_dense,
                          'Total': nums})
dataframe.to_csv("pump.csv", index=False, sep=',')