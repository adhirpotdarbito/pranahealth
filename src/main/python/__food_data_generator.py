import sys
import os
import csv
from __food_data_config import *
from collections import OrderedDict
from __db_config import *

categorySubCategoryMapping = {}
groupMapping = {}
foodItemMapping = {}
final_return_files = []
last_food_category_id = 0
last_food_item_id = 0
last_food_group_id = 0
last_fg_fi_id = 0
folder_name = ""

def setLastCatId(db):
    cat_id = []
    cursor = db.cursor()
    query = "select max(cat_id) from food_category;"
    cursor.execute(query)
    cid = cursor.fetchone()
    global last_food_category_id
    if cid[0] is not None:
        last_food_category_id = cid[0]
    #print last_food_category_id
    cursor.close()

def setLastFoodItemId(db):
    food_item_id = []
    cursor = db.cursor()
    query = "select max(fdit_id) from food_item;"
    cursor.execute(query)
    fid = cursor.fetchone()
    global last_food_item_id
    if fid[0] is not None:
        last_food_item_id = fid[0]
    #print last_food_item_id
    cursor.close()

def setLastFoodGroupId(db):
    food_group_id = []
    cursor = db.cursor()
    query = "select max(fgrp_id) from food_group;"
    cursor.execute(query)
    fg_id = cursor.fetchone()
    global last_food_group_id
    if fg_id[0] is not None:
        last_food_group_id = fg_id[0]
    #print last_food_group_id
    cursor.close()

def setLastFGFItemId(db):
    food_group_item_id = []
    cursor = db.cursor()
    query = "select max(id) from food_group_food_item;"
    cursor.execute(query)
    fgid = cursor.fetchone()
    global last_fg_fi_id
    if fgid[0] is not None:
        last_fg_fi_id = fgid[0]
    #print last_fg_fi_id
    cursor.close()
       
 
def buildFoodCategoryMapping(db):
    cursor = db.cursor()
    query = "select cat_id, category_name, sub_category_name from food_category;"
    cursor.execute(query)
    cid = cursor.fetchone()
    while cid is not None:
        categorySubCategoryMapping[cid[1] + "-" + cid[2]] = str(cid[0])
        cid = cursor.fetchone()

def buildFoodGroupMapping(db):
    cursor = db.cursor()
    query = "select fgrp_id, group_name from food_group;"
    cursor.execute(query)
    fgid = cursor.fetchone()
    while fgid is not None:
        groupMapping[fgid[1]] = str(fgid[0])
        fgid = cursor.fetchone()

def buildFoodItemMapping(db): 
    cursor = db.cursor()
    query = "select fdit_id, food_name from food_item;"
    cursor.execute(query)
    fid = cursor.fetchone()
    while fid is not None:
        foodItemMapping[fid[1]] = str(fid[0])
        fid = cursor.fetchone()

def readCSVFileIntoListDictionary(fileName):
    listToReturn = []
    with open(fileName, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file) 
        listToReturn = list(csv_reader)

    return listToReturn

def generateFoodCategoryCSV(dictListToParse):
    dictToReturn = {}
    subCategoriesList = []

    for dictToParse in dictListToParse:
        categoryName = dictToParse.get(CONST.CATEGORY_NAME, '')
        subCategoriesList = dictToReturn.get(categoryName, [])
        subCategoryName = dictToParse.get(CONST.SUB_CATEGORY_NAME, '')
        subCategoriesList.append(subCategoryName)
        dictToReturn[categoryName] = subCategoriesList

    for categoryName in dictToReturn:
        subCategoriesList = dictToReturn[categoryName]
        subCategorriesSet = set(subCategoriesList)
        subCategoriesList = list(subCategorriesSet)
        dictToReturn[categoryName] = subCategoriesList
    
    categorySubCategoryList = []
    categorySubCategoryId = last_food_category_id + 1

    for categoryName in dictToReturn:
        subCategoriesList = dictToReturn.get(categoryName, [])
        for subCategoryName in subCategoriesList:

            #update a mapping for category name & subcategory name v/s its id if not available.
            categorySubcategory = categoryName + '-' + subCategoryName
            catId = categorySubCategoryMapping.get(categorySubcategory, '') 
            if (catId == ''):
                catId = str(categorySubCategoryId)  
                categorySubCategoryMapping[categorySubcategory] = catId
                categorySubCategoryId += 1

                categorySubCategory = OrderedDict()
                categorySubCategory[CONST.CATEGORY_ID] = catId
                categorySubCategory[CONST.CATEGORY_NAME] = categoryName
                categorySubCategory[CONST.SUB_CATEGORY_NAME] = subCategoryName

                categorySubCategoryList.append(categorySubCategory)

    if (len(categorySubCategoryList) >= 1):
        categorySubCategoryKeys = categorySubCategoryList[0].keys()
        with open(folder_name + CONST.FOOD_CATEGORY_FILE, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, categorySubCategoryKeys,lineterminator="\n")
            dict_writer.writeheader()
            dict_writer.writerows(categorySubCategoryList)

           
def generateFoodGroupCSV(dictListToParse):

    dictToReturn = {}
    for dictToParse in dictListToParse:
        groupName = dictToParse.get(CONST.GROUP_NAME, '')
        groupDescription = dictToParse.get(CONST.GROUP_DESCRIPTION, '')

        dictToReturn[groupName] = groupDescription

    #print(dictToReturn)
    
    groupNameGroupDescriptionList = []
    groupNameGroupDescriptionId = last_food_group_id + 1
    for groupName in dictToReturn:
        #build a separate mapping for group name its id.
        #groupMapping[groupName] = str(groupNameGroupDescriptionId)
        grpId = groupMapping.get(groupName, '')
        if (grpId == ''):
            grpId = str(groupNameGroupDescriptionId) 
            groupMapping[groupName] = grpId 
            groupNameGroupDescriptionId += 1
            groupNameGroupDescription = OrderedDict()
            groupNameGroupDescription[CONST.GROUP_ID] = grpId
            groupNameGroupDescription[CONST.GROUP_NAME] = groupName
            groupNameGroupDescription[CONST.GROUP_DESCRIPTION] = dictToReturn.get(groupName, '')
            groupNameGroupDescriptionList.append(groupNameGroupDescription)

    if (len(groupNameGroupDescriptionList) >= 1):
        groupNameGroupDescriptionKeys = groupNameGroupDescriptionList[0].keys()
        with open(folder_name + CONST.FOOD_GROUP_FILE, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, groupNameGroupDescriptionKeys,lineterminator="\n")
            dict_writer.writeheader()
            dict_writer.writerows(groupNameGroupDescriptionList)

def generateFoodItemCSV(dictListToParse):
    dictToReturn = {}
    subCategoriesList = []

    for dictToParse in dictListToParse:
        foodName = dictToParse.get(CONST.FOOD_NAME, '')
        foodParamsList = dictToReturn.get(foodName, [])
        minQuantity = dictToParse.get(CONST.MIN_QUANTITY, '')
        foodParamsList.append(minQuantity)
        foodCalories = dictToParse.get(CONST.FOOD_CALORIES, '0')
        foodParamsList.append(foodCalories)

        #extract the id for category-subcategory combination from already built mappig.
        categoryName = dictToParse.get(CONST.CATEGORY_NAME, '')
        subCategoryName = dictToParse.get(CONST.SUB_CATEGORY_NAME, '')
        categorySubcategoryId = categorySubCategoryMapping.get(categoryName + '-' + subCategoryName, '0')
        foodParamsList.append(categorySubcategoryId)

        dictToReturn[foodName] = foodParamsList

    foodItemList = []
    foodItemId = last_food_item_id + 1
    for foodName in dictToReturn:
        foodId = foodItemMapping.get(foodName,'')
        if (foodId == ''):
            foodId = str(foodItemId)
            foodItemId += 1
            foodParamsList = dictToReturn.get(foodName, [])        
            foodItem = OrderedDict()
            foodItem[CONST.ITEM_ID] = foodId
            foodItem[CONST.CATEGORY_ID] = foodParamsList[2]
            foodItem[CONST.FOOD_NAME] = foodName
            foodItem[CONST.FOOD_CALORIES] = foodParamsList[1]
            foodItem[CONST.MIN_QUANTITY] = foodParamsList[0]

            #build a separate mapping for food name v/s its id.
            foodItemMapping[foodName] = foodId

            foodItemList.append(foodItem)

    if (len(foodItemList) >= 1):
        foodItemKeys = foodItemList[0].keys()
        with open(folder_name + CONST.FOOD_ITEM_FILE, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, foodItemKeys,lineterminator="\n")
            dict_writer.writeheader()
            dict_writer.writerows(foodItemList)


def generateFoodGroupFoodItemCSV(dictListToParse):
    foodGroupFoodItemList = []
    foodGroupFoodItemId = last_fg_fi_id + 1
    for dictToParse in dictListToParse:
        foodGroupFoodItem = OrderedDict()

        #extract the id for food group from already built group mappig.
        groupName = dictToParse.get(CONST.GROUP_NAME, '')
        groupNameId = groupMapping.get(groupName, '')

        #extract the id for mapping food name from already built food mapping.
        foodName = dictToParse.get(CONST.FOOD_NAME, '')
        foodItemId = foodItemMapping.get(foodName, '')

        foodGroupFoodItem[CONST.FOOD_GROUP_ITEM_ID] = str(foodGroupFoodItemId)
        foodGroupFoodItem[CONST.GROUP_ID] = groupNameId
        foodGroupFoodItem[CONST.ITEM_ID] = foodItemId

        foodGroupFoodItemList.append(foodGroupFoodItem)
        foodGroupFoodItemId += 1

    if (len(foodGroupFoodItemList) >= 1):
        foodGroupFoodItemKeys = foodGroupFoodItemList[0].keys()
        with open(folder_name + CONST.FOOD_GROUP_FOOD_ITEM_FILE, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, foodGroupFoodItemKeys,lineterminator="\n")
            dict_writer.writeheader()
            dict_writer.writerows(foodGroupFoodItemList)
            
def filesName():
    final_return_files = [CONST.FOOD_CATEGORY_FILE, CONST.FOOD_GROUP_FILE, CONST.FOOD_ITEM_FILE, CONST.FOOD_GROUP_FOOD_ITEM_FILE]
    print final_return_files
    return final_return_files

fileName = sys.argv[1]
folder_name = CONST.DEFAULT_FOLDER
#read the given CSV file into list of dictionaries.
if len(sys.argv) > 2:
    folder_name = sys.argv[2]
    if not os.path.exists(folder_name):
        os.makedirs(os.path.dirname(folder_name))

init_db()
db = get_db()
setLastCatId(db)
setLastFoodItemId(db)
setLastFGFItemId(db)
setLastFoodGroupId(db)

buildFoodCategoryMapping(db)
buildFoodGroupMapping(db)
buildFoodItemMapping(db)
 
dictList = readCSVFileIntoListDictionary(fileName)
#now create the food category csv file
generateFoodCategoryCSV(dictList)
generateFoodGroupCSV(dictList)
generateFoodItemCSV(dictList)
generateFoodGroupFoodItemCSV(dictList)
filesName()
db.close()

