# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:50:52 2020

@author: jmyou
"""

import os
import random as rand
import shutil




def move_files(old_dir,new_dir):
    
    for file in os.listdir(old_dir):
        old_path = old_dir + '/' + file
        new_path = new_dir + '/' + file
        shutil.move(old_path,new_path)








def dir_format():
    
    type3 = ['GRO','ALH78119','DAV','ALH85070','WSG','ALH77299']
    type4 = ['QUE','ALH85033','ALH77221']
    type5 = ['ALH78109','ALH81017','ALH77012']
    type6 = ['ALH84081','ALH85017','ALH77288']
    
    
    type3_files = []
    type4_files = []
    type5_files = []
    type6_files = []
    
    files = os.listdir('E:/Gen_Images_BigSetScreened_wnames')
    
    for file in files:
        if '.png' in file:
            sample_name = file.split('_',1)[1].split('.',1)[0]
            if sample_name in type3:
                type3_files.append(file)
            elif sample_name in type4:
                type4_files.append(file)
            elif sample_name in type5:
                type5_files.append(file)
            elif sample_name in type6:
                type6_files.append(file)
            
            else:
                print(file)
    
    
    rand.shuffle(type3_files)
    rand.shuffle(type4_files)
    rand.shuffle(type5_files)
    rand.shuffle(type6_files)  
    
    
    
    t3_test_num = int(round(len(type3_files)/5,0))
    t4_test_num = int(round(len(type4_files)/5,0))
    t5_test_num = int(round(len(type5_files)/5,0))
    t6_test_num = int(round(len(type6_files)/5,0))
    
    t3_val_num = int(round(len(type3_files)/10,0))
    t4_val_num = int(round(len(type4_files)/10,0))
    t5_val_num = int(round(len(type5_files)/10,0))
    t6_val_num = int(round(len(type6_files)/10,0))
    
    
    t3_train = []
    t4_train = []
    t5_train = []
    t6_train = []
    
    t3_test = []
    t4_test = []
    t5_test = []
    t6_test = []
    
    t3_val = []
    t4_val = []
    t5_val = []
    t6_val = []
    
    
    size_3 = len(type3_files)
    train_3 = type3_files[0:size_3-t3_test_num-t3_val_num]
    tester_3= type3_files[size_3-t3_test_num-t3_val_num:size_3-t3_val_num]
    val_3 = type3_files[size_3-t3_val_num:size_3]
    
    size_4 = len(type4_files)
    train_4 = type4_files[0:size_4-t4_test_num-t4_val_num]
    tester_4= type4_files[size_4-t4_test_num-t4_val_num:size_4-t4_val_num]
    val_4 = type4_files[size_4-t4_val_num:size_4]
    
    size_5 = len(type5_files)
    train_5 = type5_files[0:size_5-t5_test_num-t5_val_num]
    tester_5= type5_files[size_5-t5_test_num-t5_val_num:size_5-t5_val_num]
    val_5 = type5_files[size_5-t5_val_num:size_5]
    
    size_6 = len(type6_files)
    train_6 = type6_files[0:size_6-t6_test_num-t6_val_num]
    tester_6= type6_files[size_6-t6_test_num-t6_val_num:size_6-t6_val_num]
    val_6 = type6_files[size_6-t6_val_num:size_6]
    
    
    for file in train_3:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Train/Type3/' + file
        shutil.move(old_file, new_file)
        
    for file in train_4:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Train/Type4/' + file
        shutil.move(old_file, new_file)
    
    for file in train_5:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Train/Type5/' + file
        shutil.move(old_file, new_file)
    
    for file in train_6:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Train/Type6/' + file
        shutil.move(old_file, new_file)
    
    for file in val_3:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Validation/Type3/' + file
        shutil.move(old_file, new_file)
    
    for file in val_4:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Validation/Type4/' + file
        shutil.move(old_file, new_file)
    
    for file in val_5:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Validation/Type5/' + file
        shutil.move(old_file, new_file)
    
    for file in val_6:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Validation/Type6/' + file
        shutil.move(old_file, new_file)
        
    for file in tester_3:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Test/' + file
        shutil.move(old_file, new_file)
    
    for file in tester_4:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Test/' + file
        shutil.move(old_file, new_file)
    
    for file in tester_5:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Test/' + file
        shutil.move(old_file, new_file)
    
    for file in tester_6:
        old_file = 'E:/Gen_Images_BigSetScreened_wnames/' + file
        new_file = 'E:/Gen_Images_BigSetScreened_wnames/Test/' + file
        shutil.move(old_file, new_file)    
        
        


def reset_dir():
    
    home_dir = 'E:/Gen_Images_BigSetScreened_wnames'
    
    test_dir = 'E:/Gen_Images_BigSetScreened_wnames/Test'
    
    train_dir3 = 'E:/Gen_Images_BigSetScreened_wnames/Train/Type3'
    train_dir4 = 'E:/Gen_Images_BigSetScreened_wnames/Train/Type4'
    train_dir5 = 'E:/Gen_Images_BigSetScreened_wnames/Train/Type5'
    train_dir6 = 'E:/Gen_Images_BigSetScreened_wnames/Train/Type6'
    
    
    val_dir3 = 'E:/Gen_Images_BigSetScreened_wnames/Validation/Type3'
    val_dir4 = 'E:/Gen_Images_BigSetScreened_wnames/Validation/Type4'
    val_dir5 = 'E:/Gen_Images_BigSetScreened_wnames/Validation/Type5'
    val_dir6 = 'E:/Gen_Images_BigSetScreened_wnames/Validation/Type6'
    
    move_files(test_dir, home_dir)
    
    move_files(train_dir3, home_dir)
    move_files(train_dir4, home_dir)
    move_files(train_dir5, home_dir)
    move_files(train_dir6, home_dir)
    
    move_files(val_dir3, home_dir)
    move_files(val_dir4, home_dir)
    move_files(val_dir5, home_dir)
    move_files(val_dir6, home_dir)


    print('Files Reset')
    
reset_dir()
dir_format()   