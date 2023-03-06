# Typing-Speed-Test-App
This application allows you to check your typing speed.

Starting Screen:
-----
![typing_speed](https://user-images.githubusercontent.com/108438343/223138463-7fa322ad-c945-4cff-bdc8-31aa4aabeaff.png)

The app allows one to choose from two difficulties - both consist of a randomly generated sample of 20 words. 
- The easy mode picks from a text file of the common English words that contains 3000 examples.
- The hard mode uses the english_words library (stated in the requirements.txt)
- The instruction button changes the Screen's contents into a Label Widget with instructions to the app.

Instruction's Screen
-----
![Screenshot 2023-03-05 210719](https://user-images.githubusercontent.com/108438343/223141350-65b4016e-06cc-47bd-8343-008493d99b1f.png)
- The "GO BACK" button changes the Screen's contents back to the Starting Window.

Easy Mode Example and App's Layout
-----
![Screenshot 2023-03-05 210750](https://user-images.githubusercontent.com/108438343/223142431-baaaf3be-2925-45de-8c40-f5b8fa75c044.png)
- The "RESTART" button destroys all the contents, resets the timer and all the scores, then creates Starting Screen again.
- The "WRITE BELOW" Label indicates the Entry Widget where one should provide the input.

Checking Spelling and App's functionality
-----
![Screenshot 2023-03-05 210817](https://user-images.githubusercontent.com/108438343/223142730-1956cd18-86e8-4534-8ccb-c9c92a2290bf.png)
- When the first character gets typed, the timer starts. 
- The timer starts from 0 and adds seconds until the whole text gets rewritten.
- With each written character in the Entry Widget, the correctly typed letters change their color in the Text Widget into a shade of green.
- This Application counts Words Per Minute (WPM), Net Words Per Minute (NET WPM), Characters Per Minute (CPM), and Accuracy 
(not shown until the end of the test) with each change in the Entry Widget, and updates the current score of each of them 
on the Score Board visible at the top.

![Screenshot 2023-03-05 210851](https://user-images.githubusercontent.com/108438343/223146945-10e5ff45-29ec-4238-a439-af5c24105fbd.png)
- If one types a mistake, the wrong character swaps places with a correct white letter in the Text Widget and becomes red.
- Additionally, the mistake widget adds up each typo and changes its color into red.
- One can use backspace to correct any misspells, then the written letters swap to the correct ones and become white again.


Hard Mode Example
-----
![Screenshot 2023-03-05 211016](https://user-images.githubusercontent.com/108438343/223147027-ce296526-9038-4088-80ad-d7ecaee9780c.png)


End of the Test
-----
![Screenshot 2023-03-05 211310](https://user-images.githubusercontent.com/108438343/223147122-eb7540e2-5d35-4c8a-914a-74b7b671fa62.png)
- Once the whole text gets rewritten, the timer stops, and the user's results appear in the message box. 
- The app calculates Words Per Minute (WPM), Net Words Per Minute (NET WPM), Characters Per Minute (CPM), and Accuracy.
- The highest net WPN is automatically saved and stored in the data.txt file.

