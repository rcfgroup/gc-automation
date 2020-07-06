rem This example is different in that the steps are run through the python script using the command file and base.command file.
rem Below set the directories for the external script you want to use (e.g.  Python),  Input, Output and ancillary folders (e.g. Reports, Exported CSV Files).

set PYTHON=C:\temp\Example folders\3 Apply Match File\python_code_2.py
set IMG_DIR=C:\temp\Example folders\3 Apply Match File\Input
set MATCH_DIR=C:\temp\Example folders\3 Apply Match File\Exported Match Files
set REPORT_DIR=C:\temp\Example folders\3 Apply Match File\Reports
set EXPORT_DIR=C:\temp\Example folders\3 Apply Match File\Exported CSV Files
set OUTPUT_DIR=C:\temp\Example folders\3 Apply Match File\Output
set NO_MATCH_LOG=C:\temp\meowC:\temp\Example folders\3 Apply Match File\nomatch.csv

python "%PYTHON%" --image="%IMG_DIR%" --match="%MATCH_DIR%" --report="%REPORT_DIR%" --export="%EXPORT_DIR%" --output="%OUTPUT_DIR%" --nomatch="%NO_MATCH_LOG%"

rem Process finished
PAUSE