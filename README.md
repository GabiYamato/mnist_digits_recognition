---

# Handwritten Digit Recognition

Hey there! 👋

Welcome to my Handwritten Digit Recognition project! This is a cool little project where we use deep learning to recognize digits from the MNIST dataset. You can use this to guess numbers from images in real-time using your webcam. 😎

## 📦 What’s Included

1. **`TRAIN.py`**: This script trains a Convolutional Neural Network (CNN) on the MNIST dataset. It saves the trained model as `digits.h5`.

2. **`MAIN.py`**: This script uses the trained model to recognize digits from your webcam in real-time. It shows the predicted digit on your webcam feed.

## 🚀 How to Use

### 1. Train the Model

First, you need to train the model. Run this script:

```bash
python TRAIN.py
```

This will train the model and save it as `digits.h5`.

### 2. Real-Time Digit Recognition

After training, you can use the webcam to recognize digits. Run this script:

```bash
python MAIN.py
```

It’ll start your webcam and guess the digits you draw in the frame. Just press `ESC` to quit.

## ⚙️ Requirements

You’ll need Python and these libraries:
- TensorFlow
- Keras
- OpenCV
- NumPy

You can install them with pip:

```bash
pip install tensorflow keras opencv-python numpy
```

## 📝 Notes

- Make sure your webcam is working.
- The script resizes the image to 28x28 pixels and converts it to grayscale.
- The model is pretty basic, but it should work for simple digits.

## 📂 License

Feel free to use and modify this code as you like. Just give credit if you use it somewhere!

## 👋 Contact

If you have any questions, you can reach me at:

- Email: bismuthlover1404@gmail.com
- Instagram: [@notyuritomboy](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi-sMnA6LKHAxXpyzgGHbgYEk8QFnoECBEQAQ&url=https%3A%2F%2Fwww.instagram.com%2Fnotyuritomboy%2F&usg=AOvVaw0aRanhocsBdP6WrToIgsnm&opi=89978449)
- X: [@gabrielcantsimp](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi-sMnA6LKHAxXpyzgGHbgYEk8QFnoECBEQAQ&url=https%3A%2F%2Fwww.instagram.com%2Fnotyuritomboy%2F&usg=AOvVaw0aRanhocsBdP6WrToIgsnm&opi=89978449)


Enjoy! 🚀

---

Feel free to tweak it if needed!
