def clean_courses(text):
    courses=[]
    for part in text.split(","):
        label=part.strip().lower()
        if label:
            courses.append(label)
    return courses
print(clean_courses("Pyhton,Java,pyhton"))
