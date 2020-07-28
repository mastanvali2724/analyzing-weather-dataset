# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 


#Code for categorical variable
def categorical(df):
    categorical_var=df.select_dtypes(include='object')
    return categorical_var
    """ Extract names of categorical column
    
    This function accepts a dataframe and returns categorical list,
    containing the names of categorical columns(categorical_var).
    
    Keyword arguments:
    df - Pandas dataframe from which the columns name will be extracted
        
    Returns:
    categorical_var - List of categorical features
    """
 


#Code for numerical variable
def numerical(df):
    numerical_var=df.select_dtypes(include='number')
    return numerical_var
    """ Extract names of numerical column
    
    This function accepts a dataframe and returns numerical list,
    containing the names of numerical columns(numerical_var).
        
    Keyword arguments:
    df - Pandas dataframe from which the columns name will be extracted
    
    Returns:
    numerical_var - List of numerical features
    """
    



#code to check distribution of variable
def clear(df,col,val):
    """ Check distribution of variable
    
    This function accepts a dataframe,column(feature) and value which returns count of the value,
    containing the value counts of a variable(value_counts)
    
    Keyword arguments:
    df - Pandas dataframe
    col - Feature of the datagrame
    val - value of the feature
    
    Returns:
    value_counts - Value count of the feature 
    """
    value_counts=0
    if(col in df.columns):
        for value in df[col].values:
            if(value==val):
                value_counts+=1
    return value_counts            
   
#Code to check instances based on the condition
def instances_based_condition(df,col1,val1,col2,val2):

    """ Instances based on the condition
    
    This function accepts a dataframe, 2 columns(feature) and 2 values which returns the dataframe
    based on the condition.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - First feature of the dataframe on which you want to apply the filter
    val1 - Value to be filtered on the first feature
    col2 - Second feature of the dataframe on which you want to apply the filter
    val2 - Value to be filtered on second feature
    
    Returns:
    instance - Generated dataframe
    """
    column1=df[col1]>val1
    column2=df[col2]==val2
    instance=df[(column1)&(column2)]
    return instance	
    



# Code to calculate different aggreagted values according to month

def agg_values_ina_month(df,date_col,agg_col, agg):
    df[date_col]=pd.to_datetime(df[date_col])
    df['Date']=df[date_col].values.astype('datetime64[M]')
    df['Month']=pd.DatetimeIndex(df['Date']).month

    aggregated_value=pd.pivot_table(df,index='Month',values=agg_col,aggfunc=agg)
    return aggregated_value
    """  Aggregate values according to month
    
    This function accepts a dataframe, 2 columns(feature) and aggregated funcion(agg) which returns the Pivot 
    table with different aggregated value of the feature with an index of the month.
     
    Keyword arguments:
    df - Pandas dataframe which has the data.
    date_col - Date feature of the dataframe on which you want to apply to_datetime conversion
    agg_col - Feature of the dataframe on which values will be aggregated.
    agg - Dictionary of aggregate functions with feature as the key and func as the value
    
    Returns:
    aggregated_value - Generated pivot table
    """



# Code to group values based on the feature
def group_values(df,col1,agg1):
    grouping=df.groupby([col1])['Temp (C)','Dew Point Temp (C)','Rel Hum (%)','Wind Spd (km/h)','Visibility (km)','Stn Press (kPa)'].agg(agg1)

    return grouping
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 1 column(feature) and aggregated function(agg1) which groupby the 
    datframe based on the column.
   
   Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    



# function for conversion 
def convert(df,celsius):
    df[celsius]=df[celsius]*1.8+32
    return df[celsius]    
    """ Convert temperatures from celsius to fahrenhheit
    
    This function accepts a dataframe, 1 column(feature) which returns the dataframe with converted values from 
    celsius to fahrenhheit.
         
    Keyword arguments:
    df - Pandas dataframe which has the data.
    celsius - Temperature feature of the dataframe which you want to convert to fahrenhheit
    
    Returns:
    converted_temp - Generated dataframe with Fahrenhheit temp.
    
    """
    

weather_data=pd.read_csv(path)
weather=pd.DataFrame(weather_data)
# Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable `path` for you.
categorical(weather)

numerical(weather)
# As you have now loaded the weather data you might want to check the categorical and numerical variables. You can check it by calling categorical and numerical function. 
count=clear(weather,'Weather','Cloudy')
print(count)
wind_speed_35_vis_25=instances_based_condition(weather,'Wind Spd (km/h)',35,'Visibility (km)',25)
print(wind_speed_35_vis_25)
agg_values_ina_month(weather,'Date/Time','Temp (C)','mean')

mean_weather=group_values(weather,'Weather','mean')
print(mean_weather)
convert(weather,'Temp (C)')




