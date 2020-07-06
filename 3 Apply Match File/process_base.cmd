rem You can see in this base.command file, the specific match file detailed in the command file (180815 9 alkane aromatic mix_Template_Match.csv)
rem has been replaced for a generic tag $$MATCH_FILE$$. This links the commercial software with the Python script, where the Python script
rem automatically looks for the Match File (in the Exported Match Files folder) with the same batch number (e.g. 180815 9) and use it to align
rem any chromatograms (in the Input) folder using the Gros et al local alignment algorithm (in the list of commands below).

-Configure C:\temp\Example folders\3 Apply Match File\configuration file 1.cfg
-script <script>

rem rem This command contains the Gros et al local alignment algorithm as a plug-in under parameter id 'transOpType'.
<cmd name="methodCmdRegisterImage" label="Register Image">
<timeStamp>24 September, 2019 10:10:50</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
<parameter id = "workflowType" label = "Workflow Type">MANUAL_MATCH</parameter>
<parameter id = "transOpType" label = "Transform Operation Type">PLUGIN.Natural Neighbor Transform (NIES-EPFL)</parameter>
<parameter id = "templatePath" label = "Template File Path"></parameter>
<parameter id = "matchParam" label = "Match Parameters">FileType=&gt;CSV_ALIGNMENT_POINT_0;File=&gt;$$MATCH_FILE$$</parameter>
<parameter id = "transParam" label = "Transform Parameters"></parameter>
<parameter id = "interpType" label = "Interpolation Type">BILINEAR</parameter>
</do>
</cmd>
<cmd name="cmdBlobDetection" label="Blob Detection">
<timeStamp>11 March, 2019 9:34:0</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
</do>
</cmd>
<cmd name="methodCmdMatchTemplate" label="Match Template">
<timeStamp>11 March, 2019 9:39:49</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
<parameter id = "filename" label = "Template File">C:\temp\Example folders\3 Apply Match File\Template file 1.bt</parameter>
<parameter id = "updateCount" label = "Transform Updates before Applying">0</parameter>
<parameter id = "matchType" label = "Match Type">default</parameter>
<parameter id = "blobSet" label = "Match Set"></parameter>
</do>
</cmd>
<cmd name="methodCmdExportTICImageAsCSV" label="Export TIC as CSV">
<timeStamp>11 March, 2019 9:39:49</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
<parameter id = "path" label = "Destination Folder">$$EXPORT_DIR$$</parameter>
<parameter id = "filename" label = "File Name Format">filename.increment</parameter>
<parameter id = "type" label = "Data Format">1-D</parameter>
</do>
</cmd>
<cmd name="methodCmdSaveSummaryReport" label="Save Summary Report">
<timeStamp>11 March, 2019 9:39:49</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
<parameter id = "destType" label = "Report Path Type">Absolute</parameter>
<parameter id = "filename" label = "Report Path">$$REPORT_DIR$$\summary</parameter>
<parameter id = "params" label = "Default Settings"></parameter>
<parameter id = "templatePath" label = "Report Configuration">C:\temp\Example folders\3 Apply Match File\Summary report configuration file 2.rtcf</parameter>
<parameter id = "append" label = "Append">false</parameter>
</do>
</cmd>
</script>