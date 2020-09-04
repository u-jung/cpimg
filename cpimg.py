#!/usr/bin/env python3
import os
import shutil
from PIL import Image
import sys
import re

def get_date(file_name: str) -> Tuple[str, str, str]:
	"""Get picture date from EXIF data."""
	#print(file_name)
	try:
		im = Image.open(file_name)
		exif=im._getexif()
		if exif:
			if 306 in exif:
				date_time = exif[306].split(" ")
				return date_time[0].split(":")
		return ("1970","01","01")
	except:
		print ("This ist not a jpg file!")
		return ("1970","01","01")

def get_images_files(source_dir: str) -> List[]:
	list_=[]
	for root, dirs, files in os.walk(source_dir, topdown=False):
		for f in files:
			list_.append(os.path.join(root,f))
	return list_

# cpimg source_dir dest_dir_root

def main(args):
	i=[0,0,0]
	if len(sys.argv)!=3:
		print ("Please enter the command as follows: cpimg source_dir dest_dir")
		print ("Use absolute paths")
		print ("This is not working with  Python < version 3.3")
		return 1
	
	base_dir = sys.argv[2]
	source_dir = sys.argv[1]


	for fn in get_images_files(source_dir):
		print(fn)
		if not fn.lower().endswith(('.jpg','.jpeg')):
			print("skip")
			i[0]+=1
			continue
		year, month,day = get_date(os.path.join(source_dir, fn))
		dest_dir = os.path.join(base_dir, year, month,day)
		os.makedirs(dest_dir, exist_ok=True)
		if os.path.exists(os.path.join(dest_dir, fn)):
			i[1]+=1
			print('{} already exists. Skipping this file'.format(fn))
		else:
			print('Copying {} to {}'.format(fn, dest_dir))
			i[2]+=1
			shutil.copy2(source, dest_dir)
	print("---------------------")
	print("Files in directory:",i[0]+i[1]+i[2])
	print("Files skipped (There aren't *.jpg):",i[0])
	print("Files that already exist (not copied):",i[1])
	print("Files copied:",i[2])
	return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
