import sys
import json
import csv

class _Const(object):
    JSON_CONFIG_FILE='/opt/atman/config/exercise_data_config.json'
    EXERCISE_CATEGORY='exercise_category'
    EXERCISE_GROUP='exercises_group'
    EXERCISE_LIST='exercise_list'
    EXERCISE_GROUP_EXERCISE_NAME='exercise_group_exercise_name'
    EXERCISE_CATEGORY_COLUMNS='exercise_category_columns'
    EXERCISE_GROUP_COLUMNS='exercise_group_columns'
    EXERCISE_LIST_COLUMNS='exercise_list_columns'
    EXERCISE_GROUP_EXERCISE_NAME_COLUMNS='exercise_group_exercise_name_columns'
    DEFAULT_FOLDER='/opt/atman/sql/'
    EXERCISE_CATEGORY_FILE='exercise_category.csv'
    EXERCISE_GROUP_FILE='exercises_group.csv'
    EXERCISE_LIST_FILE='exercise_list.csv'
    EXERCISE_GROUP_EXERCISE_NAME_FILE='exercise_group_exercise_name.csv'
    CATEGORY_ID='cat_id'
    CATEGORY_NAME='category_name'
    SUB_CATEGORY_NAME='sub_category_name'
    GROUP_ID='grp_id'
    GROUP_NAME='exercises_group'
    GROUP_DESCRIPTION='group_description'
    EXERCISE_ID='exc_id'
    EXERCISE_NAME='exercise_name'
    TIME_IN_MINUTES="time_in_minutes"
    CALORIES_BURNED="calories_burned"
    EXERCISE_GROUP_ITEM_ID="id"
   

class ExerciseConfigManager:
    exerciseDataConfigJson = ''
    exerciseDataConfigData = {}
    exerciseCategory = {}
    exerciseGroup = {}
    exerciseList = {}
    exerciseGroupExerciseName = {}
    exerciseCategoryColumns = []
    exerciseListColumns = []
    exerciseGroupColumns = []
    exerciseGroupExerciseNameColumns = []
    exerciseCategoryFile = ''
    exerciseGroupFile = ''
    exerciseListFile = ''
    exerciseGroupExerciseNameFile = ''

    def __init__(self):
        CONST = _Const
        with open(CONST.JSON_CONFIG_FILE) as fileObject:
            self.exerciseDataConfigJson = fileObject.read()
        with open(CONST.JSON_CONFIG_FILE) as fileObject:
            self.exerciseDataConfigData = json.load(fileObject)
            self.exerciseCategory = self.exerciseDataConfigData.get(CONST.EXERCISE_CATEGORY, {})
            self.exerciseGroup = self.exerciseDataConfigData.get(CONST.EXERCISE_GROUP, {})
            self.exerciseList = self.exerciseDataConfigData.get(CONST.EXERCISE_LIST, {}) 
            self.exerciseGroupExerciseName = self.exerciseDataConfigData.get(CONST.EXERCISE_GROUP_EXERCISE_NAME, {})     
            self.exerciseCategoryColumns = self.exerciseCategory.get(CONST.EXERCISE_CATEGORY,{})
            self.exerciseGroupColumns = self.exerciseGroup.get(CONST.EXERCISE_GROUP, {})
            self.exerciseListColumns = self.exerciseList.get(CONST.EXERCISE_LIST,{})
            self.exerciseGroupExerciseNameColumns = self.exerciseGroupExerciseName.get(CONST.EXERCISE_GROUP_EXERCISE_NAME_COLUMNS, {})
         
    def getConfigParamValue(self, configParam):
        return self.exerciseDataConfigData.get(configParam, '')
    def getExerciseCategory(self):
        return self.exerciseCategory
    def getExerciseGroup(self):
        return self.exercisesGroup
    def getExerciseList(self):
        return self.exerciseList
    def getExerciseGroupExerciseName(self):
        return self.exerciseGroupExerciseName
    def getExerciseCategoryColumns(self):
        return self.exerciseCategoryColumns
    def getExerciseGroupColumns(self):
        return self.exerciseGroupColumns
    def getExerciseListColumns(self):
        return self.exerciseListColumns
    def getExerciseGroupExerciseNameColumns(self):
        return self.exerciseGroupExerciseNameColumns
 
exerciseConfigManager = ExerciseConfigManager()

def getExerciseConfigParamValue(configParam):
    return foodConfigManager.getConfigParamValue(configParam)
def getConfigParamValue():
    return foodConfigManager.foodDataConfigData.get(configParam, '')
def getExerciseCategory():
    return foodConfigManager.getExerciseCategory()
def getExerciseGroup():
    return foodConfigManager.getExerciseGroup()
def getExerciseList():
    return foodConfigManager.getExerciseList()
def getExerciseGroupExerciseList():
    return foodConfigManager.getExerciseGroupExerciseList()
def getExerciseCategoryColumns():
    return foodConfigManager.getExerciseCategoryColumns()
def getExerciseGroupColumns():
    return foodConfigManager.getExerciseGroupColumns()
def getExerciseItemColumns():
    return foodConfigManager.getExerciseListColumns()
def getExerciseGroupExerciseItemColumns():
    return foodConfigManager.getExerciseGroupExerciseNameColumns()
   

CONST = _Const()

