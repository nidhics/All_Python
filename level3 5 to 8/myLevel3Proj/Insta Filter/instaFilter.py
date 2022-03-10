import cv2

#Read the image
image = cv2.imread('insta Filter\\bg.jpg')

#greyscale filter
# def greyscale(img):
#     greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     return greyscale

# #making the greyscale image
# a1 = greyscale(image)

# filename = 'insta Filter\greyscale.jpg'
# # Using cv2.imwrite() method
# # Saving the image
# cv2.imwrite(filename, a1)
# -----------------------------------------------------------------------------------

# # brightness adjustment
# def bright(img, beta_value ):
#     img_bright = cv2.convertScaleAbs(img, beta=beta_value)
#     return img_bright

# #making the  more bright image
# #positive beta value
# a2 = bright(image, 60)
# filename = 'more_bright.jpg'
# # Using cv2.imwrite() method
# # Saving the image
# cv2.imwrite(filename, a2)
# -----------------------------------------------------------------------------------

#grey pencil sketch effect
def pencil_sketch_grey(img):
    #inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.1) 
    return  sk_color
#making the grey pencil sketch
a6 = pencil_sketch_grey(image)

filename = 'insta Filter\pencil_grey.jpg'
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, a6)

img2=cv2.imread(filename)
cv2.imshow("pencil sketch",img2)
cv2.waitKey(0)