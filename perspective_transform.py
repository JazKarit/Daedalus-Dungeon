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

def bbox2(img):
    rows = np.any(img, axis=1)
    cols = np.any(img, axis=0)
    ymin, ymax = np.where(rows)[0][[0, -1]]
    xmin, xmax = np.where(cols)[0][[0, -1]]
    return img[ymin:ymax+1, xmin:xmax+1]

def four_point_transform(image, out_pts,out_dims=None):
    dims = np.shape(image)
    in_pts = np.array([(0,0),(0,dims[1]),(dims[0],0),(dims[0],dims[1])], dtype = "float32")
    in_rect = order_points(in_pts)

    out_rect = order_points(out_pts)

    if out_dims:
        (out_width,out_height) = out_dims
    else:
        (out_width,out_height) = np.shape(out_rect)
        xmin = np.min(out_rect,1)[0]
        ymin = np.min(out_rect,1)[1]
        xmax = np.max(out_rect,1)[0]
        ymax = np.max(out_rect,1)[1]
        out_width = xmax - xmin
        out_height = ymax - ymin

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(in_rect, out_rect)
    warped = cv2.warpPerspective(image, M, (out_width, out_height),borderValue=(250,250,250))
    # return the warped image
    return bbox2(warped)

def wall_transform(img_path,wall):
    image = cv2.imread(img_path)
    if wall == 'center':
        return cv2.resize(image,(120,150))
    
    image = cv2.resize(image,(300,350))
    dims = np.shape(image)

    length_shrink = 60

    if wall == 'right':
        pts = np.array([(0,length_shrink),(0,dims[1]-length_shrink),(dims[0]-170,0),(dims[0]-170,dims[1])], dtype = "float32")
        return four_point_transform(image,pts,(168,350))

    elif wall == 'left':
        pts = np.array([(0,0),(0,dims[1]),(dims[0]-170,length_shrink),(dims[0]-170,dims[1]-length_shrink)], dtype = "float32")
        return four_point_transform(image,pts,(168,350))

    warped = four_point_transform(image, pts)    
    return warped

def wall_transform_puzzle(puzzle_path,wall):
    puzzle = cv2.imread(puzzle_path)
    if wall == 'center':
        return cv2.resize(puzzle,(30,30))
    
    puzzle = cv2.resize(puzzle,(100,117))
    dims = np.shape(puzzle)

    length_shrink = 20

    if wall == 'right':
        pts = np.array([(0,length_shrink),(0,dims[1]-length_shrink),(dims[0]-57,0),(dims[0]-57,dims[1])], dtype = "float32")
        return four_point_transform(puzzle, pts, (60,115))  

    elif wall == 'left':
        pts = np.array([(0,0),(0,dims[1]),(dims[0]-57,length_shrink),(dims[0]-57,dims[1]-length_shrink)], dtype = "float32")
        return four_point_transform(puzzle, pts, (60,115))

# right_wall = wall_transform('puzzle_door.jpg','right')
# left_wall = wall_transform('puzzle_door.jpg','left')
# center_wall = wall_transform('puzzle_door.jpg','center')

# # show the original and warped images
# cv2.imshow("Right", right_wall)
# cv2.imshow("Left", left_wall)
# cv2.imshow("Center", center_wall)
# cv2.waitKey(0)