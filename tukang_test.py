# TUKANG V0.02

import svgwrite
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Declare font
font_file = 'fonts/BarlowCondensed-Regular.ttf'
font_name = 'Barlow Condensed Regular'
pdfmetrics.registerFont(TTFont(font_name, font_file))

# Startup message
print("Running tukang v0.02..")
print(r"""
    __         __                   
   / /_ __ __ / /__ ___ _ ___  ___ _
  / __// // //  '_// _ `// _ \/ _ `/
  \__/ \_,_//_/\_\ \_,_//_//_/\_, / 
                             /___/  v0.02  
""")

while True:

    # Check if filename_svg already exists
    count_svg = 1
    filename_svg = 'ROL-ZONE1_{}.svg'
    while os.path.isfile(filename_svg.format(count_svg)):
        count_svg += 1
    filename_svg = filename_svg.format(count_svg)

    # Check if filename_ai already exists
    count_ai = 1
    filename_ai = 'ROL-ZONE1_{}.ai'
    while os.path.isfile(filename_ai.format(count_ai)):
        count_ai += 1
    filename_ai = filename_ai.format(count_ai)

    # Prompt user for box dimensions in meters
    width1_m = float(input("Enter length (in meters): "))
    width2_m = float(input("Enter width (in meters): "))
    height1_m = float(input("Enter body height (in meters): "))
    height2_m = float(input("Enter footer height (in meters): "))
    
    # Convert meter values to SVG units (points)
    width1 = width1_m * 2834.645
    width2 = width2_m * 2834.645
    height1 = height1_m * 2834.645
    height2 = height2_m * 2834.645
    
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
    text_style = f'font-size: {text_size}pt; text-anchor: middle;'

    # Create SVG file
    dwg = svgwrite.Drawing(filename_svg, size=(box_width * 2, box_height + (box_height / 5)))

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

    # Generate .svg file 
    dwg.save()
    print(filename_ai + " generated!\n")

    # Convert .svg to .ai
    svg_file = f'./{filename_svg}'
    ai_file = f'./{filename_ai}'
    drawing = svg2rlg(svg_file)

    # Create canvas and set font
    c = canvas.Canvas(ai_file)
    c.setFont(font_name, text_size)

    # Draw to canvas and save file
    renderPDF.draw(drawing, c, 0, 0)
    c.save()