import sys
import os
import csv
from __exercise_data_config import *
from collections import OrderedDict
from __db_config import *

categorySubCategoryMapping = {}
groupMapping = {}
exerciseListMapping = {}
final_return_files = []
last_exercise_category_id = 0
last_exercise_group_id = 0
last_exercise_list_id = 0
last_exg_exl_id = 0
folder_name = ""

def setLastCatId(db):
    cursor = db.cursor()
    query = "select max(cat_id) from exercise_category;"
    cursor.execute(query)
    cid = cursor.fetchone()
    global last_food_category_id
    if cid[0] is not None:
        last_exercise_category_id = cid[0]
    cursor.close()

def setLastExerciseListId(db):
    cursor = db.cursor()
    query = "select max(exc_id) from exercise_list;"
    cursor.execute(query)
    exid = cursor.fetchone()
    global last_exercise_list_id
    if exid[0] is not None:
        last_exercise_list_id = exid[0]
    cursor.close()

def setLastExerciseGroupId(db):
    cursor = db.cursor()
    query = "select max(grp_id) from exercises_group;"
    cursor.execute(query)
    eg_id = cursor.fetchone()
    global last_exercise_group_id
    if eg_id[0] is not None:
        last_exercise_group_id = eg_id[0]
    cursor.close()

def setLastEGEListId(db):
    cursor = db.cursor()
    query = "select max(id) from exercise_group_exercise_name;"
    cursor.execute(query)
    exglid = cursor.fetchone()
    global last_exg_exl_id
    if exglid[0] is not None:
        last_exg_exl_id = exglid[0]
    cursor.close()
                             
def buildExerciseCategoryMapping(db):
    cursor = db.cursor()
    query = "select cat_id, category_name, sub_category_name from exercise_category;"
    cursor.execute(query)
    cid = cursor.fetchone()
    while cid is not None:
        categorySubCategoryMapping[cid[1] + "-" + cid[2]] = str(cid[0])
        cid = cursor.fetchone()

def buildExerciseGroupMapping(db):
    cursor = db.cursor()
    query = "select grp_id, exercises_group from exercises_group;"
    cursor.execute(query)
    egid = cursor.fetchone()
    while egid is not None:
        groupMapping[egid[1]] = str(egid[0])
        egid = cursor.fetchone()
 
def buildExerciseListMapping(db):
    cursor = db.cursor()
    query = "select exc_id, exercise_name from exercise_list;"
    cursor.execute(query)
    exid = cursor.fetchone()
    while exid is not None:
        exerciseListMapping[exid[1]] = str(exid[0])
        exid = cursor.fetchone()

def readCSVFileIntoListDictionary(fileName):
    listToReturn = []
    with open(fileName, mode = 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        listToReturn = list(csv_reader)
    return listToReturn

def generateExerciseCategoryCSV(dictListToParse):
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
    categorySubCategoryId = last_exercise_category_id + 1

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
        with open(folder_name + CONST.EXERCISE_CATEGORY_FILE, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, categorySubCategoryKeys,lineterminator="\n")
            dict_writer.writeheader()
            dict_writer.writerows(categorySubCategoryList)

def generateExerciseGroupCSV(dictListToParse):

    dictToReturn = {}
    for dictToParse in dictListToParse:
        groupName = dictToParse.get(CONST.GROUP_NAME, '')
        groupDescription = dictToParse.get(CONST.GROUP_DESCRIPTION, '')

        dictToReturn[groupName] = groupDescription

    #print(dictToReturn)

    groupNameGroupDescriptionList = []
    groupNameGroupDescriptionId = last_exercise_group_id + 1
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
        with open(folder_name + CONST.EXERCISE_GROUP_FILE, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, groupNameGroupDescriptionKeys,lineterminator="\n")
            dict_writer.writeheader()
            dict_writer.writerows(groupNameGroupDescriptionList)

def generateExerciseListCSV(dictListToParse):
    dictToReturn = {}
    subCategoriesList = []

    for dictToParse in dictListToParse:
        exerciseName = dictToParse.get(CONST.EXERCISE_NAME, '')
        exerciseParamsList = dictToReturn.get(exerciseName, [])
        timeInMin = dictToParse.get(CONST.TIME_IN_MINUTES, '')
        exerciseParamsList.append(timeInMin)
        exerciseCalories = dictToParse.get(CONST.CALORIES_BURNED, '0')
        exerciseParamsList.append(exerciseCalories)

        #extract the id for category-subcategory combination from already built mappig.
        categoryName = dictToParse.get(CONST.CATEGORY_NAME, '')
        subCategoryName = dictToParse.get(CONST.SUB_CATEGORY_NAME, '')
        categorySubcategoryId = categorySubCategoryMapping.get(categoryName + '-' + subCategoryName, '0')
        exerciseParamsList.append(categorySubcategoryId)

        dictToReturn[exerciseName] = exerciseParamsList


    exerciseItemList = []
    exerciseListId = last_exercise_list_id + 1
    for exerciseName in dictToReturn:
        exerciseId = exerciseListMapping.get(exerciseName,'')
        if (exerciseId == ''):
            exerciseId = str(exerciseListId)
            exerciseListId += 1
            exerciseParamsList = dictToReturn.get(exerciseName, [])        
            exerciseList = OrderedDict()
            exerciseList[CONST.EXERCISE_ID] = exerciseId
            exerciseList[CONST.CATEGORY_ID] = exerciseParamsList[2]
            exerciseList[CONST.EXERCISE_NAME] = exerciseName
            exerciseList[CONST.TIME_IN_MINUTES] = exerciseParamsList[0]
            exerciseList[CONST.CALORIES_BURNED] = exerciseParamsList[1]

            #build a separate mapping for exercise name v/s its id.
            exerciseListMapping[exerciseName] = exerciseId

            exerciseItemList.append(exerciseList)

    if (len(exerciseItemList) >= 1):
        exerciseItemKeys = exerciseItemList[0].keys()
        with open(folder_name + CONST.EXERCISE_LIST_FILE, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, exerciseItemKeys,lineterminator="\n")
            dict_writer.writeheader()
            dict_writer.writerows(exerciseItemList)

def generateExerciseGroupExerciseNameCSV(dictListToParse):
    exerciseGroupExerciseNameList = []
    exerciseGroupExerciseNameId = last_exg_exl_id + 1
    for dictToParse in dictListToParse:
        exerciseGroupExerciseName = OrderedDict()

        #extract the id for exercise group from already built group mappig.
        groupName = dictToParse.get(CONST.GROUP_NAME, '')
        groupNameId = groupMapping.get(groupName, '')

        #extract the id for mapping exercise name from already built exercise mapping.
        exerciseName = dictToParse.get(CONST.EXERCISE_NAME, '')
        exerciseItemId = exerciseListMapping.get(exerciseName, '')

        exerciseGroupExerciseName[CONST.EXERCISE_GROUP_ITEM_ID] = str(exerciseGroupExerciseNameId)
        exerciseGroupExerciseName[CONST.GROUP_ID] = groupNameId
        exerciseGroupExerciseName[CONST.EXERCISE_ID] = exerciseItemId

        exerciseGroupExerciseNameList.append(exerciseGroupExerciseName)
        exerciseGroupExerciseNameId += 1


    if (len(exerciseGroupExerciseNameList) >= 1):
        exerciseGroupExerciseItemKeys = exerciseGroupExerciseNameList[0].keys()
        with open(folder_name + CONST.EXERCISE_GROUP_EXERCISE_NAME_FILE, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, exerciseGroupExerciseItemKeys,lineterminator="\n")
            dict_writer.writeheader()
            dict_writer.writerows(exerciseGroupExerciseNameList)

def fileNames():
    final_return_files = [CONST.EXERCISE_CATEGORY_FILE, CONST.EXERCISE_GROUP_FILE, CONST.EXERCISE_LIST_FILE, CONST.EXERCISE_GROUP_EXERCISE_NAME_FILE]
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
setLastExerciseListId(db)
setLastEGEListId(db)
setLastExerciseGroupId(db)

buildExerciseCategoryMapping(db)
buildExerciseGroupMapping(db)
buildExerciseListMapping(db)

dictList = readCSVFileIntoListDictionary(fileName)
generateExerciseCategoryCSV(dictList)
generateExerciseGroupCSV(dictList)
generateExerciseListCSV(dictList)
generateExerciseGroupExerciseNameCSV(dictList)
fileNames()
db.close()

