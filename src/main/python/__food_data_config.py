import sys
import json
import csv


class _Const(object):

    JSON_CONFIG_FILE='/opt/atman/config/food_data_config.json'
    FOOD_CATEGORY='food_category'
    FOOD_GROUP='food_group'
    FOOD_ITEM='food_item'
    FOOD_GROUP_FOOD_ITEM='food_group_food_item'
    FOOD_CATEGORY_COLUMNS='food_category_columns'
    FOOD_GROUP_COLUMNS='food_group_columns'
    FOOD_ITEM_COLUMNS='food_item_columns'
    FOOD_GROUP_FOOD_ITEM_COLUMNS='food_group_food_item_columns'
    DEFAULT_FOLDER='/opt/atman/sql/'
    FOOD_CATEGORY_FILE='food_category.csv'
    FOOD_GROUP_FILE='food_group.csv'
    FOOD_ITEM_FILE='food_item.csv'
    FOOD_GROUP_FOOD_ITEM_FILE='food_group_food_item.csv'
    CATEGORY_ID = 'cat_id'
    CATEGORY_NAME = 'category_name'
    SUB_CATEGORY_NAME = 'sub_category_name'
    GROUP_ID = 'fgrp_id'
    GROUP_NAME = 'group_name'
    GROUP_DESCRIPTION = 'group_description'
    ITEM_ID = 'fdit_id'
    FOOD_NAME = 'food_name'
    FOOD_CALORIES = 'food_calories'
    MIN_QUANTITY = 'min_quantity'
    FOOD_GROUP_ITEM_ID = 'id'


class FoodConfigManager:
    foodDataConfigJson         = ''
    foodDataConfigData         = {}
    foodCategory               = {}
    foodGroup                  = {}
    foodItem                   = {}
    foodGroupFoodItem          = {}
    foodCategoryColumns        = []
    foodGroupColumns           = []
    foodItemColumns            = []
    foodGroupFoodItemColumns   = []
    foodCategoryFile           = ''
    foodGroupFile              = ''
    foodItemFile               = ''
    foodGroupFoodItemFile      = ''

    def __init__(self):
        CONST = _Const
        with open(CONST.JSON_CONFIG_FILE) as fileObject:
            self.foodDataConfigJson = fileObject.read()
            #print (self.foodDataConfigJson)
        with open(CONST.JSON_CONFIG_FILE) as fileObject:
            self.foodDataConfigData = json.load(fileObject)
            #print (self.foodDataConfigData)
            self.foodCategory = self.foodDataConfigData.get(CONST.FOOD_CATEGORY,{})
            #print (self.foodCategory)
            self.foodGroup = self.foodDataConfigData.get(CONST.FOOD_GROUP,{})
            #print (self.foodGroup)
            self.foodItem = self.foodDataConfigData.get(CONST.FOOD_ITEM,{})
            #print (self.foodItem)
            self.foodGroupFoodItem = self.foodDataConfigData.get(CONST.FOOD_GROUP_FOOD_ITEM,{})
            #print (self.foodGroupFoodItem)
            self.foodCategoryColumns = self.foodCategory.get(CONST.FOOD_CATEGORY_COLUMNS,[])
            #print (self.foodCategoryColumns)
            self.foodGroupColumns = self.foodGroup.get(CONST.FOOD_GROUP_COLUMNS,[])
            #print (self.foodGroupColumns)
            self.foodItemColumns = self.foodItem.get(CONST.FOOD_ITEM_COLUMNS,[])
            #print (self.foodItemColumns)
            self.foodGroupFoodItemColumns = self.foodGroupFoodItem.get(CONST.FOOD_GROUP_FOOD_ITEM_COLUMNS,[])
            #print (self.foodGroupFoodItemColumns)

        
    def getConfigParamValue(self,configParam):
        return self.foodDataConfigData.get(configParam, '')
    def getfoodCategory(self):
        return self.foodCategory
    def getfoodGroup(self):
        return self.foodGroup
    def getfoodItem(self):
        return self.foodItem
    def getfoodGroupFoodItem(self):
        return self.foodGroupFoodItem
    def getfoodCategoryColumns(self):
        return self.foodCategoryColumns
    def getfoodGroupColumns(self):
        return self.foodGroupColumns
    def getfoodItemColumns(self):
        return self.foodItemColumns
    def getfoodGroupFoodItemColumns(self):
        return self.foodGroupFoodItemColumns

    def printFoodConfig(self):
        print (self.foodDataConfigJson)
        print (self.foodDataConfigData)
        print (self.foodCategory)
        print (self.foodGroup)
        print (self.foodItem)
        print (self.foodGroupFoodItem)
        print (self.foodCategoryColumns)
        print (self.foodGroupColumns)
        print (self.foodItemColumns)
        print (self.foodGroupFoodItemColumns)


foodConfigManager = FoodConfigManager()

#helper methods

def getFoodConfigParamValue(configParam):
    return foodConfigManager.getConfigParamValue(configParam)
def getConfigParamValue():
    return foodConfigManager.foodDataConfigData.get(configParam, '')
def getFoodCategory():
    return foodConfigManager.getfoodCategory()
def getFoodGroup():
    return foodConfigManager.getfoodGroup()
def getFoodItem():
    return foodConfigManager.getfoodItem()
def getFoodGroupFoodItem():
    return foodConfigManager.getfoodGroupFoodItem()
def getFoodCategoryColumns():
    return foodConfigManager.getfoodCategoryColumns()
def getFoodGroupColumns():
    return foodConfigManager.getfoodGroupColumns()
def getFoodItemColumns():
    return foodConfigManager.getfoodItemColumns()
def getFoodGroupFoodItemColumns():
    return foodConfigManager.getfoodGroupFoodItemColumns()
#call functions which returns dictionary of key and value
#foodcategory = getFoodCategory()
#foodgroup = getFoodGroup()
#fooditem = getFoodItem()
#foodgroupfooditem = getFoodGroupFoodItem()
#foodcategorycol = getFoodCategoryColumns()
#foodgroupcol = getFoodGroupColumns()
#fooditemcol = getFoodItemColumns()
#foodgroupfooditemcol = getFoodGroupFoodItemColumns()
#foodConfigManager.printFoodConfig()
CONST = _Const()

