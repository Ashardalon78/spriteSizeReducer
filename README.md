DESCRIPTION
------------------
Tool to automatically and recursively crop images to their minimum size, i.e. cutting the "white border" of the images.
Useful for sprite-cropping for 2d-game development.
ATTENTION: this tool overwirtes the original image files, it's reccomendable to create a copy of the original images' folder before using this script.


REQUIREMENTS
------------------

* Python 3.7
* Pygame 1.9.6


USAGE
-------------------
* Enter the RGB-values of the image background in the three corrseponding text fileds (This is most commonly 255,255,255 or 0,0,0).
* Press "Start" and select the folder where yor images are located.
* All .png files in the folder and all subfolders will be cropped to their minimum size.
* ATTENTION: images files will be overwritten. It's reccomendable to create a copy of the original images' folder before using this script.

LEGAL
--------------------
<a href=http://www.pygame.org>Pygame</a> is licensed under the <a href=http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>LGPLv2.1</a>.
