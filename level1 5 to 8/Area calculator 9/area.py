import math
#area calculator


def areacalculator():
    while True:
        _input_= input("Enter the shape you want to calculate area of: ").lower()
        print(_input_)
        area = 0
        #pie = 3.14
        if _input_ == "square":
            side = int(input("Enter the value of side: "))
            area = area + (side ** 2)
        elif _input_ == "circle":
            radius = int(input("Enter the value of radius: "))
            pie= round(math.pi,2)
            print(pie)
            area = area + (2 * pie * radius)
        elif _input_ == "rectangle":
            length = int(input("Enter the value of length: "))
            width = int(input("Enter the value of length: "))
            area = area + (length * width)
        elif _input_ == "triangle":
         base = int(input("Enter the value of base: "))
         height = int(input("Enter the value of height: "))
         area = area +(0.5 * base * height)
        else:
            print ("Select a valid shape")

        # print ("%0.2f" % area)
        print (f"{_input_} area is {area}")
      

areacalculator()