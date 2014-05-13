#quick data presenter
#Written by Stuart Bowe
#13/05/14
import os

def openinglines(filename):

    
    if os.path.isfile(filename):
        print 'WARNING: Overwriting previous file'
        open(filename, 'w').close()#emptys the file and warns the user that it's
        #doing so

        
    f = open(filename, 'w+')
    f.write('\\documentclass[12pt,a4paper]{report}\n')
    f.write('\\usepackage{amsmath}\n')
    f.write('\\usepackage{amssymb}\n')
    f.write('\\usepackage{graphicx}\n')
    f.write('\\usepackage{hyperref}\n')
    f.write('\\usepackage{caption}\n')
    f.write('\\usepackage{subcaption}\n')
    f.write('\\usepackage{float}\n')
    f.write('\\newcommand{\\baselinestrech}{1.5}\n')
    f.write('\n')
    f.write('\\begin{document}\n')
    return f

def printimage(f, imagepath , figurelabel, width = 0.5, caption = ''):
    f.write('\\begin{figure} [H]\n')
    f.write('\\begin{center}\n')
    f.write('\\caption{' + caption + '}\n')
    f.write('\\label{fig:' + figurelabel + '}\n')
    f.write('\\includegraphics[width=' + repr(width) + ' \\textwidth]{' + imagepath + '}\n')
    f.write('\\end{center}\n')
    f.write('\\end{figure}\n')
    f.write('\n')

def finishdocument(f):
    f.write('\n')
    f.write('\\end{document}\n')
    f.close()




filename = 'Exampleuse.txt'
f = openinglines(filename)

for width in range(100, 600, 100):
    for Ks in range(1, 100, 5):
        imagepath = 'C:/examplefolder/examplimage.jpeg'
        caption = 'An example use of this program' + repr(Ks) + repr(width)
        figurelabel = caption
        printimage(f, imagepath, figurelabel, 0.15, caption)


finishdocument(f)
