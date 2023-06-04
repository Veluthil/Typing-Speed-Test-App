# Typing Speed Test App

This is a simple application that allows you to check your typing speed. It offers two levels of difficulty, both of which consist of a randomly generated sample of 20 words. The easy mode uses a text file of the most common English words, while the hard mode uses the `english_words` library. 

## Getting Started

1. Clone the repository: 
```
git clone https://github.com/Veluthil/Typing-Speed-Test-App.git
```
2. Change directory into the project folder
3. Create virtual environment: 
```
py -m venv venv
venv/Scripts/activate
```
4. Install the required packages: 
```
pip install -r requirements.txt
```
To get started, simply run the `main.py` file. The app will launch and display the starting screen:

![typing_speed](https://user-images.githubusercontent.com/108438343/223138463-7fa322ad-c945-4cff-bdc8-31aa4aabeaff.png)

From here, you can choose your difficulty level and begin the test.

## Features

### Instruction Screen

If you need instructions on how to use the app, you can click the "Instructions" button to display the instruction screen:

![Screenshot 2023-03-05 210719](https://user-images.githubusercontent.com/108438343/223141350-65b4016e-06cc-47bd-8343-008493d99b1f.png)

From here, you can click the "Go Back" button to return to the starting screen.

### Test Screens

Once you start the test, you will be presented with a screen that looks like this:

![Screenshot 2023-03-05 210750](https://user-images.githubusercontent.com/108438343/223142431-baaaf3be-2925-45de-8c40-f5b8fa75c044.png)

The text box at the bottom is where you type your response to the randomly generated text at the top. The app will keep track of your words per minute (WPM), net words per minute (NET WPM), characters per minute (CPM), and accuracy. The score board at the top of the screen will update as you type.

### Checking Spelling

If you make a mistake, the app will show the incorrect character in red and the correct character in white. The app will also add up the number of mistakes you make and show it in the "Mistakes" box. You can use the backspace key to correct your mistakes.

![Screenshot 2023-03-05 210851](https://user-images.githubusercontent.com/108438343/223146945-10e5ff45-29ec-4238-a439-af5c24105fbd.png)

### End of Test

Once you have finished typing the text, the app will display your results in a message box:

![Screenshot 2023-03-05 211310](https://user-images.githubusercontent.com/108438343/223147122-eb7540e2-5d35-4c8a-914a-74b7b671fa62.png)

The app will also save your highest NET WPM score in the `data.txt` file.

## Requirements

This app requires Python 3 and the following Python packages:

- tkinter
- english_words

You can install these packages by running the following command:

```
pip install -r requirements.txt
```
