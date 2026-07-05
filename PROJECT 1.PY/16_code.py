with open("PROJECT 1.PY/poem.txt")as f:
 content=f.read()
if("twinkle" in content):
    print("the word twinkle is pesent in the content")
else:
    print("the word twinkle is not present in the content")

    f.close()