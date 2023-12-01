from transformers import AutoTokenizer
import transformers
import pandas as pd
from tqdm import tqdm
import argparse
import warnings
import json
import logging

warnings.filterwarnings("ignore")
logging.disable(logging.WARNING)

# Load prompt template
prompt_file_path = 'prompt.txt'
with open(prompt_file_path, 'r') as file:
    prompt_template = file.read()

def build_prompt(system_prompt, user_message):
    if system_prompt is not None:
        SYS = f"[INST] <<SYS>>\n{system_prompt}\n<</SYS>>"
    else:
        SYS = ""
    CONVO = ""
    SYS = "<s>" + SYS
    CONVO += f"[INST] {user_message} [/INST]"
    return SYS + CONVO

def label_concern(input_list):

    # concate prompt with tweets
    prompt_list = []
    sys_prompt = prompt_template
    for user_message in input_list:
        prompt = build_prompt(sys_prompt, "tweet: "+user_message)
        prompt_list.append(prompt)

    print("loading model and tokenizer ...")
    model = "incas_tuned_model/"
    tokenizer = AutoTokenizer.from_pretrained(model, max_length=1024)
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        device_map="cpu",
        max_length=1024
    )

    print("inference result ...")
    predict_results = []
    for i in tqdm(range(len(prompt_list))):
        result = pipeline(prompt_list[i])
        predict_results.append(result[0]["generated_text"])

    return predict_results

if __name__ == "__main__":
    """
        Args:
            messages: list of dictionaries [{'id':xxx,'contentText':xxx,...},...]
            sampling_size: sampling size of each date, default: 1000
            feature_size: tfidf feature size, default: 1000
            min_range: min range of detection, default: 86400
            max_depth: max depth of change point tree, default: 3

        Returns:
            A dict whose keys are message IDs and values are lists of annotations.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="small_sample.jsonl")
    args = parser.parse_args()

    # only process Twitter data
    print("loading json file ...")
    df = pd.read_json(args.file, lines=True)
    # messages = [json.loads(line) for line in file]

    contentText_list = df["contentText"].tolist()
    id_list = df["id"].tolist()

    label_list = label_concern(contentText_list)

    print("annotating messages ...")
    annotations = {}
    for i in range(len(id_list)):
        annotation={}
        annotation["id"] = id_list[i]
        annotation["contentText"] = contentText_list[i]
        annotation["concern"] = label_list[i]
        annotation["providerName"] = "ta1-usc-isi"
        annotations["id"] = [annotation]

    with open('concern_annotate_{}.json'.format(file), 'w') as json_file:
        json_file.write(json.dumps(annotations))


