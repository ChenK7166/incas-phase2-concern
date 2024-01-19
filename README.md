# incas-phase2-concern

## How to build project

* Then download model files from [here](https://drive.google.com/drive/folders/1zHIxTBD9fcuhva723TjOYNz0qUqok26p?usp=sharing). Please keep file 'annotate.py' and the folder `incas_tuned_model` in the same directory.

The directory should look like this:

````
incas-phase2-concern
├── incas_tuned_model --place models here
├── Readme.md
├── annotate.py
├── requirements.txt
├── small_sample.jsonl
└── prompt_inference.txt

````
## How to run
```
# Install torch
CPU: pip3 install torch torchvision torchaudio
GPU: pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install other lib
pip install -r requirements.txt

# Run concern model
python annotate.py --file your_file_name
```

The input file parameter is a single dictionary file.

The return value is a dictionary whose keys are message IDs and values are lists of DARPA-defined annotation instances.

## Example
```
python annotate.py --file small_sample.jsonl
```

input:
```
{{"id": "84c8aad06b52235727a1e4f957c7a78f7a023c0d", "contentText": "@_miggypot29 I \u2764 EDCA\u270c"}
```

output:
```
{"concern": {"Concern/US Military": 1, "Concern/International Relations": 0, "Concern/Domestic Political Issues": 0, "Concern/Defense and Military": 0, "Concern/Insurgent Threats": 0, "Concern/Social and Economic Issues": 0, "Concern/Public Services": 0, "Concern/Environmental Issues": 0, "Concern/Energy": 0, "Concern/Labor and Migration": 0, "Concern/Crime": 0, "Concern/NoneOther": 0}}
```

