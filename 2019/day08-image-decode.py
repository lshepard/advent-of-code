

def decode_image(x, y, image_data):

    lst = list(image_data.strip())
    chunk_size = x * y
    layers = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

    return layers

def num_int_on_layer(layer, desired_int):
    return len([x for x in layer if int(x) == int(desired_int)])
    
def part1(x, y, image_data):
    layers = decode_image(x, y, image_data)

    ll = min(layers, key=lambda l: num_int_on_layer(l, 0))
    return  num_int_on_layer(ll, 1) * num_int_on_layer(ll, 2)

def part2(x, y, image_data):
    layers = decode_image(x, y, image_data)

    im = []
    
    for i in range(0,len(layers[0])):
        vals = [layer[i] for layer in layers]
        im.append(pixelval(vals))

    return "\n".join(["".join(im[i:i+x]) for i in range(0,len(im),x)])
        
def pixelval(vals):
    for val in vals:
        if int(val) == 0:
            return "."
        if int(val) == 1:
            return "@"
        if int(val) < 2:
            return val
    return 3

#print(decode_image(3,2,"123456789012"))# == ["123456","789012"])

inpt = open("day8.input").read()
#print(part1(25,6,inpt))
print(part2(25,6,inpt))
