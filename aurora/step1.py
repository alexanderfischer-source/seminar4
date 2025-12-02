import csv



def read_csv():
    content = []
    with open("secret_opps_dataset.csv", encoding='utf-8') as f:
        r = csv.DictReader(f)
        for i, row in enumerate(r):
                content.append(row)
                if i == 4:
                    break

     return content

def write_csv(rows):
    fieldnames = list(data[0].keys())
    with open(butput_path, "w", newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames):
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def parse_args():
    p = argparse.ArgumentParser(description='prit first [n]=4 lines from filename')

    p.add_argument('input_file', help='input_file')
    p.add_argument('output_file', help='output file')

    return p

def main():
    parser = parse_args()
    args = parser.parse_args()
    sample = read_csv("args.input_file")
    write_csv(sample, "args.output_file")

if __name__ == '__main__':
    main()
