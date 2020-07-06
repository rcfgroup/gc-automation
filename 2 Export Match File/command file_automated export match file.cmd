rem See example 1 (Match Template folder) for overview of command file contents.

-Configure C:\temp\Example folders\2 Export Match File\configuration file 2.cfg
-script <script>
<cmd name="methodCmdMatchTemplate" label="Match Template">
<timeStamp>11 March, 2019 9:39:49</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
<parameter id = "filename" label = "Template File">C:\temp\Example folders\2 Export Match File\Alignment template file.bt</parameter>
<parameter id = "updateCount" label = "Transform Updates before Applying">0</parameter>
<parameter id = "matchType" label = "Match Type">default</parameter>
<parameter id = "blobSet" label = "Match Set"></parameter>
</do>
</cmd>

rem This command generates a Summary Report based on the summary report configuration you want to use speicified in parameter id 'templatePath'.
<cmd name="methodCmdSaveSummaryReport" label="Save Summary Report">
<timeStamp>11 March, 2019 9:39:49</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
<parameter id = "destType" label = "Report Path Type">Absolute</parameter>
<parameter id = "filename" label = "Report Path">C:\temp\Example folders\2 Export Match File\Reports\Alignment Template Summary Reports</parameter>
<parameter id = "params" label = "Default Settings"></parameter>
<parameter id = "templatePath" label = "Report Configuration">C:\temp\Example folders\2 Export Match File\Summary report configuration file.rtcf</parameter>
<parameter id = "append" label = "Append">false</parameter>
</do>
</cmd>
</script>