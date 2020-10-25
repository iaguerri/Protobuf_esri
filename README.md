# Product Engineer Test README file
This README is the document which will explain the Technical Assignment for the Product Engineer Test. 
The aim for this test is to design a Python architecture following the rules dicted by the *Python Test Driven Development framework* in order to create a ready-to-go environment so this framework could be reused as many times as needed. 
The task given for the developer are the following ones:
- Read the .proto files
- Define the pandas dataframe with the loading of the binary data allocated in the recordings files (.pb)
- Design the dataframe, with all the relevant data needed for the analysis
- Compute the position of each measurement point (Pn) by linear interpolation
    - xpn = (tpn - t0)/(t1-t0) * (x1 - x0) + x0
    - ypn = (tpn - t0)/(t1-t0) * (y1 - y0) + y0
- Compute the magnetic field amplitude
    - mag = (magx^2 + magy^2 + magz^2)^0.5
- Compute the average magnetic field amplitude in each map grid. The grid is a rectangle with size of 5m start from the position (0,0)
- Visualize the (grid) magnetic field strength heatmap.


![Image](https://www.esri.com/content/dam/esrisites/en-us/media/landingpages/g805553-arcgis-indoors-product-page-updates/indoors-main-banner-device-fg.png)

---


## **Structure:**

### :raising_hand: **Name** 
Protocol buffers TDD

### :baby: **Status**
This is the first release of the project. In future times it will be modified and changed as needs from the designer.

### :computer: **Technology stack**
In this case, the technologies used are based on Python.

- :rotating_light: The library chosen to develop the test is `Unittest` that is included in the Python package.
- :bar_chart: The libraries included are the ones needed for spatial analysis: Pandas and Numpy, Matplotlib.
- Also, the libraries needed to process the binary data from Protocol buffers (Google).
- The system is standalone.


### :boom: **Core technical concepts and inspiration**
The archicture developed is designed following the principles of TDD. This approach is a process that can be defined as:
1. Write a failing unit test
2. Make the unit test pass
3. Refactor the test

![Image](https://cdn-media-1.freecodecamp.org/images/1*FZGakHQbCUMAyDinf-KBiw.png)

The TDD approach reduces the amount of time spent in the test after the code is developed because the functions written must pass the tests that we have designed before.

## :wrench: **Deployment**
### Prerequisites
1. To have installed `conda`
2. To have installed `git`

### :one: Installation instructions
The installation process is the next:
  1. Download this repository
  2. Execute in the terminal
        `bash Environments.bash`
    This will do the next tasks:
        - It will create and activate a `conda environment` called `py37`
        - It will install `Python 3.7`
        - It will install the libraries listed in the file `requirements.txt`
        - It will execute the script `test_pbuf_esri.py`
  

### :file_folder: **Folder structure**
The folder is structured as TDD python architecture.
This architecture indicates that the test will be name with `test`+ foldername.


```
└── Protobuf_esri
    ├── .gitignore
    ├── requirements.txt
    ├── Environment.bash
    ├── README.md
    ├── magnetic_field
    │   ├── pbuf_esri.py
    ├── test_magnetic_field
    │   ├── test_pbuf_esri.py
    └── rawdata
        ├── locatorevents.proto
        ├── positions.proto
        ├── sensors.proto
        ├── recordings.proto
        ├── structures.proto
        ├── build
            ├── locatorevents_pb2.py
            ├── positions_pb2.py
            ├── sensors_pb2.py
            ├── recordings_pb2.py
            ├── structures_pb2.py
        ├── recordings
            ├── 10732.pb
            ├── 10740.pb
            ├── sensors_pb2.py
```


## :shit: **Technical hurdles **
The technical hurdles that I have had to face where the following:

1. Even it was not my assignment, in first place I wanted to look up the files and try to do the code in order to understand the task given to the developer and try to design the best architecture for her/him. Finally, I could understand how the `.proto` files worked but I could not be able to open the dataset.

:white_check_mark: The structure of the `.proto` indicates that the main file is `recordings.proto`, where the rest of the metadata files are called (rest of the `.proto` files)

T

2. The functions that I have developed are intended to meet the following requirements
    2.1 

### :wrench: **Developer Warnings**
For developer:
    :heavy_exclamation_mark: The directory should be `/
-directorio Protobuf_esri,
- 
-cuando ejecute el 3d que plot.show()
include the file where the metadata of the protocol buffers is (recordings_pb2)
- the libraries are in requirements.txt

### :shit: **ToDo**
- Get all the functions to develop all the tasks: automatize the protocol buffers compilation and develop the rest code




### :love_letter: **Contact info**
Getting help, getting involved, hire me please.
mail: ireneaguerri@gmail.com

---

