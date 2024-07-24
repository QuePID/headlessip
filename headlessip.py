import glob, os, ftplib
# store ip to file ip.txt
os.system('hostname -I > ip.txt')

FTP_HOST = "put_ftp_server_ip_or_hostname_here"
FTP_USER = "put_ftp_username_here";
FTP_PASS = "put_ftp_password_here"

# Fetch file list into list (array)
#os.chdir("/root)
filelist = glob.glob("ip.txt")
print(filelist)

# connect to FTP Server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"
ftp.cwd('put_folder_on_server_to_hold_ip_files')
ftp.dir()
# upload to FTP Server
mycount = 0

for i in filelist:
 file = filelist[mycount]
 with open(file, "rb") as file:
  ftp.storbinary("STOR %s" % file.name,file)
  print(file.name, " uploaded")
  ftp.dir()
  mycount += 1
