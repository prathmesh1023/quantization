import pyexiv2
import re
flag=0
patterns = ['Adobe','adobe','ADOBE','photoshop','Photoshop','Affinity','PaintShop','Acorn','PhotLab','Camera+','Pixelmator ','Pixlr','GIMP','Paint.net','Sumo Paint','Aviary']
data = pyexiv2.metadata.ImageMetadata('dog2.jpg')
data.read()
for key in data.exif_keys:
 tag = data[key]
 s=key
 k=tag.value
 if 'Software' in s:
  print(' %-40s%s' %(s, k))
  for p in patterns:
  	if re.search(p,k):
  		flag=1
if(flag==1):
	print("forged")
else:
	print("original")	  