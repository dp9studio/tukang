# TUKANG V0.03
import svgwrite
import os
import sys

# Startup message
print("\nRunning tukang v0.03..")
print(r"""
    __         __                   
   / /_ __ __ / /__ ___ _ ___  ___ _
  / __// // //  '_// _ `// _ \/ _ `/
  \__/ \_,_//_/\_\ \_,_//_//_/\_, / 
                             /___/  v0.03  
""")

def program_exit():
    print("Exiting the bengkel..\n")
    sys.tracebacklimit = 0
    sys.exit(0)

def program_help():
    # Print the commands to the user
    print("\n")
    print("Exit/quit the program: !exit")
    print("Change the unit of measurement: !settings")
    print("\n")

def program_setting():
    global unit_output
    # Prompt user for unit of measurement
    while True:
        unit_input = input("Enter a unit of measurement to use (m, cm, mm, px, pt): ")
        if unit_input == '!exit':
            program_exit()
        elif unit_input == '!help':
            program_help()
            continue
        elif unit_input not in ('m', 'cm', 'mm', 'px', 'pt'):
            print("Invalid input or command!")
            continue
        elif unit_input == 'm':
            print("Input the following measurements in metres.\n")
        elif unit_input == 'cm':
            print("Input the following measurements in centimetres.\n")
        elif unit_input == 'mm':
            print("Input the following measurements in millimetres.\n")
        elif unit_input == 'px':
            print("Input the following measurements in pixels.\n")
        elif unit_input == 'pt':
            print("Input the following measurements in points.\n")
        unit_output = unit_input
        break

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def check_unit_input():
    # Default values
    restart_unit_input = False
    width1_input = 0
    width2_input = 0
    height1_input = 0
    height2_input = 0

    while True:
        if restart_unit_input:
            restart_unit_input = False
            continue
        # Prompt user for box dimensions in the requested unit of measurement
        while not restart_unit_input:
            width1_input = input("Enter length: ")
            if width1_input == '!exit':
                program_exit()
            if width1_input == '!help':
                program_help()
                continue
            if width1_input == '!settings':
                restart_unit_input = True
                program_setting()
                break
            if not is_float(width1_input):
                print("Error! Integers only.")
                continue
            width1_input = float(width1_input)
            break

        while not restart_unit_input:
            width2_input = input("Enter width: ")
            if width2_input == '!exit':
                program_exit()
            if width2_input == '!help':
                program_help()
                continue
            if width2_input == '!settings':
                restart_unit_input = True
                program_setting()
                break
            if not is_float(width2_input):
                print("Error! Integers only.")
                continue
            width2_input = float(width2_input)
            break

        while not restart_unit_input:
            height1_input = input("Enter body height: ")
            if height1_input == '!exit':
                program_exit()
            if height1_input == '!help':
                program_help()
                continue
            if height1_input == '!settings':
                restart_unit_input = True
                program_setting()
                break
            if not is_float(height1_input):
                print("Error! Integers only.")
                continue
            height1_input = float(height1_input)
            break

        while not restart_unit_input:
            height2_input = input("Enter footer height: ")
            if height2_input == '!exit':
                program_exit()
            if height2_input == '!help':
                program_help()
                continue
            if height2_input == '!settings':
                restart_unit_input = True
                program_setting()
                break
            if not is_float(height2_input):
                print("Error! Integers only.")
                continue
            height2_input = float(height2_input)
            break
        
        return width1_input, width2_input, height1_input, height2_input, restart_unit_input

# Print the help command to the user
print("\nType !help for program commands\n")

program_setting()

while True:
    # Check if the filename already exists
    count = 1
    filename = 'ROL-ZONE2_{}.svg'
    while os.path.isfile(filename.format(count)):
        count += 1
    filename = filename.format(count)

    # Check what the user inputed as unit of measurement
    if unit_output == 'm':
        width1_output, width2_output, height1_output, height2_output, restart_unit_output = check_unit_input()
        if restart_unit_output:
            continue
        # Amount of points equivalent to metres
        unit2point = 2834.645
    if unit_output == 'cm':
        width1_output, width2_output, height1_output, height2_output, restart_unit_output = check_unit_input()
        if restart_unit_output:
            continue
        # Amount of points equivalent to centimetres
        unit2point = 28.34645
    if unit_output == 'mm':
        width1_output, width2_output, height1_output, height2_output, restart_unit_output = check_unit_input()
        if restart_unit_output:
            continue
        # Amount of points equivalent to millimetres
        unit2point = 2.834645
    if unit_output == 'px':
        width1_output, width2_output, height1_output, height2_output, restart_unit_output = check_unit_input()
        if restart_unit_output:
            continue
        # Amount of points equivalent to pixels
        unit2point = 1
    if unit_output == 'pt':
        width1_output, width2_output, height1_output, height2_output, restart_unit_output = check_unit_input()
        if restart_unit_output:
            continue
        # Amount of points equivalent to points
        unit2point = 1

    # Converts the inputed values into SVG usable units (points)
    width1 = width1_output * unit2point
    width2 = width2_output * unit2point
    height1 = height1_output * unit2point
    height2 = height2_output * unit2point

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