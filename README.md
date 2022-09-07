# Xcelligence-Time-Course
This is to generate Time Course data from Xcelligence.

- To find the path where to put the folder:

    i. Click data (see left panel)

    ii. Right click " Reveal in File Explorer", this will open WIndows Explorer to locate that "data" folder.

- Move your NEW data that need to be analysed to that "data" folder

- You can select your file on left panel and click on "Copy Relative Path" to get full path.
  Please replace any \ with / and then Change Line number # 10 on the **"extract.py"** file to specify the new data source file.

- Open TERMINAL on VS Code, if that is not visible vlivk on "ctrl+`" to show the hidden TERMINAL.

- Install Virtual Environment on your machine in that TERMINAL.

    i. Run: `py -3 -m venv venv` 

    ii. If you are using **Windows**, run: `source venv/Scripts/activate` or if you are using **mac**, run: `source venv/bin/activate` to activate the Python virtual environment.

- Run: `python extract.py` to get output on "output/output_for_<Name_of_your_Source_File>.xlsx".
