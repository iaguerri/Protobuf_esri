# :beginner: Product Engineer Test

This README is the document which will explain the **Technical Assignment for the Product Engineer Test**. 
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


## **Structure of the Project:**

### :raising_hand: **Name** 
Protocol buffers TDD

### :baby: **Status**
This is the first release of the project. In future times it will be modified and changed as needs from the developers and the customer needs.

### :computer: **Technology stack**
In this case, the technologies used are based on Python.

- :rotating_light: The library chosen to develop the test is `Unittest` which is included in the Python package.
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


## :nut_and_bolt: **Deployment**
### :key: Prerequisites
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
Following this architecture, the main file where the code must be developed is the one located in `magneticfield/pbuf_esri`.

And the tests will be designed in the file `test_magneticfield/test_pbuf_esri.py`

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
            ├── 10742.pb
```
## :notebook_with_decorative_cover: **Software architecture**
The functions that I have developed are intended to meet the following requirements.

***1.1*** Check that the dataframe where the information will be upload is a `pandas.DataFrame`

***1.2***  To check the relevant data stored in the dataframe and if it has the variables needed for the interpolation algorithm.

***1.3***  We know that the `magnetic` column has the information in an array of the vectors (x,y,z). This function checks that the vector shape has the three parts in the array.

Even though, I know that there are some tasks that with this code could not be evaluated.
My script would have these functions.

:arrow_heading_down: *Test the compilation of the protocol buffer files*.

:arrow_heading_down: *Test the execution of the different formulas*.

:arrow_heading_down: *Test the value of the data recorded and if it is valid for the tasks to do.*

:arrow_heading_down: *Test that the **heatmap** show correctly the magnetic field*.




## :shit: **Technical hurdles**
The technical hurdles that I have had to face where the following:

1. Even it was not my assignment, in first place I wanted to look up the files and try to do the code in order to understand the task given to the developer and try to design the best architecture for her/him. Finally, I could understand how the `.proto` files worked but I was not be able to open the dataset.

    After research, I could figure out the next information:

    :white_check_mark: The structure of the `.proto` indicates that the main file is  `recordings.proto`, where the rest of the metadata files are called (rest of the `.proto` files). 

    :white_check_mark: When you import in the main file the `message` you import the metadata, in our case it would be the arrays' names or the columns name of the DataFrame.

2. Also, the TDD approach is a good technique to learn how to develop correctly Python code. My main problem here was to think about what requirements I needed for the definition of the functions.

I tried to design a Python TDD architecture trying to understand how it works. That is why I decided to have this software architecture.




### :shit: **ToDo**
1. Automatize the protocol buffers compilation and develop the rest of the code needed to fulfill the tasks.
2. Improve the functions defined in the test and refactor them with the real code in order to finish the code.

### :wrench: Developer Warnings
For the developer:
- :heavy_exclamation_mark: The directory should be `/Protobuf_esri/`
- :heavy_exclamation_mark: Libraries are in the file `requirements.txt`
- :heavy_exclamation_mark: In the `pbuf_esri.py`remember to import the module `Record` from `recordings_pb2.py`in order to get the whole structure of the future dataset


### :love_letter: **Contact info**
This project was developed by Irene Aguerri.

https://linkedin.com/in/ireneaguerri

If you have any doubts or comments, please refer to my email

:inbox_tray: ireneaguerri@gmail.com

---

