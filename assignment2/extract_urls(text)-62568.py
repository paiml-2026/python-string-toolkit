def extract_urls(text):
    url=""
    word=text.split()
    for i in word:
        if i[0:7]=="http://" or i[0:8]=="https://":
            if url=="":
                url=i
            else:
                url=url+" ,"+i
    return url
text=input("Enter any text which contains url")
if extract_urls(text)=="":
    print("No Url Found!!")
else:
    print(extract_urls(text))

