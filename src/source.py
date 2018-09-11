import os
import shutil

from PyPDF2 import PdfFileReader, PdfFileWriter

# Get directory name and all files in directory.
folder = raw_input("Name of directory looking to encrypt and compress: ")
files = os.listdir(folder)

# Get password to encrypt pdf files with.
password = raw_input("Password to encrypt files with: ")

# Generate temp folder name.
newdirect = folder + "123"

# Try to create new temp directory.
try:
	os.makedirs(newdirect)
except OSError:
    pass

# Loop through files in list, open with pdf file reader and copy to file writer then encrypt with password.
for file in files:
	if file.endswith('.pdf'):
		pdfIn = PdfFileReader(open(folder + "/"+ file, "rb"))
		pdfOut = PdfFileWriter()
		pdfOut.appendPagesFromReader(pdfIn)
		pdfOut.encrypt(password)

		# Write new encrypted files to new folder.
		with open(newdirect + "/" + file, "wb") as outFile:
			pdfOut.write(outFile)

# Create compressed file from encrypted files folder.
shutil.make_archive(folder + "-compressed", 'zip', newdirect)

# Delete temporary encrypted files folder.
shutil.rmtree(newdirect)

print "Task Completed"