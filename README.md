# **Tunic Rune Reader**
The goal of this project is to create an application (or script or whatever) which can recognize letters and words from screenshots of text in the game **Tunic**.


# Main Steps (partially courtesy of ChatGPT)

## 1. Dataset Preparation
Since the language has a finite set of symbols, you can generate synthetic data with variations to make the model robust:  
1. Use both single- and multi-character words in the same samples, to properly synthesize the language.
2. Different colors for the text and background (black on white, white on black, black on grey, etc.)
3. Low resolution and blur effects
4. Background noise (inconsistent patterns or colour behind different parts of the text) (mabe less important than the other two steps)


## 2. Choosing a character- or object recognition Model
The main competing options for category of model were:  
* YOLO (or Object Detection)  
  * Good if the characters are clearly distinct and don’t form continuous words.
  * Detects each character as a separate object and then runs classification.
  * Could struggle if characters are too close together.
* **CRNN (Convolutional Recurrent Neural Network) (WINNER)**
  * More suited for sequential text recognition.
  * Uses CNNs to extract visual features, and an RNN to handle character sequences.
  * More tolerant to minor distortions and blending effects.
  * A good balance between flexibility and accuracy.
* Transformer-Based OCR (TrOCR, ViT-based Models)
  * Uses a vision transformer for feature extraction.
  * Can handle complex shapes and distortions well.
  * Might be overkill for a small dataset but is state-of-the-art.
* Tesseract with Custom Training
  * Requires training with synthetic fonts.
  * Works well if the text is well-separated but struggles with merged characters.


## 3. Training the Model

## 4. Post-Processing



blabla

