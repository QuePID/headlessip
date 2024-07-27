import glob, os, ftplib
# store ip to file ip.txt

# Fetch hostname and store to filename
os.chdir("/bme280/ips/")
hostname = "hostname -I > " + os.uname()[1] + "_ip.txt"
os.system(hostname)

# FTP connections settings
FTP_HOST = "ftp hostname"
FTP_USER = "ftp username";
FTP_PASS = "ftp password"

# Fetch file list into list (array)
os.chdir("ips folder")
filelist = glob.glob("*.txt")

# connect to FTP Server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
ftp.cwd('where to put ip files')
# upload to FTP Server
mycount = 0

for i in filelist:
 file = filelist[mycount]
 with open(file, "rb") as file:
  ftp.storbinary("STOR %s" % file.name,file)
  print(file.name, " uploaded")
  ftp.dir()
  mycount += 1
ftp.close()
