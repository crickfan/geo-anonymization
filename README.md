# geo-anonymization
geo location anonymization for IMAGEN project

1. Befor using the script, you will need:

  1.1 Get a Google API key. 
    You can apply one here: https://cloud.google.com/maps-platform/?apis=places
    Select "Places" on the prodect selection page. You will need to provide your bank details, but you won't be charged for the current project because the usage is tiny. Full pricing list is here: https://cloud.google.com/maps-platform/pricing/sheet/?_ga=2.114431171.555751564.1540810985-327939475.1540810985
    
Although the script relies on the other server (Nominatim, open street map) as a backup in case Google can not find geo-location, it provides much less coverage than Google. You will find many missing locations if you use Nominatim alone. 
  
  1.2 Make sure the file formatting is correct. 
    Open your file with a text editor instead of Excel for checking because Excel would render the display so you won't be able to use what the file really look like.
    Make sure ID are not quoted, addresses are quoted; two columns are separated by comma. Please refer to the sample_addresses.csv for formatting.
    
  1.3 Know the file encoding of your file. 
    You can open your file in Notepad++ and find the encoding information either on the right-bottom corner of the software, or by clickig "Encoding" button on the top banner.
    For west Europe Windows computers you will probably fine the encoding being ANSI, in this case please specify the fileEncoding as 'cp1252' for running the script.
    Other common encodings are 'utf-8' (for the 'sample_addresses.csv'), 'gb2312' (for Chinese, also 'gbk', 'gb18030). File will probably not be able to load into the script if wrong encoding info is provided.
    For a complete list of encoding please see:
    https://docs.python.org/3/library/codecs.html#standard-encodings
    


2. How to run the sample:

  2.1 Import the script and function
  
  Switch your working directory to where the anony.py script is. In the python console type and enter:
import anony
from anony import anony

  2.2 Type and enter:
  
  anony('sample_addresses.csv', 'utf-8', 'Germany', 'your google api key here')
  
  The script will run roughly 20 searches per second, if too slow it means that Nominatim server is used instead of Google, which is not a good sign. Results are in 'sample_addresses_anon.csv', which looks like:
  
  ,ID,lat,lon
1,12345,52.52,13.38
2,67890,52.51,13.37

  Don't worry it looks better in Excel. Please try this sample first before using it on your own file. 
  
3. Run the script for your own address file:

  3.1 If you are in west Europe, for your own file you can probably trying 'cp1252' as the encoding parameter first if you are not sure about encoding.
  3.2 The country is provided as an additional parameter, and will be appended to the addresses to ensure accurate location searching. If you already got country information in your file, you can put '' (blank string) in the parameter for country.

  
  
  
  
