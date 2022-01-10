print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.\n\n")
# ввод: копируем 3 столбца с координатами компонентов из pcb list
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    finally:
        if len(line) < 1:
            break
    # contents.append(float(line))  # разделитель точка
    contents.append(line)

print(contents)

# dist = contents[-1] - contents[0]
# dist = round(dist / (len(contents) - 1), 3)
# print(str(dist) + '\n\n\n')
#
# for x in range(len(contents)):
#     print(round(contents[0] + x * dist, 3))
