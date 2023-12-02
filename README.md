# incas-phase2-concern

## How to build project

* Then download model files from [here](https://drive.google.com/drive/folders/1PNVDQPPMuQuaMDG7hvwUW64W15A4fCuC?usp=sharing). Please keep file 'annotate.py' and the folder `incas_tuned_model` in the same directory.

The directory should look like this:

````
incas-phase2-concern
├── incas_tuned_model --place models here
├── Readme.md
├── annotate.py
├── requirements.txt
└── prompt.txt

````
## How to run
```
pip install -r requirements.txt
python annotate.py --file your_file_name
```

The input file parameter is a single dictionary file.

The return value is a dictionary whose keys are message IDs and values are lists of DARPA-defined annotation instances.
