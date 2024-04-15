PLACEHOLDER = "[name]"
with open("input/letters/letter_template.txt") as template_file:
    template = template_file.read()

with open("input/names/invited_names.txt") as name_list:
    names = name_list.read().splitlines()
    for name in names:
        with open(f"output/ready-to-send/letter_for_{name}.txt", mode="w") as write_file:
            write_file.write(template.replace(PLACEHOLDER, name))
