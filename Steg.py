from PIL import Image

def generate_data(data):
    new_data = []

    for i in data:
        new_data.append(format(ord(i), '08b'))
    return new_data


# convert each byte into its 8 bit binary code, read pixels right to left in
# read each pixel from right to left in groups of 3, having 9 total values
# first 8 values store binary data, and is made odd if 1 occurs or even if 0 occurs

def modify_pixel(pixel, data):
    list = generate_data(data)
    data_len = len(list)
    image_data = iter(pixel)

    for i in range(data_len):
        #get set of 3 pixels

        pixel = [value for value in image_data.__next__()[:3] +
                                    image_data.__next__()[:3] +
                                    image_data.__next__()[:3]]

        # Set odd value for 1 and even value for 0
        for j in range(0,8):
            if (list[i][j] == '0' and pixel[j] % 2 != 0):
                pixel[j] -= 1
            
            elif (list[i][j] == '1' and pixel[j] % 2 == 0):
                if(pixel[j] != 0):
                    pixel[j] -= 1
                else:
                    pixel[j] += 1

        #eighth pixel tells us to stop or continue
        # let 0 denote to contiue, 1 to stop
        if (i == data_len - 1):
            if (pixel[-1] % 2 == 0):
                if(pixel[-1] != 0):
                    pixel[-1] -= 1
                else:
                    pixel[-1] += 1
        else:
            if (pixel[-1] % 2 != 0):
                pixel[-1] -= 1
        
        pixel = tuple(pixel)

        #throw the pixels back to the caller
        yield pixel[0:3]
        yield pixel[3:6]
        yield pixel[6:9]

def encode_helper(new_image, data):
    width = new_image.size[0]
    (x, y) = (0,0)

    for pixel in modify_pixel(new_image.getdata(), data):

        new_image.putpixel((x,y), pixel)
        if (x == width - 1):
            x = 0
            y += 1
        else:
            x += 1

def encode(image_file):
    image = Image.open(image_file, 'r')

    data = ("testing Encoding")
    if (len(data) == 0):
        raise ValueError('No Data Present')

    new_image = image.copy()
    encode_helper(new_image, data)
    new_image_name = "EncodedImage.png"
    new_image.save(new_image_name, str(new_image_name.split(".")[1].upper()))


encode("WSU.png")