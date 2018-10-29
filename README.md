# geo-anonymization
geo location anonymization for IMAGEN project

Befor using the script, you will need:

  1. Get a Google API key. 
    You can apply one here: https://cloud.google.com/maps-platform/?apis=places
    Select "Places" on the prodect selection page. You will need to provide your bank details, but you won't be charged for the current project because the usage is tiny. Full pricing list is here: https://cloud.google.com/maps-platform/pricing/sheet/?_ga=2.114431171.555751564.1540810985-327939475.1540810985
    
    Although the script relies on the other server (Nominatim, open street map) as a backup in case Google can not find geo-location, it provides much less coverage than Google. You will find many missing locations if you use Nominatim alone. 
  
  2. Make sure the file formatting is correct. 
    Open your file with a text editor instead of Excel for checking because Excel would render the display so you won't be able to use what the file really look like.
    Make sure ID are not quoted, addresses are quoted; two columns are separated by comma. Please refer to the sample_addresses.csv for formatting.
    
  3. Know the file encoding of your file. 
    You can open your file in Notepad++ and find the encoding information either on the right-bottom corner of the software, or by clickig "Encoding" button on the top banner.
    For west Europe Windows computers the encoding is probably ANSI, in this case please specify the fileEncoding as 'cp1252' for running script. Other common encodings are 'utf-8' (for the 'sample_addresses.csv'), 'gb2312' (for Chinese). File will not be able to load if wrong encoding info is provided.



How to run the script:
