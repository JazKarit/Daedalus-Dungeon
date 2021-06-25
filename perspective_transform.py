# import the necessary packages
import numpy as np
import cv2
def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype = "float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # return the ordered coordinates
    return rect

def four_point_transform(image, out_pts):
    # obtain a consistent order of the points and unpack them
    # individually
    dims = np.shape(image)
    in_pts = np.array([(0,0),(0,dims[1]),(dims[0],0),(dims[0],dims[1])], dtype = "float32")
    in_rect = order_points(in_pts)

    out_rect = order_points(out_pts)

    (out_width,out_height) = np.shape(out_rect)

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(in_rect, out_rect)
    warped = cv2.warpPerspective(image, M, (400, 400),borderValue=(250,250,250))
    # return the warped image
    return warped

def wall_transform(img_path,wall):
    image = cv2.imread(img_path)
    if wall == 'center':
        return cv2.resize(image,(150,150))
    
    image = cv2.resize(image,(350,350))
    dims = np.shape(image)

    if wall == 'right':
        pts = np.array([(0,85),(0,dims[1]-85),(dims[0],0),(dims[0],dims[1])], dtype = "float32")
    elif wall == 'left':
        pts = np.array([(0,0),(0,dims[1]),(dims[0],85),(dims[0],dims[1]-85)], dtype = "float32")

    warped = four_point_transform(image, pts)    
    return warped

# right_wall = wall_transform('puzzle_door.jpg','right')
# left_wall = wall_transform('puzzle_door.jpg','left')
# center_wall = wall_transform('puzzle_door.jpg','center')

# # show the original and warped images
# cv2.imshow("Right", right_wall)
# cv2.imshow("Left", left_wall)
# cv2.imshow("Center", center_wall)
# cv2.waitKey(0)