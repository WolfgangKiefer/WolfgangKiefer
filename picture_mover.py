import os
import time
from datetime import date
from exif import Image
import shutil

def GetDateTaken(filename):
  rc = date.today()
  with open(filename, "rb") as file:
    imgob = Image(file)
    rc = date(int(imgob.Datetime[0:4]), int(imgob.Datetime[5:7]), int(imgob.Datetime[8:10]))
  return rc
  
src = "/fastshare/bilder"
trg = "/sdb/share/Bilder"

for f in os.listdir(src):
	if f[0:3] == "101" and f[-3:] == "jpg" \
	or f[0:3] == "101" and f[-4:] == "jpeg":
		os.rename(os.path.join(src, f), os.path.join(src, "P" + str(f)))
		
for f in os.listdir(src):
	crtdate = time.strptime(time.ctime(os.path.getctime(os.path.join(src, f))))
	crtdate = date(crtdate.tm_year, crtdate.tm_mon, crtdate.tm_mday)
	if f[-3:] == "jpg" or f[-4:] == "jpeg":
		crtdate = GetDateTaken(os.path.join(src, f))
	trgpath = os.path.join(trg, str(crtdate.year), str(crtdate.year) + "_" + str(crtdate.month).zfill(2))
	if not os.path.isdir(trgpath):
		os.makedirs(trgpath)
	shutil.move(os.path.join(src, f), trgpath)
		