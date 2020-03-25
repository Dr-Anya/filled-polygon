# QUESTIONS
ONE
1. Describe using a working examples, the relationship between the following coordinate systems in the graphics (OCS - object coordinate system WCS - world coordinate system VCS - viewing coordinate system CCS - clipping coordinate system NDCS -normalized device coordinate system DCS - device coordinate system)
b) Why do we need homogeneous coordinates?

2. Our good Classrep Kimani , is a fan of Chess. He has lost his chessboard. Write a program in OpenGL that implements a 8 by 8 chessboard. Kimani prefers brown and white color instead of black and white . Help Kimani out!

TWO
1. using OpenGL, write a program that draws a circle using Bresenham circle drawing algorithm: The parameters for the circle are as follows – the radius should be 4 Centimeters and the starting point coordinates are (3,5)
a. Draw the same circle at start coordinates (-2,-1) and fill it with Cyan shade (hint RGB #00ffff)
2. Using a working example , Write an OpenGL routine to split a concave polygon, using the vector method as described in Chapter 2 of our reading Text (Hearn, Baker and Carithers book called Computer Graphics with Open GL)

THREE
1.Using OpenGL draw a filled polygon with the following dimensions (8,4;2,4;0,8;3,12;7,12;10,8) hint (GL POLYGON function ) might be useful
a. Write a function to fill the polygon above in Red (#FF0000.)
b. write program to scale up (scaling) the polygon by a factor of 2
c. Write a procedure to fill the interior of a given polygon with shades of asterisks

FOUR
1. using OpenGL, write a program that draws a circle using Midpoint circle drawing algorithm: The parameters for the circle are as follows – the radius should be 5 Centimeters and the starting point coordinates are (0,3)
a. write a program to rotate the Circle 90 degrees and fill it with purple shade (hint RGB #800080)
2. Using a working example , Write an OpenGL routine to split a concave polygon, using the rotational method as described in Chapter 2 of our reading Text (Hearn, Baker and Carithers book called Computer Graphics with Open GL)

FIVE
1. Using OpenGL, write a program that draws a line using Gupta-Sproull algorithm line drawing algorithm: The parameters for the line are as follows –the starting point (20, 10) and ending coordinates (30, 18).
a. What is Line raterization and the anti-aliasing
i. Describe using your line drawn above how is Gupta-Sproull anti-aliasing
2. Using OpenGL, write a program that draws a line using Xiaolin Wu's line algorithm line drawing algorithm: The parameters for the line are as follows –the starting point (15, 10) and ending coordinates (23, 18).
i. Demonstrate using the example the Xiaolin Wu's line algorithm does anti-aliasing

SIX
Next week there is freshers Bash in Juja , they have heard you are the computer graphic Guru. The organizers want a banner written : JKUAT ROCKS (the words JKUAT in green and OCKS in Red) ….they also prefer a brown background (might be ugly but client is always right!)
a. Demonstrate how this can be achieved Using OpenGL( you may use TrueType and OpenType fonts if need be)
b. If your client complains that the text size is small how would you increase? please demonstrate with a working code

SEVEN
A survey was carried out in Gachororo about youth preference on fruits. 150 youth were interviewed about their fruits of preference as follows 
Fruit: Ovacado Orange Banana Kiwifruit Mangos Grapes 
People: 36 31 11 26 40 6
a) Write an OpenGL program that displays the bar chart. Input to the program is to include the data points and the labeling required for the x and y axes. The data points are to be scaled by the program so that the graph is displayed across the full area of a display window. (reading Chapter on Graphics Output Primitives in the book will help)
i. Ensure that each bar has the color that closely resembles the ripe fruit under consideration
ii. label your x axis as well in black and Y axis in Red
b) Suppose we wish to start the graph at point (5,5) on the display window, demonstrate how this would be achieved using your question case example

EIGHT
A survey was carried out in Gachororo about average youth daily earnings and reported as follows 
Day: Mon Tue Wed Thurs Fri Sat 
KSh: 500 850 600 570 1000 1020
a) Write an OpenGL program that displays the line graph . Input to the program is to include the data points and the labeling required for the x and y axes. The data points are to be scaled by the program so that the graph is displayed across the full area of a display window. (reading Chapter on Graphics Output Primitives in the book will help)
i. In the first case the data points are to be displayed as asterisks joined with straight-line segments, and the x and y axes are to be labeled according to input specifications
ii. In the second case , increase the width of the line to 2 and use small boxes as data marks
iii. In the third case the draw the line using the blue color and data points as small circles in red and the chart background to be cream (#FFFDD0)

NINE
Using the data provided in Question for group 7 , Write a program to draw a pie chart ( the pie chart should represent the percentages) .
i. The output of the program should have the name of the pie chart, and the names of the intervals. Each section label is to be displayed outside the boundary of the pie chart near the corresponding pie section.
ii. Redraw the same Pie chart using the section colors that closely resemble the ripe fruit and put the label and the percentage near its corresponding section
iii. How would you convert the chart background to gray scale using OpenGL code? demonstrate how this can be achieved

TEN
a) Write a working algorithm for implementing a color lookup table that we discussed in class
b) The local ice cream shop keeps track of how much ice cream they sell versus the noon temperature on that day. Here are their figures for the last 12 days: (source https://www.mathsisfun.com/data/scatter-xy-plots.html) D
Ice Cream Sales vs Temperature
Temperature °C--Ice Cream Sales
14.2°       $215
16.4°       $325
11.9°       $185
15.2°       $332
18.5°       $406
22.1°       $522
19.4°       $412
25.1°       $614
23.4°       $544
18.1°       $421
22.6°       $445
17.2°       $408
Using OpenGL draw the following based on the above data, attempt to replicate the output shown below where the data points are in blue #0000FF and the line of best fit or trend line is in orange (#FFA500) . Ensure that your axis are also labeled
Draw the line of best fit using the DDA algorithm we discussed in class.
###################################################3

ELEVEN
a) Suppose you have a system with a 12 inch by 14 inch video monitor that can display 120 pixels per inch. If memory is organized in one byte words, the starting frame buffer address is 0, and each pixel is assigned 4 bits of storage, what is the frame buffer address of the pixel with screen coordinates (x, y)?
b) Using OpenGL Draw a figure with coordinate points A(0, 4), B(3, 4), C(4, 0), D(0, 0).
i. Apply the translation with distance 2 towards X axis and 2 towards Y axis. Obtain the new coordinates of the square.
ii. The translated figure should have a green border line and cream inner shading
iii. write an openGL program to rotate the translated figure on Rotation angle = θ = 30º and show the output

TWELVE
a) Using a working example, prove that the multiplication of transformation matrices for each of the following sequences is commutative:
i. Two successive rotations.
ii. Two successive translations.
iii. Two successive scalings.
b) Using openGL, draw a triangle with vertices (-1,6 ; 2,0; -4,9)
Write a program
i. Rotate the triangle with a rotation of -45 degrees
ii. Vary the shading of the rotated triangle to have a mix of the three primary colors (Below is a hint of
how the color shades should look like in the rotated triangle ….Any color shade fashion will suffice ).. a soft-fill algorithm can achieve this ##############################################3

THIRTEEN
a) Using OpenGL, Write a boundary-fill procedure to fill an 8-connected region of your choice.
b) Use the midpoint method and symmetry considerations to scan convert the parabola
y = 50 − x2
over the interval −5 ≤ x ≤ 5.
Show the working of the method
Draw the Parabola using OpenGL and offer it the shade of your choice
(for more on this read the chapter on Implementation Algorithms for Graphics Primitives and Attributes)
c) Calculate the points between the starting point (18,17) and ending point (43, 4) using Midpoint Line drawing algorithm .
and plot the line using OpenGL ( show the working and also the program plus the plot)

FOURTEEN
1. How would you set the color of OpenGl display to green and change the fill color to have texture? Do a demonstration example with the circle with parameter starting coordinates (-3,-6) and radius of 4 cm and texture type of the circle of your choice ( mention in the write up what you used)
i. Using an OpenGL program. write a program to apply the reflection of the above circle on the X axis , show the new coordinates of the object.
ii. Write an OpenGl program to scale up (scaling circle starting at (-3,-6) and radius of 2 cm with a scale of 2

FIFTEEN
1. Using Open GL and midpoint ellipse algorithm , draw an Ellipse with centre as (-2,2) given by
##########################################
a. Apply the flood-fill algorithm to fill the interior ellipse with cyan Color
b. Apply shear parameter 2 on X axis and 2 on Y axis and find out the new coordinates of the Ellipse drawn above and plot the resulting figure using openGL
c. Rotate the original ellipse at a rotation angle of - 140
d. Develop an algorithm for antialiasing elliptical boundaries above
e. Using Open GL write a program to boundary fill of the ellipse in (b) with color Green
