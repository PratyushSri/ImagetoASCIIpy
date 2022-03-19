# ImagetoASCIIpy
I developed a Python Project that takes in an image and creates an Ascii art of it. Art will get printed into a txt file and on a Tkinter canvas (which is a bit buggy), I'm open to suggestions regarding improvements and other challenges. Idea From YouTube coding Challenge- **The Coding Train** " https://youtu.be/55iwMYv8tGI " 

> Use the ipynb file or Directly run the py file using command prompt

## Requirements:
  
 ```bash 
  pip install Pillow
  ```
  ```bash
   pip install Tk
   ```
   ```bash
   pip install opencv-python
  ```
  
## Input:
  - when the program asks for file name, enter  "Image/<Filename>"  add name in place of <filename>
  - Try to Use some of the already added images for quick check.
 
## Output:
  - Open in notepad with font-size: 1 (recommended), zoom in if image looks like it has colors.
  - Tkinter window will also open to show image in red color.
  
## How it works:
  - Using cv2.imread() we can get pixel value of a particular pixel using grayscale we only get one value ranging from 0-255.
  - I then associate those values to similar strenght characters used in the ascii string.
  - which is then converted into a string and then into a file.
  
## To do next:
  - Try to form a better image object instead of using tkinter which might give a distorted image.
  - Any form of improvements including optimizations or anything ( message me )
  
  
## Author

- [@PratyushSri](https://www.github.com/PratyushSri)

 - [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pratyush-srivastava-787a27206)


