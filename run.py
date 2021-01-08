import csv, sys, jinja2
from template import html_content

# This function loads CSV to header and list_of_rows variables
def load_csv(filename):
    with open(filename + '.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        list_of_rows = []
        for rows in reader:
            list_of_rows.append(rows)
    return [header, list_of_rows]

# This is main function used to create HTML
def create_html(filenames=sys.argv, label="Total Assets", value="Percentage"):
    if len(filenames) < 2:
        return -1
    try:
        list_of_csv = []
        for args in filenames[1:]:
            # Getting the Header and Rows for each file
            the_csv = None
            the_csv = load_csv(args)
            list_of_csv.append(the_csv)
        # Getting Percentage and Labels
        index_of_label = the_csv[0].index(label)
        index_of_value = the_csv[0].index(value)
        label = []
        value = []
        for item in the_csv[1]:
            label.append(item[index_of_label])
            value.append(int(item[index_of_value]))
        # Working with jinja template
        template = jinja2.Template(html_content)
        return template.render(list_of_csv=list_of_csv, label=label, value=value)
    except:
        return -2

# Executing the function
print(create_html())
