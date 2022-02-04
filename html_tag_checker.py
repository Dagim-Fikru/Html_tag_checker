"""
This program will check if an html file has the right order of tags.
"""

not_closable_tags = ["<area>", "<base>", "<br>", "<col>", "<!doctype>", "<embed>", "<hr>",
                     "<img>", "<input>", "<link>", "<meta>", "<param>", "<source>", "<track>", "<wbr>"]
while 1:
    print("Paste the location (absolute) of your html file")
    location = input("here :")
    try:
        file = open(location, 'r')
        html = file.read()
        break
    except:
        print("Invalid file location")
html = html.replace("<", ":|:|:<")
html = html.lower()
tagList = html.split(":|:|:")
valid = True
opend_tags = []
for tag in tagList:
    closing_tag = False
    if len(tag) > 0 and tag[0] == "<":
        if " " in tag and tag.index(" ") < tag.index(">"):
            tag = tag[:tag.index(" ")]
        else:
            tag = tag[:tag.index(">")]
        tag += ">"
        if "/" in tag:
            tag = "<"+tag[2:]
            closing_tag = True
        if tag not in not_closable_tags:
            if not closing_tag:
                tag_was_opened = False
                for opend_tag in opend_tags:
                    if opend_tag[0] == tag:
                        opend_tag[1] += 1
                        tag_was_opened = True
                        break
                if not tag_was_opened:
                    opend_tags.append([tag,1])
            else:
                tag_was_not_opened = True
                for opend_tag in opend_tags:
                    if opend_tag[0] == tag and opend_tag[1] > 0:
                        opend_tag[1] -= 1
                        tag_was_not_opened = False
                        break
                if tag_was_not_opened:
                    valid = False
                    print("</"+tag[1:] + " - this tag was not opend")
                    pass
for opend_tag in opend_tags:
    if opend_tag[1] > 0:
        valid = False
        print(opend_tag[0] + " - this tag is not closed")
if not valid:
    print("The html is INVALID")
else:
    print("The html is VALID")
