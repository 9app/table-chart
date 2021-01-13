import csv, sys, jinja2
import matplotlib.pyplot as plt

# This function loads CSV to header and list_of_rows variables
def load_csv(filename):
    with open(filename + '.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        list_of_rows = []
        for rows in reader:
            list_of_rows.append(rows)
    return [header, list_of_rows]

def get_chunks(filenames, label, value):
    if len(filenames) < 2:
        return -1
    list_of_csv = []
    labels = []
    values = []
    for index, args in enumerate(filenames[1:]):
        # Getting the Header and Rows for each file
        the_csv = None
        the_csv = load_csv(args)
        list_of_csv.append(the_csv)
        # Getting Percentage and Labels
        index_of_label = the_csv[0].index(label)
        index_of_value = the_csv[0].index(value)
        labels_ = []
        values_ = []
        for item in the_csv[1]:
            labels_.append(item[index_of_label])
            values_.append(int(item[index_of_value]))
        labels.append(labels_)
        values.append(values_)
    charts = create_chart(labels, values)
    return [list_of_csv, charts]

def create_chart(labels, values):
    color_list = [
                    "#5ac18e","#40e0d0","#8b0000","#ff4040","#333333","#444d56",
                    "#e6e6ea","#fed766","#f4b6c2","#6497b1","#4b86b4","#fe9c8f",
                    "#e5edf1","#87cefa","#aec9eb","#efc5b5","#e1d590","#d3b683",
                    "#e5ccbd","#d2bfc4","#ccfd7f","#b7d24b","#befd73","#64bfa4",
                    "#bf77f6"]
    image_names = []
    for index, label in enumerate(labels):
        plt.figure(figsize=(5,5))
        plt.pie(values[index], labels=label, autopct="%.1f%%", colors=color_list[:len(label)])
        image_name = "attachment-" + str(index+1) + ".png"
        plt.savefig(image_name)
        image_names.append(image_name)
    return image_names


# This is main function used to create HTML
def create_html(filenames, label, value):
    with open('template.html', 'r') as f:
        html_content = f.read()
    template = jinja2.Template(html_content)
    chunks = get_chunks(filenames, label, value)
    list_of_csv = chunks[0]
    charts = chunks[1]
    return template.render(list_of_csv=list_of_csv, charts=charts)

# Edit this according to your CSV file.
print(create_html(filenames=sys.argv, label="Total Assets", value="Percentage"))