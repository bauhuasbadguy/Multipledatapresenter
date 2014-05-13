Multipledatapresenter
=====================

Module to present a set of images quickly and easely.

Description
============

This contains a python program designed to put a series of images into a latex document so that they can be easely attached 
to an email and sent as a summary document eg if you need to send the final states of a series of OOMMF simulations to someone
and all the jpegs are in different but logically named folders you can use the program to make a pdf instead of copy pasting
into word.

The program works by producing a .txt document the contents of which need to be copy pasted into a latex/texmaker file and
compiled into a single document. The code works by calling 3 functions:-


*f = openinglines(filename)* :- Takes in the file name for the .txt document and writes the packages to use as well as start the document

*printimage(f, imagepath, figurelabel, width (default 0.5X text width), caption (default none))* :- This takes in the identifier
of the .txt file to write to, where to find the image to draw, what to use as the figure label and as optional parameters:
The size of the image and the caption to attach to it.

*finishdocument(f)* :-Writes the finishing lines to the latex document

Future updates
===============

I'm too lazy to add any more features unless I find something I might need in the future so if you want more bells and 
whistles feel free to fork the repository.
