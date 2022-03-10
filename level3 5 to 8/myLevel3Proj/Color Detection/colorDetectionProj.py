
import cv2
import pandas as pd

img = cv2.imread('colorpic.jpg')

# print(img)
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file with pandas and giving names to each column
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)#names give the name to each column 
# print(csv)
# print(csv.head())
# print(csv.tail())
# print(len(csv))
# print(csv.loc[0,"R"])
# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        # print(img[y,x])
        b = int(b)
        g = int(g)
        r = int(r)

# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 100 #minimum difference 
    for i in range(len(csv)):
        # abs -->absolute negative value will convert into +ve
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
       
        #finding closest value in csv list
        if d <= minimum:
            # print(d)
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

print(get_color_name(255,255,0))
cv2.namedWindow('color detection project')
cv2.setMouseCallback('color detection project', draw_function)

while True:

    cv2.imshow("color detection project", img)
    if clicked:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255),2)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'q' key
    if cv2.waitKey(1)==ord('q'):
        break
    # if cv2.waitKey(0):
    #     break
cv2.destroyAllWindows()