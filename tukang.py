# TUKANG V0.03

import svgwrite
import os

# Startup message

print("Running tukang v0.03..")
print(r"""
    __         __                   
   / /_ __ __ / /__ ___ _ ___  ___ _
  / __// // //  '_// _ `// _ \/ _ `/
  \__/ \_,_//_/\_\ \_,_//_//_/\_, / 
                             /___/  v0.03  
""")

# Prompt user for unit of measurement
unit_input = input("Enter a unit of measurement to use (m, cm, mm, px, pt): ")

while True:
    # Check if the filename already exists
    count = 1
    filename = 'ROL-ZONE2_{}.svg'
    while os.path.isfile(filename.format(count)):
        count += 1
    filename = filename.format(count)

    # Check what the user inputed as unit of measurement
    if unit_input == 'm':
        # Prompt user for box dimensions in metres
        width1_input = float(input("Enter length (in metres): "))
        width2_input = float(input("Enter width (in metres): "))
        height1_input = float(input("Enter body height (in metres): "))
        height2_input = float(input("Enter footer height (in metres): "))
        # Amount of points equivalent to metres
        unit2point = 2834.645
    if unit_input == 'cm':
        # Prompt user for box dimensions in centimetres
        width1_input = float(input("Enter length (in centimetres): "))
        width2_input = float(input("Enter width (in centimetres): "))
        height1_input = float(input("Enter body height (in centimetres): "))
        height2_input = float(input("Enter footer height (in centimetres): "))
        # Amount of points equivalent to centimetres
        unit2point = 28.34645
    if unit_input == 'mm':
        # Prompt user for box dimensions in millimetres
        width1_input = float(input("Enter length (in millimetres): "))
        width2_input = float(input("Enter width (in millimetres): "))
        height1_input = float(input("Enter body height (in millimetres): "))
        height2_input = float(input("Enter footer height (in millimetres): "))
        # Amount of points equivalent to millimetres
        unit2point = 2.834645
    if unit_input == 'px':
        # Prompt user for box dimensions in pixels
        width1_input = float(input("Enter length (in pixels): "))
        width2_input = float(input("Enter width (in pixels): "))
        height1_input = float(input("Enter body height (in pixels): "))
        height2_input = float(input("Enter footer height (in pixels): "))
        # Amount of points equivalent to pixels
        unit2point = 1
    if unit_input == 'pt':
        # Prompt user for box dimensions in points
        width1_input = float(input("Enter length (in points): "))
        width2_input = float(input("Enter width (in points): "))
        height1_input = float(input("Enter body height (in points): "))
        height2_input = float(input("Enter footer height (in points): "))
        # Amount of points equivalent to points
        unit2point = 1

    # Converts the inputed values into SVG usable units (points)
    width1 = width1_input * unit2point
    width2 = width2_input * unit2point
    height1 = height1_input * unit2point
    height2 = height2_input * unit2point

    # Calculate box size and position
    box_width = width1 + width2
    box_height = height1 + height2
    if width2 < width1:
        box_x = max(0, (width2 - width1) / 2)
    else:
        box_x = max(0, (width1 - width2) / 2)
    if height2 < height1:
        box_y = max(0, (height2 - height1) / 2)
    else:
        box_y = max(0, (height1 - height2) / 2)
    
    # Calculate font size
    if box_height > box_width:
        text_size = int(width2 / 4)
    else:
        text_size = int(box_height / 10)
    # Set font of the text
    text_style = f'font-family: Barlow Condensed; font-size: {text_size}pt; text-anchor: middle;'

    # Create SVG file
    dwg = svgwrite.Drawing(filename, size=(box_width * 2, box_height + (box_height / 5)))

    # Add top-left rectangle
    rect1 = dwg.rect((box_x, box_y), (width1, height1), fill='none', stroke='black', stroke_width='2pt')
    dwg.add(rect1)

    # Add top-right rectangle
    rect2 = dwg.rect((box_x + width1, box_y), (width2, height1), fill='none', stroke='black', stroke_width='2pt')
    dwg.add(rect2)

    # Add bottom-left rectangle
    rect3 = dwg.rect((box_x, box_y + height1), (width1, height2), fill='none', stroke='black', stroke_width='2pt')
    dwg.add(rect3)

    # Add bottom-right rectangle
    rect4 = dwg.rect((box_x + width1, box_y + height1), (width2, height2), fill='none', stroke='black', stroke_width='2pt')
    dwg.add(rect4)
    
    # Duplicate the four rectangles and place them to the right
    rect5 = dwg.rect((box_x + box_width, box_y), (width1, height1), fill='none', stroke='black', stroke_width='2pt')
    dwg.add(rect5)

    rect6 = dwg.rect((box_x + box_width + width1, box_y), (width2, height1), fill='none', stroke='black', stroke_width='2pt')
    dwg.add(rect6)

    rect7 = dwg.rect((box_x + box_width, box_y + height1), (width1, height2), fill='none', stroke='black', stroke_width='2pt')
    dwg.add(rect7)

    rect8 = dwg.rect((box_x + box_width + width1, box_y + height1), (width2, height2), fill='none', stroke='black', stroke_width='2pt')
    dwg.add(rect8)

    # Add BACK text
    text_back = dwg.text('BACK', insert=(box_x + (width1 / 2), box_y + box_height + (box_height / 10) + (text_size / 3)), style=text_style)
    dwg.add(text_back)

    # Add LEFT text
    text_left = dwg.text('LEFT', insert=(box_x + width1 + (width2 / 2), box_y + box_height + (box_height / 10) + (text_size / 3)), style=text_style)
    dwg.add(text_left)
    
    # Add FRONT text
    text_front = dwg.text('FRONT', insert=(box_x + box_width + (width1 / 2), box_y + box_height + (box_height / 10) + (text_size / 3)), style=text_style)
    dwg.add(text_front)

    # Add RIGHT text
    text_right = dwg.text('RIGHT', insert=(box_x + box_width + width1 + (width2 / 2), box_y + box_height + (box_height / 10) + (text_size / 3)), style=text_style)
    dwg.add(text_right)

    dwg.save()
    print(filename + " generated!\n")