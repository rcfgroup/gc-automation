rem Usage
rem Lines start with rem are comments and are safe to delete
rem This code will loop through all chromaotgrams (*.gci) under directory set in APP_IN and process each one
rem Please change paths below to corresponding directories
rem All chromaotgrams to be processed must be under the directory specified in APP_IN
rem No double quotes required for path variables below

rem set full path for GC Image CommandLine.bat file (change from C:\ onwards with own filepath if not the same)
set GC_IMG=C:\GC Image\GC Image 2.8r2 GCxGC (64-bit)\bin\CommandLine.bat

rem set where process method cmd file is located (change from C:\ onwards with own filepath if not the same)
set APP_PROC=C:\temp\Example folders\2 Export Match File\command file_automated export match file.cmd

rem set where chromaotgrams to be processed are located (change from C:\ onwards with own filepath if not the same)
set APP_IN=C:\temp\Example folders\2 Export Match File\Input

rem set where output chromaotgrams are going to be saved (change from C:\ onwards with own filepath if not the same)
set APP_OUT=C:\temp\Example folders\2 Export Match File\Output


rem In this section an external Python script has been integrated to automatically generate and export a match file
rem for each chromatogram in the Input folder.
rem Change the file paths from C:\ onwards with own filepath if not the same and change the Python file (.py) and template file as necessary.

set PYTHON_SCRIPT=C:\temp\Example folders\2 Export Match File\python_code.py
set TEMPLATE=C:\temp\Example folders\2 Export Match File\Alignment template file.bt
set REPORT_SOURCE=C:\temp\Example folders\2 Export Match File\Reports\Alignment Template Summary Reports_xml_files
set TEMPLATE_MATCH_DESTINATION=C:\temp\Example folders\2 Export Match File\Exported Match Files


rem save current working directory (do not change for the example)
set CURRENT_DIR=%cd%

rem switch into input directory (do not change for the example)
cd "%APP_IN%"

rem loop through each *.gci file and process it (do not change for the example)
for %%i in (*.gci) do "%GC_IMG%" -sysu -cmdFile "%APP_PROC%" -s "%APP_IN%\%%i" -d "%APP_OUT%\%%i" 2>&1 1>nul | more
python "%PYTHON_SCRIPT%" --template="%TEMPLATE%" --source="%REPORT_SOURCE%" --destination="%TEMPLATE_MATCH_DESTINATION%"

rem switch back to saved working directory (do not change for the example)
cd "%CURRENT_DIR%"
