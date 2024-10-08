'''@article{XU2023284,
    author = {Bowen Xu and Jiakun Xu and Nan Xue and Gui-Song Xia},
    title = {HiSup: Accurate polygonal mapping of buildings in satellite imagery with hierarchical supervision},
    journal = {ISPRS Journal of Photogrammetry and Remote Sensing},
    volume = {198},
    pages = {284-296},
    year = {2023},
    issn = {0924-2716},
    doi = {https://doi.org/10.1016/j.isprsjprs.2023.03.006},
}'''
import numpy as np
from squeeze.squeeze import region_grow

def lsgenerator(offset):
    H, W = offset.shape[1:]
    offset = np.sign(offset)*np.exp(-np.abs(offset))
    offset[0] *= W
    offset[1] *= H
    offset_x = offset[0]
    offset_y = offset[1]

    xx,yy = np.meshgrid(range(W),range(H))
    xx = np.array(xx,dtype=np.float32)
    yy = np.array(yy,dtype=np.float32)

    xx += offset_x
    yy += offset_y

    xx, yy = xx.flatten(), yy.flatten()
    offset_x = offset_x.flatten()
    offset_y = offset_y.flatten()
    ind = np.where(np.logical_and(np.logical_and(xx>=0, xx<=W-1),np.logical_and(yy>=0, yy<=H-1)))[0]

    xx, yy = xx[ind], yy[ind]
    ox, oy = offset_x.flatten()[ind], offset_y.flatten()[ind]
    theta = np.mod(np.arctan2(oy,ox)+np.pi/2.0,np.pi)
    rects = region_grow(xx, yy, theta, np.array([H, W], dtype=np.int32))

    return rects, xx, yy
