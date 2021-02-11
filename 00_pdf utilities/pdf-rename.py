# https://github.com/slgobinath/pdfrename/blob/master/pdf-rename.py

# This script is developed by L.Gobinath (www.javahelps.com)
# to rename PDF files using their Title meta-information.
# If the title information is not available. it will skip the files.
# If there is a Title information available for the PDF,
# it will rename the file name to the title name after confirming it from
# the user.

# You need pyPdf Python module to use this script.
# sudo pip install pyPdf

# You also need pdf Python module to use pyPdf
# sudo pip install python-pdf

# sudo apt-get install python-pypdf

from pyPdf import PdfFileReader
import os
import re

count = 0

# Retrive all the files from the current directory
for fileName in os.listdir('.'):
    
    count += 1

    # Print an empty line.
    print("")

    try:
        
        # Process nly the pdf files.
        if fileName.lower()[-3:] != "pdf":
            continue

        # Print the file name.
        print("OldName " + fileName)

        # Retrive the Title of the pdf.
        pdfReader = PdfFileReader(file(fileName, "rb"))
        title = pdfReader.getDocumentInfo().title
        
        # close the pdf
        pdfReader.stream.close()
                
        # Format the Title by removing any special characters.
        newName = "------------" + re.sub('[^-a-zA-Z0-9_.() ]+', '', title) + "-" + str(count) + ".pdf"
        #newName = "------------" + str(count) + ".pdf"

        os.rename(fileName, newName)

        print("NewName " + newName)

    except:
        print("##################################Error in processing file: " + fileName)
        count += 1
        continue
