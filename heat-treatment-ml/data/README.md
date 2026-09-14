# Data

## Primary dataset

The project uses a 51-observation AISI-SAE 4340 subset associated with Penha (2010), covering tempering temperatures from 100–700 °C and tempering times from 10–86,400 s.

The model-ready processed file is:

`processed/4340_Penha2010_processed.csv`

It contains the variables required for the analysis: source, steel type, tempering temperature, tempering time, time in hours, log10(time), and final hardness.

## Original source

The broader dataset is **Tempering data for carbon and low alloy steels**, assembled by Raiipa Technologies from metallurgical literature including Hollomon (1945), Grange (1956), and Penha (2010).

Source: https://www.kaggle.com/datasets/rgerschtzsauer/tempering-data-for-carbon-and-low-alloy-steels

The Kaggle dataset is listed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. Attribution should be retained when redistributing source-derived data.

The full raw dataset is not duplicated in this project directory; the repository contains the model-ready 4340 subset used for the analysis.
