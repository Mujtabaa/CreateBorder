import os
import random
#Pillow library
from PIL import Image, ImageDraw

random.seed

print("Directory for pictures to loop: ")
directory = input()
print("\nWhat type of pics for your input?\n1 - jpg\n2 - png\n3 - both\n")
pin = input()
print("\nWhat type of pics for your output?\n1 - jpg\n2 - png\n3 - same\n")
pout = input()
print("\nWhere do I save the new pics at? ")
directoryOut = input()

if pin == '3':
#Looping through different directory with pics
#for f in os.listdir(('M:\TEMP PICS\Batch 3\PNG')):
    for f in os.listdir((directory)):
        if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png'):
            print (f)

            #fn contains filename, fext contains file extension
            fn, fext = os.path.splitext(f)

            Red = random.randint(0,254)
            Green = random.randint(0,254)
            Blue = random.randint(0,254)

            #Opening the current picture, editing, and saving to a folder
            with Image.open(directory + '/' + str(f)) as im:

                draw = ImageDraw.Draw(im)
                draw.line((0,0, im.size[0], 0),width=(im.size[0]//50), fill=(Red,Green,Blue,128) )
                draw.line((im.size[0],0, im.size[0], im.size[1]),width=(im.size[0]//50), fill=(Red,Green,Blue,128) )
                draw.line((im.size[0], im.size[1], 0, im.size[1]),width=(im.size[0]//50), fill=(Red,Green,Blue,128))
                draw.line((0, im.size[1], 0, 0),width=(im.size[0]//50), fill=(Red,Green,Blue,128))

                print("size1: " + str(im.size[0]) + " size2:" + str(im.size[1]) + " Total size: " + str(im.size))
                match pout:
                    case '1':
                        im.save(directoryOut + '/{}_Bordered.jpg'.format(fn)) 
                    case '2':
                        im.save(directoryOut + '/{}_Bordered.png'.format(fn)) 
                    case '3':
                        im.save(directoryOut + '/{}_Bordered'.format(fn) + '{}'.format(fext)) 
elif pin == '1':
#Looping through different directory with pics
#for f in os.listdir(('M:\TEMP PICS\Batch 3\PNG')):
    for f in os.listdir((directory)):
        if f.endswith('.jpg') or f.endswith('.jpeg'):
            print (f)

            #fn contains filename, fext contains file extension
            fn, fext = os.path.splitext(f)

            Red = random.randint(0,254)
            Green = random.randint(0,254)
            Blue = random.randint(0,254)

            #Opening the current picture, editing, and saving to a folder
            with Image.open(directory + '/' + str(f)) as im:

                draw = ImageDraw.Draw(im)
                draw.line((0,0, im.size[0], 0),width=(im.size[0]//50), fill=(Red,Green,Blue) )
                draw.line((im.size[0],0, im.size[0], im.size[1]),width=(im.size[0]//50), fill=(Red,Green,Blue) )
                draw.line((im.size[0], im.size[1], 0, im.size[1]),width=(im.size[0]//50), fill=(Red,Green,Blue))
                draw.line((0, im.size[1], 0, 0),width=(im.size[0]//50), fill=(Red,Green,Blue))

                print("size1: " + str(im.size[0]) + " size2:" + str(im.size[1]) + " Total size: " + str(im.size))
                match pout:
                    case '1':
                        im.save(directoryOut + '/{}_Bordered.jpg'.format(fn)) 
                    case '2':
                        im.save(directoryOut + '/{}_Bordered.png'.format(fn)) 
                    case '3':
                        im.save(directoryOut + '/{}_Bordered'.format(fn) + '{}'.format(fext))
elif pin == '2':
#Looping through different directory with pics
#for f in os.listdir(('M:\TEMP PICS\Batch 3\PNG')):
    for f in os.listdir((directory)):
        if f.endswith('.png'):
            print (f)

            #fn contains filename, fext contains file extension
            fn, fext = os.path.splitext(f)

            Red = random.randint(0,254)
            Green = random.randint(0,254)
            Blue = random.randint(0,254)

            #Opening the current picture, editing, and saving to a folder
            with Image.open(directory + '/' + str(f)) as im:

                draw = ImageDraw.Draw(im)
                draw.line((0,0, im.size[0], 0),width=(im.size[0]//50), fill=(Red,Green,Blue,128) )
                draw.line((im.size[0],0, im.size[0], im.size[1]),width=(im.size[0]//50), fill=(Red,Green,Blue,128) )
                draw.line((im.size[0], im.size[1], 0, im.size[1]),width=(im.size[0]//50), fill=(Red,Green,Blue,128))
                draw.line((0, im.size[1], 0, 0),width=(im.size[0]//50), fill=(Red,Green,Blue,128))

                print("size1: " + str(im.size[0]) + " size2:" + str(im.size[1]) + " Total size: " + str(im.size))
                match pout:
                    case '1':
                        im.save(directoryOut + '/{}_Bordered.jpg'.format(fn)) 
                    case '2':
                        im.save(directoryOut + '/{}_Bordered.png'.format(fn)) 
                    case '3':
                        im.save(directoryOut + '/{}_Bordered'.format(fn) + '{}'.format(fext)) 
else: print ('\nI have messed up somewhere...')