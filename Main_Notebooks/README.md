Here we can update each other on what each file contains (a brief summary) to make it easier to find the appropriate notebook.

**Notebooks:**
- The imputed farms are in `imputed_farm.txt`. This contains all the attributes for the 85,112 farms. This includes: location, cow, ruminant, water, grazing, milk, equipment and FMD status.
- Imputations were made using KNN (which can be unreliable for high N). This is `farm_imputation_code.ipynb` notebook. **maybe we should look into this**
- The data provided to use (`completeData2.csv` - confidential, see emails) and data we imputed `imputed_farm.txt` is collected together saved as a data file `All_data`. This converts the log-lat coordinates into easting-northing coordinates (required when using the Jewells' distance kernel). This can be found in the `Attributes_sparse_matrices.ipynb` notebook. This notebook contains the functions required to collect indices corresponding to the non-negative values where farms share (farms within a 10km radius): 
    1. milk
    2. water
    3. grazing
    4. equipment
    5. vet
    6. contact with humans and animals
    
This can be used to create the sparse matrices ([Intro_sparse_matrices](https://cmdlinetips.com/2018/03/sparse-matrices-in-python-with-scipy/))

