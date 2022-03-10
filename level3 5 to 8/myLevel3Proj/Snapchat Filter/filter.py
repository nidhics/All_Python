
import cv2, dlib
from imutils import face_utils

def apply_sprite(frame, p2sprite, w, x, y, ontop = True):
	sprite = cv2.imread(p2sprite, -1)
	# print(sprite.shape)
	factor = (w/sprite.shape[1])*4
	
	sprite = cv2.resize(sprite, (0,0), fx=factor, fy=factor)

	frame = draw_sprite(frame, sprite, x, y)

def draw_sprite(frame, sprite, x, y):
	(h,w) = (sprite.shape[0], sprite.shape[1])	
	for c in range(3):


		frame[y:y+h, x:x+w, c] = sprite[:,:,c] * (sprite[:,:,3]/255.0) + frame[y:y+h, x:x+w,c] * (1.0 - sprite[:,:,3]/255.0)

	return frame


def calc_bbox(coords):
	x = min(coords[:,0])
	y = min(coords[:,1])
	w = max(coords[:,0]) - x
	h = max(coords[:,1]) - y
	return (x,y,w,h)

def get_bbox(points, part):
	if part == 1:
		(x,y,w,h) = calc_bbox(points[17:22])	#left eyebrow
	elif part == 2:
		(x,y,w,h) = calc_bbox(points[22:27])	#right eyebrow
	elif part == 3:
		(x,y,w,h) = calc_bbox(points[36:42])	#left eye
	elif part == 4:
		(x,y,w,h) = calc_bbox(points[42:48])	#right eye
	elif part == 5:
		(x,y,w,h) = calc_bbox(points[29:36])	#nose
	elif part == 6:
		(x,y,w,h) = calc_bbox(points[48:68])	#mouth
	return (x,y,w,h)



vs = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
model = r'D://programming with python//level3 5 to 8//myLevel3Proj/Snapchat Filter/filters/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(model)

while True:
	ret, frame = vs.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector(gray)
	print(len(faces))
	for face in faces:
		(x,y,w,h) = (face.left(), face.top(), face.width(), face.height())

		# print(x)
		shape = predictor(gray, face)
		
		shape = face_utils.shape_to_np(shape)
		# print(len(shape[0]))
		# print(len(shape), len(shape[0]))
		# print(shape)
		(x0,y0,w0,h0) = get_bbox(shape, 1)	#left eyebrow
		(x2,y2,w2,h2) = get_bbox(shape, 5)	#nose

		apply_sprite(frame, r'D:/programming with python/level3 5 to 8/myLevel3Proj/Snapchat Filter/mustache.png', w2, x2-20, y2+20, ontop = False)

		apply_sprite(frame, r'D:/programming with python/level3 5 to 8/myLevel3Proj/Snapchat Filter/hat.png', w0, x0, y0-100, ontop = False)

	cv2.imshow('Snap', frame)
	
	if cv2.waitKey(1) == ord('q'):
		break

vs.release()
cv2.destroyAllWindows()
