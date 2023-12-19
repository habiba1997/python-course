import cv2
import numpy as np

image = cv2.imread('./Archive/lena.jpg', 0)
cv2.imshow('image', image)

# transformations:
# scaling: making image bigger or smaller
# cv2.resize(image, output_image, output_image_size, fx_scale_factor_in_x_axis,
#            fy_scaling_factor_in_y_axis, interpolation_method_for_scaling)

#  scale down half
resize = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('resize', resize)

# translation: shifting image location
# cv2.warpAffine(image, transformation_matrix, output_image_size)
matrix = np.float32([[1, 0, 100], [0, 1, 100]])
row, col = image.shape
transform_image = cv2.warpAffine(image, matrix, (col, row))
cv2.imshow('transformation', transform_image)

# rotation: rotating an image at specific angle
# transformation matrix is the difference here
# cv2.warpAffine(image, transformation_matrix, output_image_size)
# center is 1st parameter, then specify the kind of rotation you want, scale factor 1 (no scaling)
rot_matrix = cv2.getRotationMatrix2D((col / 2, row / 2), 90, 1)
rot_image = cv2.warpAffine(image, rot_matrix, (col, row))
cv2.imshow('rotation', rot_image)

cv2.waitKey(10000)
cv2.destroyAllWindows()
