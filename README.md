# Linux Debian Package Auto Installer

Demo Video: https://youtu.be/Bqkv0SUi5TE

Python script that generates a bash shell script file to automatically install a user-selected set of programs on Debian Linux Distros. Similar to the Ninite program installer for Windows operating systems, but in the format of a simple bash script. 

**Compatibility:** Ubuntu, MX Linux, Kali Linux, Deepin OS and other Debian-based distros.
    - Tested on Ubuntu 20.04.03 LTS
    - Uses snap packages to simplify installation.

**Instructions:** (Also available as a video in this repository):
    
1. Clone this repository and ensure that 'main.py' and 'main.sh' are downloaded. Ensure that 'main.sh'
and 'main.py' are in the same folder. Additionally, ensure that your computer has an Internet connection and
adequate storage to install programs.

2. Replace the file path for 'main.sh' in the 'main.py' python script. The line to be replaced will initially resemble something similar to the snippet below: 

        with open('YOUR-FILE-DIRECTORY-HERE', 'w') as sh:

You can find the file path for 'main.sh' by using Ctrl + I or double clicking on the file,
then selecting 'Properties' and copying the path found in the Properties window. The line should now resemble
something similar to the snippet below:

       with open('/home/sannjay/Documents/VS Code Projects/Project 1/main.sh', 'w') as sh:
       
After this, save both files.

3. Open a terminal window and redirect the terminal path to the folder with both 'main.py' and 'main.sh'. 

4. Then, run the Python script in the terminal using the following command:

       python3 main.py

After this, the program will prompt you for the programs you want to install. An example would be:

        Select your Web Browsers
        ------------------------
        
        1) Google Chrome
        2) Microsoft Edge
        3) Mozilla Firefox
        4) Opera
        
User input:

        1 2
        
This indicates that the user has chosen to install Google Chrome and Microsoft Edge. Any invalid value inputed
(e.g inputing 5 when you only have 4 choices, non-integer values, etc) will be ignored by the program.

5. After choosing which programs are to be installed, type the following into your terminal.

       chmod +x main.sh

This gives the shell script permission to download programs.

6. Install all your programs by running the shell script.

       ./main.sh
       
The program might prompt you for your user password. After entering your password, main.sh will install
your programs of choice.


**Programs supported:**

   - Web Browsers
        * Google Chrome
        * Microsoft Edge
        * Mozilla Firefox
        * Opera
    
   - Utilities
        * OBS Studio
        * qBittorrent
    
   - Communication Programs
        * Zoom
        * Discord
        * Skype
        * Pidgin
    
   - Production/Editing Programs:
        * Blender
        * Shotcut
        * GIMP
        * Inkscape
        * LMMS
        
   - Developer Tools:
        * FileZilla
        * Notepad++
        * Visual Studio Code
        
   - Media:
        * VLC Media Player
        * foobar2000
        * Audacity
        * Spotify
        * GOM
 
 
**Suggestions/Feedback:**

Any feedback or suggestions, including program choices to include in 'main.py' would be appreciated. 
Email: sannjaykarthikeyan28@gmail.com
