# gc-automation

To help users with the basics of running their workflow steps through the command line interface, we recommend running the example scripts in the example folders. These instructions and examples allow the user to become familiar with the format and check for errors before moving onto more complex custom tasks.

## Before you begin

The commercial and free and open-source software (FOSS) for your own custom workflow would already be installed. However, for this specific example, the following steps should be followed to ensure the example folders work as described.

### Prerequisite
- Python 3.6+
- Python packages:
	- pandas
	- click
- Commercial software:
	- GC Image (see below)
	- GC Image plugin: Natural Neighbour (NIES-EPFL) (see below)

### Installing commercial software

Ensure a copy of the commercial software (in this instance GC Image) is installed (the examples were generated in version 2.8r2). A free trial of the software is available on request from [https://gcimage.com/gcxgc/trial.html](https://gcimage.com/gcxgc/trial.html)

### Installing plug-ins

The examples describe interfacing a published alignment algorithm<sup>[1]</sup>. This algorithm is freely available as a plug-in at [http://gcimage.com/forum/viewtopic.php?f=5&t=104](http://gcimage.com/forum/viewtopic.php?f=5&t=104) via the website under Plug-ins and must be installed in order for the second and third example folders to work. To access the plug-in, login to your (free) user account. The original Matlab tool is available at [https://github.com/jsarey/GCxGC-alignment](https://github.com/jsarey/GCxGC-alignment). Once the plug-in file has been downloaded and extracted to the GC Image program folder, open GC Image, go to **Tools** in the menu bar and from the list select **Manage Plugins**. Click the **Import** button and locate and import the plug-in file. The **Natural Neighbour (NIES-EPFL)** plug-in should now appear in the list of imported plug-ins. Click **Configure** and change the parameters to match those below. Click **OK** and close the program.


## Quick start

1. Clone this repository to your local computer or [download](https://github.com/rcfgroup/gc-automation/archive/master.zip) this repository as a zip archive and extract.
2. Install GC Image and Natural Neighbour (NIES-EPFL) plugin.
3. Install Python 3.6+, you can find downloads and installation documentations at [https://www.python.org/](https://www.python.org/)
4. Run `pip install pandas click` in commandline.

This repository contains three folders: 
- 1 Match Template
- 2 Export Match File
- 3 Apply Match File. 

These three folders are examples to help a beginner become familiar with the concept of using the command line interface to integrate free and open-source software with commercial software for GC×GC data processing. The examples in the folders wouldn’t necessarily be used independently as part of a workflow but effectively demonstrate this new way of being able to process GCxGC data.

Please note, if using a different version of the commercial software (not v2.8r2), you may need to change the path for the Command Line. In the first and second example folders, this can be changed in the batch (.bat) file. In the third example folder, this can be changed in the python (.py) file (line 41, keeping the double slash formatting). The command line interface can be found in the program directory. An example path is: C:\GC Image\GC Image 2.8r2 GCxGC (64-bit)\bin\CommandLine.bat.

Edit the .bat file in the first or second example folder, or the .py file for the third example folder. In the .bat file, change the value of `GC_IMG`, or in the .py file, change the value of `cmd` to match your GC Image CommandLine.bat path.

## FAQs
#### An error message says: "Software version is older than image version, open image may cause error!"

This is because you are running an GC Image version different from the one used to generate the example image. It is safe to click **OK** to ignore this message and continue.


