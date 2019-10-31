from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def flip(full_path_image, image_filename):

    img = np.array(Image.open(full_path_image))

    flipped_img = np.fliplr(img)

    plt.axis('off')
    plt.imshow(flipped_img)
    plt.savefig("static/augmented/flip-" + image_filename, bbox_inches='tight', pad_inches=0)

    return "static/augmented/flip-" + image_filename

def left_translation(full_path_image, image_filename):

    img = np.array(Image.open(full_path_image))

    HEIGHT = img.shape[1]
    WIDTH = img.shape[0]
    TRANSLATION = 100

    for i in range(HEIGHT, 1, -1):
      for j in range(WIDTH):
         if (i < HEIGHT-TRANSLATION):
           img[j][i] = img[j][i-TRANSLATION]
         elif (i < HEIGHT-1):
           img[j][i] = 0

    plt.axis('off')
    plt.imshow(img)
    plt.savefig("static/augmented/left-translated-" + image_filename, bbox_inches='tight', pad_inches=0)

    return "static/augmented/left-translated-" + image_filename

def right_translation(full_path_image, image_filename):

    img = np.array(Image.open(full_path_image))

    HEIGHT = img.shape[1]
    WIDTH = img.shape[0]
    TRANSLATION = 100

    for j in range(WIDTH):
      for i in range(HEIGHT):
        if (i < HEIGHT-TRANSLATION):
          img[j][i] = img[j][i+TRANSLATION]

    plt.axis('off')
    plt.imshow(img)
    plt.savefig("static/augmented/right-translated-" + image_filename, bbox_inches='tight', pad_inches=0)

    return "static/augmented/right-translated-" + image_filename

def up_translation(full_path_image, image_filename):

    img = np.array(Image.open(full_path_image))

    HEIGHT = img.shape[1]
    WIDTH = img.shape[0]
    TRANSLATION = 100

    for j in range(WIDTH):
      for i in range(HEIGHT):
        if (j < WIDTH - TRANSLATION and j > TRANSLATION):
          img[j][i] = img[j+TRANSLATION][i]
        else:
          img[j][i] = 0

    plt.axis('off')
    plt.imshow(img)
    plt.savefig("static/augmented/up-translated-" + image_filename, bbox_inches='tight', pad_inches=0)

    return "static/augmented/up-translated-" + image_filename
