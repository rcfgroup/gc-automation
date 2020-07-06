rem Usage
rem Lines start with rem are comments and are safe to delete
rem This code will loop through all chromatograms (*.gci) under directory set in APP_IN and process each one
rem Please change paths below to corresponding directories
rem All chromatograms to be processed must be under the directory specified in APP_IN
rem No double quotes required for path variables below

rem set full path for GC Image CommandLine.bat file (change from C:\ onwards with own filepath if not the same)
set GC_IMG=C:\GC Image\GC Image 2.8r2 GCxGC (64-bit)\bin\CommandLine.bat

rem set where process method cmd file is located (change from C:\ onwards with own filepath if not the same)
set APP_PROC=C:\temp\Example folders\1 Match Template\command file_detect peaks and match template.cmd

rem set where chromatograms to be processed are located (change from C:\ onwards with own filepath if not the same)
set APP_IN=C:\temp\Example folders\1 Match Template\Input

rem set where processed chromatograms are going to be saved (change from C:\ onwards with own filepath if not the same)
set APP_OUT=C:\temp\Example folders\1 Match Template\Output




rem save current working directory (do not change)
set CURRENT_DIR=%cd%

rem switch into input directory (do not change)
cd "%APP_IN%"

rem loop through each *.gci file and process it (do not change)
for %%i in (*.gci) do "%GC_IMG%" -sysu -cmdFile "%APP_PROC%" -s "%APP_IN%\%%i" -d "%APP_OUT%\%%i" 2>&1 1>nul | more >> "C:\temp\Example folders\1 Match Template\log.txt"

rem switch back to saved working directory (do not change)
cd "%CURRENT_DIR%"
