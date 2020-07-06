rem This is the command file. In this file we've entered the steps we want performing as if it was being performed on a single file.
rem The Python script looks between this command file and the base.command file which contains generic terms for the files we want to change
rem such as the Match File being used in the Gros et al local alignment step.

-Configure C:\temp\Example folders\3 Apply Match File\configuration file 1.cfg
-script <script>

rem This command contains the Gros et al local alignment algorithm as a plug-in under parameter id 'transOpType'.
<cmd name="methodCmdRegisterImage" label="Register Image">
<timeStamp>24 September, 2019 10:10:50</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
<parameter id = "workflowType" label = "Workflow Type">MANUAL_MATCH</parameter>
<parameter id = "transOpType" label = "Transform Operation Type">PLUGIN.Natural Neighbor Transform (NIES-EPFL)</parameter>
<parameter id = "templatePath" label = "Template File Path"></parameter>
<parameter id = "matchParam" label = "Match Parameters">FileType=&gt;CSV_ALIGNMENT_POINT_0;File=&gt;C:\temp\Example folders\3 Apply Match File\Exported Match Files\180815 9 alkane aromatic mix_Template_Match.csv</parameter>
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
<parameter id = "path" label = "Destination Folder">C:\temp\Example folders\3 Apply Match File\Exported CSV Files</parameter>
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
<parameter id = "filename" label = "Report Path">C:\temp\Example folders\3 Apply Match File\Reports\summary</parameter>
<parameter id = "params" label = "Default Settings"></parameter>
<parameter id = "templatePath" label = "Report Configuration">C:\temp\Example folders\3 Apply Match File\Summary report configuration file 2.rtcf</parameter>
<parameter id = "append" label = "Append">false</parameter>
</do>
</cmd>
</script>