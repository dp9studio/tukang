# TUKANG V0.01

import svgwrite
import os

while True:
    # Check if the filename already exists
    count = 1
    filename = 'ROL-ZONE1_{}.svg'
    while os.path.isfile(filename.format(count)):
        count += 1
    filename = filename.format(count)

    # Startup message

    print("Running tukang v0.01..")
    print(r"""
    __         __                   
   / /_ __ __ / /__ ___ _ ___  ___ _
  / __// // //  '_// _ `// _ \/ _ `/
  \__/ \_,_//_/\_\ \_,_//_//_/\_, / 
                             /___/  v0.01  
""")

    # Prompt user for box dimensions in meters
    height1_m = float(input("Enter body height in meters (or enter 'exit' to quit): "))
    if height1_m == 'exit':
        break
    height2_m = float(input("Enter footer height (in meters): "))
    if height2_m == 'exit':
        break
    width1_m = float(input("Enter length (in meters): "))
    if width1_m == 'exit':
        break
    width2_m = float(input("Enter width (in meters): "))
    if width2_m == 'exit':
        break
    
    # Convert meter values to SVG units (points)
    height1 = height1_m * 1000
    height2 = height2_m * 1000
    width1 = width1_m * 1000
    width2 = width2_m * 1000
    
    # Calculate box size and position
    box_width = width1 + width2
    box_height = height1 + height2
    box_x = max(0, (width2 - width1) / 2)
    box_y = max(0, (height2 - height1) / 2)
    
    # Calculate font size
    if box_height > box_width:
        text_size = int(width2 / 3)
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
    count += 1