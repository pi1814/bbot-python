def print_report(string_file_dict):
    print('...Start Report Printing...')
    for key, value in sorted(list(string_file_dict.items())):
        if key.isalpha():
            print(f"{key} has occured {value} times")
    print('...End Report Printing...')
        

file_contents = ''
word_count = float('-inf')
stringFile = ''
report = {}
with open('./books/frank.txt') as f:
    file_contents = f.read()
    stringFile = ''.join(file_contents.split())
    word_count = len(file_contents.split())

for letter in stringFile:
    if letter.lower() in report:
        report[letter.lower()] += 1
    else:
        report[letter.lower()] = 1


print_report(report)
