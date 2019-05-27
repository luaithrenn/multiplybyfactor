PACKAGE_URL = 'git+https://github.com/luaithrenn/multiplybyfactor.git@'
#URL of the package repository.
    
import datetime as dt
import json
import os
import pandas as pd
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, func
from iotfunctions.preprocessor import BaseTransformer
from iotfunctions.base import BaseTransformer
from iotfunctions.metadata import EntityType
from iotfunctions.db import Database
from iotfunctions import ui

#Create a function to multiple an input item  value by a factor value that is specified through the UI. 

class MultiplyByFactor(BaseTransformer):
   
    '''
    Multiply input items by a factor to produce a result
    '''
    
    url = PACKAGE_URL

     
    def __init__(self, input_items, factor, output_items):
    #Initalization method.  Define input and output items here.  

        self.input_items = input_items
        self.output_items = output_items
        self.factor = float(factor)
        super().__init__()
        

    def execute(self, df):
    #Execute method. 
        
        df = df.copy()
        for i,input_item in enumerate(self.input_items):
        df[self.output_items[i]] = df[input_item] * self.factor
        return df
      
    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
                name = 'input_items',
                datatype=float,
                description = "Input items to be adjusted",
                output_item = 'output_items',
                is_output_datatype_derived = True)
                      )        
        inputs.append(ui.UISingle(
                name = 'factor',
                datatype=float)
                      )
        outputs = []
        return (inputs,outputs)   
