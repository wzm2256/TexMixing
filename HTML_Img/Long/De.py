import os
import matplotlib.pyplot as plt
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
denoise_wavelet, estimate_sigma)

import PIL.Image as Image
import numpy as np

All_folder = os.listdir()
for f in All_folder:
    if os.path.isdir(f) == False:
        continue
    if os.path.isdir(f + '_De/') == False:
        os.mkdir(f + '_De/')

    List=os.listdir(f)
    for i in List:
        I=Image.open(f + '/' +i)
        I_a = np.array(I)
        I_d = denoise_tv_chambolle(I_a, weight=0.01, multichannel=True)
        # I_d = denoise_wavelet(I_a, multichannel=True, convert2ycbcr=True)
        plt.imsave(f + '_De/' + i, I_d)