import cProfile

import re
import sys
import tqdm
import cv2
import numpy as np
from collections import Counter
from PIL import Image, ImageDraw

def points(inpt):
    r = re.compile(r"position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>")
    return [ tuple([int(x) for x in r.match(p).groups()]) for p in inpt]

def find_next_interesting_version(points):
    """The visual search isn't working -- lets look for shapes like a solid line"""
    
    for i in range(1000):
        (x, y, vx, vy) = zip(*points)
        cx = Counter(x)
        cxmax = max(cx,key=cx.get)

        cy = Counter(y)
        cymax = max(cy,key=cy.get)
    
        if cxmax > 10 or cymax > 10:
            return points

        points = next_version(points)

    #stop at some point
    return points

def next_version(points, scale=1):
    return [(px+vx*scale,py+vy*scale,vx,vy) for (px,py,vx,vy) in points]

def create_image(points, width, height):
    (x, y, vx, vy) = zip(*points)
    xscale = width*1.0 / (max(x) - min(x) + 1)
    xoffset = min(x)
    
    yscale = height*1.0 / (max(y) - min(y) + 1)
    yoffset = min(y)
    
    image = Image.new(mode='L', size=(width, height), color=255)
    draw = ImageDraw.Draw(image)
    for (x,y,xv,yv) in points:
        x0 = int((x-xoffset) * xscale)
        y0 = int((y-yoffset) * yscale)
        draw.rectangle([x0, y0, x0 + 6, y0 + 40], fill="black")
        
    return image
    
def create_mov(points, nframes, vscale=1, width=500, height=500):
    images = []
    print("Creating images...")
    for i in tqdm.tqdm(range(nframes)):
        images.append(create_image(points, width, height))
        points = next_version(points)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
    out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (width, height))

    print("Creating movie...")
    for image in tqdm.tqdm(images):
        frame = np.array(image.convert('RGB')) # i think it's an array
        out.write(frame) # Write out frame to video
        cv2.imshow('video',frame)

    out.release()
    
        
#    images[0].save('anitest.gif',
#               save_all=True,
#               append_images=images[1:],
#               duration=100,
#               loop=0)

def emit_bounding_area_chart(points):
    for i in tqdm.tqdm(range(50000)):
        (x, y, vx, vy) = zip(*points)
        width = max(y) - min(y)
        height = max(x) - min(x)
        area = width * height
        
        if area < 10000:
            create_mov(points, 200)
            print("created movie")
            exit()
            
        points = next_version(points)

if __name__ == "__main__":
    inpt = sys.stdin.readlines()
    print(emit_bounding_area_chart(points(inpt)))
#    print(cProfile.run("create_mov(points(inpt),500)"))
    print("Done!")
