import io
import pandas as pd
import stopwords as sw

def main():
    file = open("16k_neprocesat.txt", "r")

    raw_content = file.readlines()
    new_output = []

    raw_content.pop(0)

    for line in raw_content:
        result = line.split(',', 1)
        new_output.append((result[0], sw.elim_sw(result[1].replace('\n', ''))))

    output = pd.DataFrame(new_output, columns=['offensive', 'text'])
    output.to_csv('training_data.csv', index=False)
