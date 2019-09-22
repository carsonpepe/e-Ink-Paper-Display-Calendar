#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd7in5b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from time import gmtime, strftime
from utilCalc import *
import quickstart
import operator
from newDayRefresh import *
import os

#Xm = am_or_pm(t[11:13])

#hour = hourFix(t[11:13])
#minute = minuteFix(t[14:16])


#curTime = hour + ':' + minute + ' ' + Xm

#refresh_rate = 900 # Seconds

meetings_x = 74
def main():
    try:
        epd = epd7in5b.EPD()
        epd.init()
        #print("Clear...")
        epd.Clear(0xFF)
        print("Done Clearing")
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
        update_check = []
        date_reg = ''
        date_x_reg = 0
        refresh = True
        startup = True
        loop = True # should always be true
        while loop:
            t = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            print(t)
            month, date_x = monthName(int(t[5:7]))
            day = dayFix(t[8:10], t[11:13])
            date = month + ' ' + day + ', ' + t[0:4]
            if date != date_reg and date_reg != '':
                epd, drawblack, drawred, HBlackimage, HRedimage = new_day_redraw()
                # Draws back over old date in white to make it disappear
                drawred.text((date_x_reg, 32), date_reg, font = font_title, fill = 255)
            drawred.text((date_x, 32), date, font = font_title, fill = 0)  #Date
            date_reg = date
            date_x_reg = date_x
            ## CALENDAR DATA PROCESSING ###
            events_temp = quickstart.main()
            events_official_start = {} # Final dict to store event data --> key: meeting name, value: time
            events_official_end = {}
            for event_tup in events_temp:
                if int(event_tup[1][8:10]) == int(day):
                    start_time = event_tup[1][11:16]
                    end_time = event_tup[2][11:16]
                    # Makes time into an int without ':' as the value corresponding to its key
                    # for sorting purposes. Leading zero's are eliminated as well.
                    events_official_start[event_tup[0]] = int(start_time.replace(':', ''))
                    events_official_end[event_tup[0]] = int(end_time.replace(':', ''))
            # events_sorted will be a list of tuples sorted by second element in each tuple (time)
            events_sorted_start = sorted(events_official_start.items(), key=operator.itemgetter(1))
            events_sorted_end = sorted(events_official_end.items(), key=operator.itemgetter(1))
        
            meetings = [] # List of meetings in order
            start_times = [] # List of times corresponding to their associated meetings in order
            for tup in events_sorted_start:
                meetings.append(tup[0])
                time_str = str(tup[1])
                start_time = time_str[0:2] + ':' + time_str[2:] # Assumes current hour is before 10am
                hour = int(time_str[0:2])
                if len(time_str) == 3: # Fixes current time variable if its 10am or after
                    start_time = time_str[0] + ':' + time_str[1:]
                    hour = int(time_str[0])
                xm = 'am' # Assumes its before 12pm due to military time
                if hour > 11:
                    xm = 'pm' # Catches if its 12pm or later
                    if hour > 12: # Checks to see if convert from military to normal time is needed
                        hr = hour - 12
                        start_time = str(hr) + ':' + time_str[2:]
                start_times.append(start_time + ' ' + xm)
            end_times = []
            for tup in events_sorted_end:
                time_str = str(tup[1])
                end_time = time_str[0:2] + ':' + time_str[2:]
                hour = int(time_str[0:2])
                if len(time_str) == 3:
                    end_time = time_str[0] + ':' + time_str[1:]
                    hour = int(time_str[0])
                xm = 'am'
                if hour > 11:
                    xm = 'pm'
                    if hour > 12:
                        hr = hour - 12
                        end_time = str(hr) + ':' + time_str[2:]
                end_times.append(end_time + ' ' + xm)

            print(start_times)
            print(end_times)
            print(meetings)
            print("Meetings length: " + str(len(meetings)))
            print("UpdateCheck length: " + str(len(update_check)))
            if len(meetings) == len(update_check):
                for i in range(len(meetings)):
                    if meetings[i] != update_check[i]:
                        refresh = True
                        break
                    refresh = False
            else:
                refresh = True
            
            if refresh:
                for i in range(len(start_times)):
                    t1 = start_times[i]
                    t2 = end_times[i]
                    if t1[1] == ':':
                        h1 = int(t1[0])
                        m1 = int(t1[2:4])
                        start_time_y = time_y_coord(h1, m1)
                    else:
                        h1 = int(t1[0:2])
                        m1 = int(t1[3:5])
                        start_time_y = time_y_coord(h1, m1)
                    if t2[1] == ':':
                        h2 = int(t2[0])
                        m2 = int(t2[2:4])
                        end_time_y = time_y_coord(h2, m2)
                    else:
                        h2 = int(t2[0:2])
                        m2 = int(t2[3:5])
                        end_time_y = time_y_coord(h2, m2)
                    meeting_y = ((start_time_y + end_time_y)//2) - 7
            
                    erase_y = None
                    if h1 != 12:
                        if (h2 - h1) == 1:
                            er_y = {
                                10: 128,
                                11: 192,
                                12: 256,
                                1: 319,
                                2: 383,
                                3: 447,
                                4: 511,
                                5: 575
                                }
                            erase_y = er_y.get(h2, None)
                        elif (h2 - h1) == 2:
                            er_y = {
                                10: 128,
                                11: 128,
                                12: 192,
                                1: 256,
                                2: 319,
                                3: 383,
                                4: 447,
                                5: 511,
                                6: 575
                                }
                            erase_y = er_y.get(h2, None)
                        if erase_y is not None:
                            drawblack.line((50, erase_y, 381, erase_y), fill = 255)
                    else:
                        if h2 == 1:
                            drawblack.line((50, y_one, 381, y_one), fill = 255)
                        elif h2 == 2:
                            drawblack.line((50, y_two, 381, y_two), fill = 255)
        
                    ### Start Time Lines ###
                    # 9am
                    if start_time_y < 81 and start_time_y > 64:
                        drawred.line((1, start_time_y, 9, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 9, start_time_y + 1), fill = 0)
                        drawred.line((41, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((41, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 10am
                    elif start_time_y < 145 and start_time_y > 128:
                        drawred.line((1, start_time_y, 10, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 10, start_time_y + 1), fill = 0)
                        drawred.line((50, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((50, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 11am
                    elif start_time_y < 209 and start_time_y > 192:
                        drawred.line((1, start_time_y, 10, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 10, start_time_y + 1), fill = 0)
                        drawred.line((50, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((50, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 12pm
                    elif start_time_y < 275 and start_time_y > 256:
                        drawred.line((1, start_time_y, 10, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 10, start_time_y + 1), fill = 0)
                        drawred.line((50, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((50, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 1pm
                    elif start_time_y < 338 and start_time_y > 319:
                        drawred.line((1, start_time_y, 10, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 10, start_time_y + 1), fill = 0)
                        drawred.line((41, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((41, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 2pm
                    elif start_time_y < 402 and start_time_y > 383:
                        drawred.line((1, start_time_y, 9, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 9, start_time_y + 1), fill = 0)
                        drawred.line((41, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((41, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 3pm
                    elif start_time_y < 466 and start_time_y > 447:
                        drawred.line((1, start_time_y, 9, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 9, start_time_y + 1), fill = 0)
                        drawred.line((41, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((41, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 4pm
                    elif start_time_y < 530 and start_time_y > 511:
                        drawred.line((1, start_time_y, 8, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 8, start_time_y + 1), fill = 0)
                        drawred.line((41, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((41, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 5pm
                    elif start_time_y < 594 and start_time_y > 575:
                        drawred.line((1, start_time_y, 9, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 9, start_time_y + 1), fill = 0)
                        drawred.line((41, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((41, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    # 6pm
                    elif start_time_y > 624:
                        drawred.line((1, start_time_y, 9, start_time_y), fill = 0)
                        drawred.line((1, start_time_y + 1, 9, start_time_y + 1), fill = 0)
                        drawred.line((41, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((41, start_time_y + 1, 382, start_time_y + 1), fill = 0)
                    else:
                        drawred.line((1, start_time_y, 382, start_time_y), fill = 0)
                        drawred.line((1, (start_time_y + 1), 382, (start_time_y + 1)), fill = 0)
            
                    ### End Time Lines ###
                    # 9am
                    if end_time_y < 81 and end_time_y > 64:
                        drawred.line((1, end_time_y, 9, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 9, end_time_y - 1), fill = 0)
                        drawred.line((41, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((41, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 10am
                    elif end_time_y < 145 and end_time_y > 128:
                        drawred.line((1, end_time_y, 10, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 10, end_time_y - 1), fill = 0)
                        drawred.line((50, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((50, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 11am
                    elif end_time_y < 209 and end_time_y > 192:
                        drawred.line((1, end_time_y, 10, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 10, end_time_y - 1), fill = 0)
                        drawred.line((50, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((50, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 12pm
                    elif end_time_y < 275 and end_time_y > 256:
                        drawred.line((1, end_time_y, 10, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 10, end_time_y - 1), fill = 0)
                        drawred.line((50, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((50, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 1pm
                    elif end_time_y < 338 and end_time_y > 319:
                        drawred.line((1, end_time_y, 10, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 10, end_time_y - 1), fill = 0)
                        drawred.line((41, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((41, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 2pm
                    elif end_time_y < 402 and end_time_y > 383:
                        drawred.line((1, end_time_y, 9, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 9, end_time_y - 1), fill = 0)
                        drawred.line((41, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((41, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 3pm
                    elif end_time_y < 466 and end_time_y > 447:
                        drawred.line((1, end_time_y, 9, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 9, end_time_y - 1), fill = 0)
                        drawred.line((41, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((41, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 4pm
                    elif end_time_y < 530 and end_time_y > 511:
                        drawred.line((1, end_time_y, 8, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 8, end_time_y - 1), fill = 0)
                        drawred.line((41, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((41, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 5pm
                    elif end_time_y < 594 and end_time_y > 575:
                        drawred.line((1, end_time_y, 9, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 9, end_time_y - 1), fill = 0)
                        drawred.line((41, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((41, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    # 6pm
                    elif end_time_y > 624:
                        drawred.line((1, end_time_y, 9, end_time_y), fill = 0)
                        drawred.line((1, end_time_y - 1, 9, end_time_y - 1), fill = 0)
                        drawred.line((41, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((41, end_time_y - 1, 382, end_time_y - 1), fill = 0)
                    else:
                        drawred.line((1, end_time_y, 382, end_time_y), fill = 0)
                        drawred.line((1, (end_time_y - 1), 382, (end_time_y - 1)), fill = 0)
            
                    # Left and right side borders for meetings
                    drawred.line((0, start_time_y, 0, end_time_y), fill = 0)
                    drawred.line((1, start_time_y, 1, end_time_y), fill = 0)
                    drawred.line((2, start_time_y, 2, end_time_y), fill = 0)
                    drawred.line((383, start_time_y, 383, end_time_y), fill = 0)
                    drawred.line((382, start_time_y, 382, end_time_y), fill = 0)
                    drawred.line((381, start_time_y, 381, end_time_y), fill = 0)
            
                    if len(meetings[i]) <= 33:
                        if h1 > 9 or h2 > 9:
                            drawred.text((302, meeting_y), t1[:-3] + '-' + t2[:-3],
                                         font = font_time_small, fill = 0)
                        else:   
                            drawred.text((315, meeting_y), t1[:-3] + '-' + t2[:-3],
                                         font = font_time_small, fill = 0)
                            # Meeting Titles
                    drawred.text((55, meeting_y), meetings[i], font = font_time_slot, fill = 0)

                update_check = meetings
                epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))

                startup = False


            else:
                time.sleep(30)
            
            if startup:
                epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
                startup = False
            
    except Exception as e:
        print('exception ' + str(e))
        main()

if __name__ == "__main__":
    main()