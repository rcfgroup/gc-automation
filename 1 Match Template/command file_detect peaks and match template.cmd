rem Usage
rem Lines start with rem are comments and are safe to delete
rem Please change paths below to corresponding directories
rem These include configuration file path under 'Configure' and template file path under 'Template  File'
rem All chromatograms to be processed must be under the directory specified in APP_IN
rem No double quotes required for path variables below

rem This 'Configure' command tells the software which configuration file (settings) you want it to use (e.g. minimum peak, SNR)
-Configure C:\temp\Example folders\1 Match Template\configuration file 1.cfg
-script <script>

rem This command tells the software to detect peaks (detect 'blobs')
<cmd name="cmdBlobDetection" label="Blob Detection">
<timeStamp>11 March, 2019 9:34:0</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
</do>
</cmd>

rem This command tells the software to match Template file 1 to against the peaks detected.
rem In the first parameter id the template file is specified.
<cmd name="methodCmdMatchTemplate" label="Match Template">
<timeStamp>11 March, 2019 9:39:49</timeStamp>
<userName>localuser</userName>
<cmdversion>2.8.2</cmdversion>
<do>
<parameter id = "filename" label = "Template File">C:\temp\Example folders\1 Match Template\Template file 1.bt</parameter>
<parameter id = "updateCount" label = "Transform Updates before Applying">0</parameter>
<parameter id = "matchType" label = "Match Type">default</parameter>
<parameter id = "blobSet" label = "Match Set"></parameter>
</do>
</cmd>
</script>