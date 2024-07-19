'''USE THIS TO RUN IN REAL TIME'''

import cv2
from tensorflow import keras
import numpy as np

# using cv2 to read the image
# convert image to BW
# sharpen image
# pass image to model
# get prediction and display in real time
# exit when esc key is pressed


def recognize_digit():

    frame_size = 240
    x, y, w, h = 0, 0, frame_size, frame_size
    model = keras.models.load_model('digits.h5')
    camera = cv2.VideoCapture(0)

    while True:
        return_value, image = camera.read()
        original_image = image

        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)

        image = cv2.resize(image[y:y + h, x:x + w], (28, 28))
        im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        x_pred = im_bw.reshape(28, 28, 1)
        batch = np.array([x_pred])
        output = str(np.argmax(model.predict(batch, verbose=0)))

        cv2.putText(original_image, "GUESSED DIGIT: " + output, (200, 300), cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 0, 255), 2)
        cv2.putText(original_image, "Press \'ESC\' to Quit", (200, 350), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 255, 0), 1)
        cv2.imshow('image', original_image)

        if cv2.waitKey(1) & 0xFF == 27: # index of escape key ~chatgpt
            break

    camera.release()
    cv2.destroyAllWindows()


def main():
    recognize_digit()

if __name__ == '__main__':
    main()