# PLR-Net_torch_version
Official Pytorch Code base for "Extracting vectorized agricultural parcels from high-resolution satellite images using a Point-Line-Region interactive multi-task model"
# Training & Testing
The structure of the data file should be like:
/data 
|-- data
    |-- train
    |   |-- images
    |   |-- annotation.json
    |   |-- annotation-small.json
    |-- val
    |   |-- images
    |   |-- annotation.json
    |   |-- annotation-small.json
Training
Single GPU training
python scripts/train.py --config-file config-files/PLR-Net.yaml 
Testing
python scripts/test.py --config-file config-files/PLR-Net.yaml 
