# YouTubeToAudio
Created by Tony Vo
Date of initial commit: May 16th, 2017

## Short Description
The purpose of this project was to simply download YouTube videos as music files. It has a basic GUI.

# Languages Used
1. Python 3.6

## Libraries and Module's Used
1. [youtube_dl](https://github.com/rg3/youtube-dl)
2. tkinter
3. pyinstaller

## Files Used
1. YouTubeToAudio.py
    This contains a class that is used to implement a basic GUI and download functionality.
   

# Set-up guide:
1. Download the necessary files
2. Run YouTubeToAudio.py
3. Select Browser path and insert URL. Check optional playlist option.
3a. "Ctrl-V" to paste, "Ctrl-C" to copy.
4. Press download.

## Implementation Ideas:
- [ ] Download videos rather than just audio files.
- [ ] Better GUI, maybe try PyQT
- [ ] Try refactoring file information such title, artist, album ect.

# Known Bugs:
- [ ] Breaks when trying to download playlist but video was removed online
- [ ] Not responding on GUI when downloading. (Still downloading in background)

## Notes about project:
My friend was downloading music and had to continously go onto a site and download them one by one. He gave me the idea of implementing a local downloader that accepts a path and a URL that downloads the audio file to that path. The next day, I searched around and discovered youtube_dl which was perfect for this project. I created a simple GUI using tkinter and then turned this file into an executable using pyinstaller.  This application is by no means perfect and infact is very buggy but it functions and I'm glad I created it.

Below are a few of my experiences going through this project.
### Things learned:
* Read the documents
    * tkinter was super well documented and so was youtube_dl which made it easier to learn and embed into my program.
* tkinter GUI
    * I'm no master at GUI's and have never even touched on GUI's before this. It was nice to see my project come to life. Looking at the documentation, examples online and stackoverflow posts really helped me develop this basic application.
* audio formats
   * When I initially downloaded the music, I forced a .mp3 extension onto the files which was naiive of me as not all files were properly encoded. I later changed this format using youtube_dl which allows preference based downloading extensions. It mainly downloads to m4a format. 
* pyinstaller
    * I created an executable for the first time from a program and pyinstaller made it relatively easy to create. Just Awesome. Though it was small, I was super happy and proud.

### Problems encountered:
* Python Version
    * When I was trying convert the program to an executable, I couldn't because pyinstaller only supported python 3.5 or below where as I had python 3.6 installed. This caused me to have to uninstall python 3.6 and downgrade. However after the downgrade, it worked perfectly.
* Class implementation 
    * When designing the GUI, I was deciding whether or not to have a class based approach vs just coding the methods in main. To play around, I tried creating some stuff just on main to see how it would turn out. I then created a Class based GUI implementation and it worked out perfectly. I definately preferred it as to the orignal because it made everything so much neater and organized. 

### Moving foward:
* Continue learning and devloping!


