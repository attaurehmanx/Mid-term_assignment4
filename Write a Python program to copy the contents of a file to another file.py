file1=input("enter file whose content you want to copy another file:")
file2=input("enter file where the copied content is placed:")
with open (file1) as f:
    with open (file2, 'w') as f1:
        for line in f:
            f1.write(line)

        