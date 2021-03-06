#!/usr/bin/env python
# encoding: utf-8
import DAL
import os
import pydicom 

root = '/home/jkexin/Desktop/testdata'


def insert_job(list_):

#调用DAL链接数据库，定义函数向mysqldb数据库中插入数据

	
	try:
		msl = DAL.Mysql('127.0.0.1','3306','root','root','homework')
		sql = "insert  tests (NAME,SEX,AGE,Modality) values ('{}','{}','{}','{}')".format(list_[0],list_[1],list_[2],list_[3])
		rowcount,result = msl.execute(sql)
		msl.close()
	except:
		print('sql go error and go to check sql')
	print  result

	return result

def get_dicom_path():

#遍历获取目录下所有dicom存储的路径

	dicom_path_list = []
	for roots,dirs,files in os.walk(root):
		if len(files) > 0:
			print '\n'
			print len(files),'\n'
			dicom_path = os.path.join(roots,os.listdir(roots)[0])
			print dicom_path
			print '----------------------------------------------'
			dicom_path_list.append(dicom_path)

	print dicom_path_list
	return dicom_path_list

def get_dicom_info():

#获取dicom影像信息，调用insert函数向数据控中插入信息。

	dicom_path_list = get_dicom_path()
	for dicom_path in dicom_path_list:
		    ds = pydicom.read_file(dicom_path)
		    dicom_info = [ds.PatientID,ds.PatientSex,ds.PatientAge,ds.Modality]
		    print (dicom_info)
		    check_list = []
		    for i in xrange(len(dicom_info)):
		    	if not  dicom_info[i] in check_list:
		    		check_list.append(dicom_info[i])
		    	
		    insert_job(dicom_info)
		    		
		   		   
if __name__ == '__main__':
	get_dicom_info()
