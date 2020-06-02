from PIL import Image

"""
inspired from:
https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/index.html

"""

class AsciiImage():

    def __init__(self, img_file):
        self.img_file = img_file
        self.img = Image.open(img_file)
        self.img_width, self.img_height = self.img.size
        self.img_dat = self.img.getdata()
        self.ascii_string = list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")

    def refactor_pixels(self) -> list:
        pixel_arr = [[] for x in range(self.img_height)]

        for i, x in enumerate(self.img_dat):
            pixel_arr[i // self.img_width].append(x)

        return pixel_arr

    def to_brightness(self, pixel_arr) -> list:
        bright_arr = [[] for x in range(self.img_height)]

        for i, x in enumerate(pixel_arr):
            for y in x:
                bright_arr[i].append(sum(y)/3)

        return bright_arr

    def to_ascii(self, bright_arr) -> list:
        ascii_arr = [[] for x in range(self.img_height)]

        for i, x in enumerate(bright_arr):
            for y in x:
                ascii_arr[i].append(self.ascii_string[int(y/3.92)]*2)

        return ascii_arr

    def print_ascii(self, ascii_arr) -> None:
        for x in ascii_arr:
            print(''.join(x))

        return None


def main():
    my_img = AsciiImage("pineapple.jpg")
    my_pixels = my_img.refactor_pixels()
    my_brightness = my_img.to_brightness(my_pixels)
    my_ascii = my_img.to_ascii(my_brightness)
    my_img.print_ascii(my_ascii)

if __name__ == '__main__':
    main()




