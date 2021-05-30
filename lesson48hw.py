                                                                    #Модуль ZipFile
import zipfile
import os

folder_path = 'c:\\Users\\Notnik_kg\\PycharmProjects\\lesson1\\folder'
zip_path = 'c:\\Users\Notnik_kg\PycharmProjects\\folder\\test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

my_zip.write('c:\\Python\\folder\\1.txt', compress_type=zipfile.ZIP_DEFLATED)

my_zip.close()