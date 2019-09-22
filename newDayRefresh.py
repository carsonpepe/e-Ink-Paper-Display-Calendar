import epd7in5b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

def new_day_redraw():
    epd = epd7in5b.EPD()
    epd.init()
    #print("Clear...")
    epd.Clear(0xFF)
    # Drawing on the Vertical image
    HBlackimage = Image.new('1', (epd7in5b.EPD_HEIGHT, epd7in5b.EPD_WIDTH), 255)  # 298*126
    HRedimage = Image.new('1', (epd7in5b.EPD_HEIGHT, epd7in5b.EPD_WIDTH), 255)  # 298*126    
    
    # Vertical
    drawblack = ImageDraw.Draw(HBlackimage)
    drawred = ImageDraw.Draw(HRedimage)
    
    font_title = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 24)
    font_message = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 22)
    font_date = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 18)
    font_meeting = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 17)
    font_time_slot = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 16)
    font_time_small = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 14)
    
    drawred.text((68, 4), 'Main Conference Room', font = font_title, fill = 0)
    drawblack.line((70, 29, 314, 29), fill = 0)
    
    # Bottom Border for Title
    drawred.line((3, 60, 380, 60), fill = 0)
    drawred.line((3, 61, 380, 61), fill = 0)
    drawblack.line((2, 62, 381, 62), fill = 0)
    drawred.line((0, 63, 384, 63), fill = 0)
    drawred.line((0, 64, 384, 64), fill = 0)
    # Top Border for Title
    drawred.line((0, 0, 384, 0), fill = 0)
    drawred.line((0, 1, 384, 1), fill = 0)
    drawblack.line((2, 2, 381, 2), fill = 0)
    drawred.line((3, 3, 380, 3), fill = 0)
    drawred.line((3, 4, 380, 4), fill = 0)
    # Right Border for Title
    drawred.line((379, 5, 379, 59), fill = 0)
    drawred.line((380, 5, 380, 59), fill = 0)
    drawblack.line((381, 2, 381, 62), fill = 0)
    drawred.line((382, 2, 382, 62), fill = 0)
    drawred.line((383, 2, 383, 64), fill = 0)
    # Left Border for Title
    drawred.line((0, 2, 0, 64), fill = 0)
    drawred.line((1, 2, 1, 63), fill = 0)
    drawblack.line((2, 2, 2, 62), fill = 0)
    drawred.line((3, 3, 3, 59), fill = 0)
    drawred.line((4, 3, 4, 59), fill = 0)
    
    drawblack.line((383, 65, 383, 640), fill = 0)
    drawblack.line((382, 65, 382, 640), fill = 0)
    drawblack.line((0, 65, 0, 640), fill = 0)
    drawblack.line((1, 65, 1, 640), fill = 0)
    
    ###Time Slot Lines & Text###
    normal_tick_x2 = 5
    thirty_tick_x2 = 9
    time_text_x = 10
    # 9am Ticks & Text
    y_nine = 64
    drawblack.line((0, (y_nine + 10), normal_tick_x2, (y_nine + 10)))
    drawblack.line((0, (y_nine + 21), normal_tick_x2, (y_nine + 21)))
    drawblack.line((0, (y_nine + 32), thirty_tick_x2, (y_nine + 32)))
    drawblack.line((0, (y_nine + 43), normal_tick_x2, (y_nine + 43)))
    drawblack.line((0, (y_nine + 54), normal_tick_x2, (y_nine + 54)))
    drawblack.text((time_text_x, (y_nine + 1)), '9am', font = font_time_slot, fill = 0)
    # 10am Line
    y_ten = 128
    drawblack.line((0, y_ten, 384, y_ten), fill = 0)
    # 10am Ticks & Text
    drawblack.line((0, (y_ten + 10), normal_tick_x2, (y_ten + 10)))
    drawblack.line((0, (y_ten + 21), normal_tick_x2, (y_ten + 21)))
    drawblack.line((0, (y_ten + 32), thirty_tick_x2, (y_ten + 32)))
    drawblack.line((0, (y_ten + 43), normal_tick_x2, (y_ten + 43)))
    drawblack.line((0, (y_ten + 54), normal_tick_x2, (y_ten + 54)))
    drawblack.text((time_text_x, (y_ten + 1)), '10am', font = font_time_slot, fill = 0)
    # 11am Line
    y_eleven = 192
    drawblack.line((0, y_eleven, 384, y_eleven), fill = 0)
    # 11am Ticks & Text
    drawblack.line((0, (y_eleven + 10), normal_tick_x2, (y_eleven + 10)))
    drawblack.line((0, (y_eleven + 21), normal_tick_x2, (y_eleven + 21)))
    drawblack.line((0, (y_eleven + 32), thirty_tick_x2, (y_eleven + 32)))
    drawblack.line((0, (y_eleven + 43), normal_tick_x2, (y_eleven + 43)))
    drawblack.line((0, (y_eleven + 54), normal_tick_x2, (y_eleven + 54)))
    drawblack.text((time_text_x, (y_eleven + 1)), '11am', font = font_time_slot, fill = 0)
    # 12pm Line
    y_twelve = 256
    drawblack.line((0, y_twelve, 384, y_twelve), fill = 0)
    # 12pm Ticks & Text
    drawblack.line((0, (y_twelve + 10), normal_tick_x2, (y_twelve + 10)))
    drawblack.line((0, (y_twelve + 20), normal_tick_x2, (y_twelve + 20)))
    drawblack.line((0, (y_twelve + 31), thirty_tick_x2, (y_twelve + 31)))
    drawblack.line((0, (y_twelve + 42), normal_tick_x2, (y_twelve + 42)))
    drawblack.line((0, (y_twelve + 53), normal_tick_x2, (y_twelve + 53)))
    drawblack.text((time_text_x, (y_twelve + 1)), '12pm', font = font_time_slot, fill = 0)
    # 1pm Line
    y_one = 319
    drawblack.line((0, y_one, 384, y_one), fill = 0)
    # 1pm Ticks & Text
    drawblack.line((0, (y_one + 10), normal_tick_x2, (y_one + 10)))
    drawblack.line((0, (y_one + 21), normal_tick_x2, (y_one + 21)))
    drawblack.line((0, (y_one + 32), thirty_tick_x2, (y_one + 32)))
    drawblack.line((0, (y_one + 43), normal_tick_x2, (y_one + 43)))
    drawblack.line((0, (y_one + 54), normal_tick_x2, (y_one + 54)))
    drawblack.text((time_text_x, (y_one + 1)), '1pm', font = font_time_slot, fill = 0)
    # 2pm Line
    y_two = 383
    drawblack.line((0, y_two, 384, y_two), fill = 0)
    # 2pm Ticks & Text
    drawblack.line((0, (y_two + 10), normal_tick_x2, (y_two + 10)))
    drawblack.line((0, (y_two + 21), normal_tick_x2, (y_two + 21)))
    drawblack.line((0, (y_two + 32), thirty_tick_x2, (y_two + 32)))
    drawblack.line((0, (y_two + 43), normal_tick_x2, (y_two + 43)))
    drawblack.line((0, (y_two + 54), normal_tick_x2, (y_two + 54)))
    drawblack.text((time_text_x, (y_two + 1)), '2pm', font = font_time_slot, fill = 0)
    # 3pm Line
    y_three = 447
    drawblack.line((0, y_three, 384, y_three), fill = 0)
    # 3pm Ticks & Textblack
    drawblack.line((0, (y_three + 10), normal_tick_x2, (y_three + 10)))
    drawblack.line((0, (y_three + 21), normal_tick_x2, (y_three + 21)))
    drawblack.line((0, (y_three + 32), thirty_tick_x2, (y_three + 32)))
    drawblack.line((0, (y_three + 43), normal_tick_x2, (y_three + 43)))
    drawblack.line((0, (y_three + 54), normal_tick_x2, (y_three + 54)))
    drawblack.text((time_text_x, (y_three + 1)), '3pm', font = font_time_slot, fill = 0)
    # 4pm Line
    y_four = 511
    drawblack.line((0, y_four, 384, y_four), fill = 0)
    # 4pm Ticks & Text
    drawblack.line((0, (y_four + 10), normal_tick_x2, (y_four + 10)))
    drawblack.line((0, (y_four + 21), normal_tick_x2, (y_four + 21)))
    drawblack.line((0, (y_four + 32), thirty_tick_x2, (y_four + 32)))
    drawblack.line((0, (y_four + 43), normal_tick_x2, (y_four + 43)))
    drawblack.line((0, (y_four + 54), normal_tick_x2, (y_four + 54)))
    drawblack.text((time_text_x, (y_four + 1)), '4pm', font = font_time_slot, fill = 0)
    # 5pm Line
    y_five = 575
    drawblack.line((0, y_five, 384, y_five), fill = 0)
    # 5pm Ticks & Text
    drawblack.line((0, (y_five + 10), normal_tick_x2, (y_five + 10)))
    drawblack.line((0, (y_five + 21), normal_tick_x2, (y_five + 21)))
    drawblack.line((0, (y_five + 32), thirty_tick_x2, (y_five + 32)))
    drawblack.line((0, (y_five + 43), normal_tick_x2, (y_five + 43)))
    drawblack.line((0, (y_five + 54), normal_tick_x2, (y_five + 54)))
    drawblack.text((time_text_x, (y_five + 1)), '5pm', font = font_time_slot, fill = 0)
    #6pm Text
    drawblack.text((time_text_x, 623), '6pm', font = font_time_slot, fill = 0)
    
    return (epd, drawblack, drawred, HBlackimage, HRedimage)