# Code for PalMod Transient 
This repository contains code I used for the PalMod transient experiment.

## `forcings_Palmod_transient`
### Description
This folder has a notebook which can be used to generate yearly forcing data
from pre-defined tables. Ideally it would also generate the tables from
scratch; but that isn't in there yet. It creates the file
`PalMod_Transient_Forcing_Table.csv` which can be used with the `esm-tools`
runscripts for a transient experiment starting at 21ka BP, which corresponds to
the model calendar year of 1850.

### TODO
+ [ ] A header/comment line with some info
+ [ ] A "build", which can recreate the file from scratch.
