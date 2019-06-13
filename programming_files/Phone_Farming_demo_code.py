#Phone Farm(ing) demo code
import re
import subprocess
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 37

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=10, auto_write=False, pixel_order=ORDER)

#define different colors
one_blue = (30,0,255)
two_blue = (10, 80, 220)
three_blue = (0, 160, 160)
green_blue = (0, 180, 80)
one_green = (0, 220, 60)
two_green = (0, 255, 20)


device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)

def CountDevices():
    df = subprocess.check_output("lsusb")
    devices = []
    for i in df.split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)
    #print (devices.count(1))

#change here to the count of devcies when only your empty USB hub is connected
    return len(devices) -4

def LEDcontrol():
    if CountDevices() == 0:
        #1stlevel
        pixels[13] = one_blue
        pixels[14] = one_blue
    elif CountDevices() == 1:
        #1stlevel
        pixels[13] = one_blue
        pixels[14] = one_blue
        #2ndlevel
        pixels[15] = two_blue
        pixels[24] = two_blue
    elif CountDevices() == 2:
        #1stlevel
        pixels[13] = one_blue
        pixels[14] = one_blue
        #2ndlevel
        pixels[15] = two_blue
        pixels[24] = two_blue
        #3rdlevel
        pixels[5] = three_blue
        pixels[12] = three_blue
        pixels[16] = three_blue
        pixels[23] = three_blue
        pixels[25] = three_blue
        pixels[32] = three_blue
        pixels[33] = three_blue
    elif CountDevices() == 3:
        #1stlevel
        pixels[13] = one_blue
        pixels[14] = one_blue
        #2ndlevel
        pixels[15] = two_blue
        pixels[24] = two_blue
        #3rdlevel
        pixels[5] = three_blue
        pixels[12] = three_blue
        pixels[16] = three_blue
        pixels[23] = three_blue
        pixels[25] = three_blue
        pixels[32] = three_blue
        pixels[33] = three_blue
        #4thlevel
        pixels[0] = green_blue
        pixels[4] = green_blue
        pixels[6] = green_blue
        pixels[11] = green_blue
        pixels[17] = green_blue
        pixels[22] = green_blue
        pixels[26] = green_blue
        pixels[31] = green_blue
        pixels[34] = green_blue
        pixels[36] = green_blue
    elif CountDevices() == 4:
        #1stlevel
        pixels[13] = one_blue
        pixels[14] = one_blue
        #2ndlevel
        pixels[15] = two_blue
        pixels[24] = two_blue
        #3rdlevel
        pixels[5] = three_blue
        pixels[12] = three_blue
        pixels[16] = three_blue
        pixels[23] = three_blue
        pixels[25] = three_blue
        pixels[32] = three_blue
        pixels[33] = three_blue
        #4thlevel
        pixels[0] = green_blue
        pixels[4] = green_blue
        pixels[6] = green_blue
        pixels[11] = green_blue
        pixels[17] = green_blue
        pixels[22] = green_blue
        pixels[26] = green_blue
        pixels[31] = green_blue
        pixels[34] = green_blue
        pixels[36] = green_blue
        #5thlevel
        pixels[1] = one_green
        pixels[3] = one_green
        pixels[7] = one_green
        pixels[10] = one_green
        pixels[18] = one_green
        pixels[21] = one_green
        pixels[27] = one_green
        pixels[30] = one_green
        pixels[35] = one_green
        #6thlevel
        pixels[2] = two_green
        pixels[8] = two_green
        pixels[9] = two_green
        pixels[19] = two_green
        pixels[20] = two_green
        pixels[28] = two_green
        pixels[29] = two_green

#resetcommand
pixels.show()


while True:
    print (CountDevices())
    LEDcontrol()
    time.sleep(0.1)
