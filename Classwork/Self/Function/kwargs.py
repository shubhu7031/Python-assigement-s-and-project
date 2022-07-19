from unicodedata import name


def pratik(**keval):
    for k, v in keval.items():
        print(f"the {k} is {v}")



pratik(name="Shubham",age="21")

