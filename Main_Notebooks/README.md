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

- The notebook `spatial_disease_model.ipynb` takes in the data and sparse matrices from `Attributes_sparse_matrices.ipynb`. It creates a matrix A: farm number by status (where status can be of S,E,I,V,R). This matrix contains random numbers drawn from distributions describing that farms specific infectious periods, recovery periods etc. 

- The matlab file `createInds` takes in the file all_Data (which you have to import first - double click from in matlab, and click on import selection). It saves three cells of vectors: row_ind, col_ind and data_Arr, which contain the indices of the farms within 10km of each other. If `parfor` doesn't work, the `par` can be removed, but will take approximately 20 minutes to run rather than 5 or so. By default, MATLAB used 4 workers on my laptop, but this could be increased to 8.

-The matlab file `createSparse` creates a sparse matrix from row_ind, col_ind and data_Arr, and so `createInds` needs to be run first. This will output a cell S which contains the sparse matrices for each attribute.

