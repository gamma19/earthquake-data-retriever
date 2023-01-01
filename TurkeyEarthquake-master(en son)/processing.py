import json
import re
import pandas as pd

with open('quakes_raw.json', 'r') as json_obj:
  json_data = json.loads(json_obj.read())

f = open("data\\danger_raw.txt", "a")


def danger_calc():
    for i in json_data:
        try:
            f.write(
                # Every magnitute increase by 1 means approx. 10 times bigger devastation.
                # Lower the earthquake's depth(km) means lower devastation.
                # Regular expression used for getting area data within paranthesis.
              re.search('\(([^)]+)', str(json_data[str(i)]['Region']).replace(" ", "")).group(1) +" " + str(round(((10 ** float(json_data[str(i)]['Magnitude'][2:5])) / float(json_data[str(i)]['Depth(km)'])), 2)) +"\n"
            )


        #Zero-Division Exception
        except:
            pass
    f.close()

danger_calc()


# Python program to convert text
# file to JSON

# the file to be converted
filename = 'data\\danger_raw.txt'

# resultant dictionary
dict1 = {}

# fields in the sample file
fields = ['city','dangerindex']

with open(filename) as fh:
    # count variable for employee id creation
    l = 1

    for line in fh:

        # reading line by line from the text file
        description = list(line.strip().split(None, 4))

        # for output see below
        #print(description)

        # for automatic creation of id for each employee
        sno = str(l)

        # loop variable
        i = 0
        # intermediate dictionary
        dict2 = {}
        while i < len(fields):
            # creating dictionary for each employee
            dict2[fields[i]] = description[i]
            i = i + 1

        # appending the record of each employee to
        # the main dictionary
        dict1[sno] = dict2
        l = l + 1

# creating json file
out_file = open("data\\citydanger.json", "w")
json.dump(dict1, out_file, indent=4)
out_file.close()

with open('data\\citydanger.json', 'r') as json_obj:
  json_danger = json.loads(json_obj.read())

  df2 = pd.DataFrame.from_dict(json_danger, orient="index")
  print(df2)

# Lambda function usage for type casting into float.
result = df2.groupby("city").agg(
   lambda x: x.astype(float).sum()
)
print(result)
print(str(result['dangerindex'].nlargest(n=15)))
m = open("data\\result.txt", "a")

m.write(str(result['dangerindex'].nlargest(n=15)))
m.close()