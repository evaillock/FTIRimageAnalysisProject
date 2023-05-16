# FTIRimageAnalysisProject
## Dependencies
Pandas <br>
Numpy<br>
Matplotlib.pyplot<br>
Seaborn<br>
jcamp<br>
pupchempy<br>
rdkit<br>
sklearn<br>
RDkit<br>
requests<br>
os<br>
glob<br>
shutil<br>
BeautifulSoup<br>

## Goals and Background
FTIR analysis is a common process in the identification of chemical compounds. FTIR analysis utilizes the relationship between a compounds interference with the IR spectrum at differing wavelengths. The nature of the interfereance (Measured in Absorbance or Transmittance) can reveal specifications about the chemical make up. Many functional groups can be identified by observing absorbance peaks at specific wavelengths, in addition the fingerprint region can be used to identify specific chemicals. <br>
FTIR analysis is typically done by hand and requires a trained technician with experience and access to refrences for FTIR wavelengths. Some machine based identification are available but require a database of FTIR spectra to compare the sample too. In this case it is impossible for the machine to make a prediction outside of the refrence samples in the database. For this reason it is considered to create a machine learning based approach that could allow quick identification of all functional groups for any spectra without requiring a refrence database or skilled technicians.<br>
In this project we have built a SVM model that shows strong predictive power for many functional groups

### Obtaining Our data
Our data was obtained from the NIST chemistry webbook via web scraping. <br>
The species.txt file was obtained from the NIST chemistry webbook page and turned into a csv file<br>
The file scrapeIR.py contains the function which searches the webbook by cas and obtains a FTIR jcamp if available<br>
The file scrapeSpeciesNIST.py is the script that was used to attempt a scrape for every item in the species list<br>
 - This script stores all of the files in a folder it creates called scrapedFTIR
 - it depends on having the scrapeIR.py file to pull the scrape function from<br>
theCheckAbsWavenumbers.py script sorts the obtained files into folders goodUnits and badUnits, good units are files that are already in absorbance and wavenumbers format<br>
checkX++Y.py is used to verify the files are in the right format for the xy datatables<br>

***cleaning and adding to data***
The Data organization, normalization and resampling and the Convert transmittance data jupyter notebooks are where the data is worked into our usuable state for modeling.<br>
We use a function created in the getInchi.py file and the function created in the smileFunctionalGroup.py file to obtain inchi keys and smiles codes for our data. <br>
The smiles codes are used in our notebook to obtain the classification values used for our model for each functional group
 - 1 indicates functional group is present
 - 0 indicates functional group is absent

In order to make the model we needed to organize the data so that each item has the same features. To do this we resampled to a common set of wavenumbers. This resampling was done from 550-3846 wavenumber (a common range found in the entire dataset) we then created new y values based on nearest two points interpolation method. <br>
Finally the absorbance values were normalized to a max peak height of 1, we now considered the data ready for modeling. 

### Building the model
We built seperate models for each functional group using SVM architecture from scikit learn. <br>
We looked at several data splitting techniques, the whole dataset split randomly, a strattified shuffle split, and a balanced minority and majority class dataset. The first two methods created a model that simply was picking the majority class most often, the balanced set contained many fewere false negatives however it did have a lower overall accuracy <br>

### Validating the model
We looked at the confusion matricies and several associated metrics after applying the model to the whole dataset. <br>
Accross the board accuracy and recall were high, however precision was generally low alhtough precision was still high in some models.<br>
We also looked at the coeficents and see that genearlly the heaviest weighted coeficents are at the expected wavenumbers when compared to the literature.<br>

The final metric we looked at for the model was a Tanimoto similarity between the set of actual functional gorups present and the set of predicted functional groups present. (ie, the model did not gain points for not predicting a functional group that was not present) here the model did ok, the average score was 0.56, and the maximum score was 1.00. While overall the score was not as high as we liked it did show potential for strong total predictive power. <br>

we only had one outside jcamp file usable for validation and this spectra was of bypyridine, a functional group we did not build the model to predict. If you consider the pyridine to be both an aromatic and a nitrile however our model was able to predicte it with a 1.00 tanimoto similarity. 

#### Looking at a non linear kernal
We took a quick look at using a radial kernal however the overall accuracy and metrics of the radial model were very similar to the linear model







