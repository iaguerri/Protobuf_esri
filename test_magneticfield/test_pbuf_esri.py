import unittest
from magneticfield.pbuf_esri import Protobuf
import pandas as pd


class Test_Protobuf(unittest.TestCase):
        
    def test_check_pd_type(self):
        #This function will check that the input is a pandas dataframe
        self.assertIsInstace(df, pd.Dataframe)
        
    def test_relevant_data_linear_interpolation(self):
        #This function will check that the fields t,x,y are position and timestamp in dataframe
        column_names_list = ["t","x","y"]
        self.assertTrue(df.columns in column_names_list)

    def test_magnetic_field_amplitude(self):
        #Check that magnetic column array's shape is 3 (magx, magy and magz).
        mag = df['magnetic'].shape[0]
        self.assertEqual(mag, 3)

        #The rest of the functions will be described in the README.md but I was not able to develop them
    
    

