#Import libraries
from subprocess import check_call
import google.protobuf
from read_protobuf import read_protobuf
import recordings_pb2 as recordings_pb2
import pandas as pd
import matplotlib

class Protobuf:
    #Before the start of writting the code, you should compile the proto files in order to
    #have the files ready for coding.
    
    def check_pd_type():
        #We can upload the data using read-protobuf. I will show how I will do it but I wasn't a
        record = recordings_pb2.Recording() 
        fields = record.DESCRIPTOR.fields_by_name.keys()
        df = read_protobuf(['10732.pb', '10740.pb','10742.pb'], Record)
        return df
        
    def relevant_data_linear_interpolation():
        #Do the code. 
        #column_names_list = ["t","x","y"]
        return
   
    def magnetic_field_amplitude():
        #mag = df['magnetic'].shape[0]
        return
