import os
rootdir = r'D:\EXON\Exxn_Intergration\S_H114'  #directory path

for subdir, dirs, files in os.walk(rootdir):
    print("SubDir-",subdir,"dirs-",dirs)
    for file in files:
        print(file)
        image_name_txt = file.split('.')[0] + "." + "txt"
        #print("image_name_txt-->",image_name_txt)
        file_path = os.path.join(subdir, file)
        #print("file_path->",file_path)
        file_name_save = os.path.join(subdir, image_name_txt)
        #ABBYY_ocr.sep_ocr(file_path,"q",file_name_save)
        print("file_name_save",file_name_save)
