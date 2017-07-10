import os,json,shutil,uuid

file_name = "restaurant.json" # Give the file name
dir = os.path.dirname(__file__)
file = os.path.join(dir,file_name)
filenew = os.path.join(dir,'out')

if not os.path.exists(filenew):
    os.makedirs(filenew)
else: 
    shutil.rmtree(filenew)
    os.makedirs(filenew)

with open(file) as data_file: 
   data = json.load(data_file) 



print("Original Json:\n"+json.dumps(data,indent=4,sort_keys=True))



def normaliser(y):
    """
    Flatens json and write in multiple files
    """

    foo = {}
   # normaliser function
    def normaliser_wrap(x,key='',ids=0):
        if type(x) is dict:
            out = {}
            outer = []
            for a in x:
                if (type(x[a]) is dict):
                    normaliser_wrap(x[a],key+"_"+a,ids=str(uuid.uuid4()))
                elif (type(x[a]) is list):
                    normaliser_wrap(x[a],key+"_"+a,ids=str(uuid.uuid4()))
                else:
                    if ids != 0:
                        out["id"] = ids
                    out[a] = x[a]

            outer.append(out)
            if bool(out):
                foo[key] = outer
        elif type(x) is list:
            for a in x: 
                normaliser_wrap(a,key,ids=str(uuid.uuid4()))
        else:
            print("You have an error")
        
    normaliser_wrap(y)

    
    print("Original Json:\n"+json.dumps(foo,indent=4,sort_keys=True))
    if bool(foo):
        for p in foo:
            with open("out/"+p+".json","w") as outfile:
                json.dump(foo[p],outfile)
          

normaliser(data)

# def normaliser(y):
    # """
    # def normaliser_wrap(x,key=''):
        # if type(x) is dict: 
            # out = {}
            # for a in x:
                # # with open(a+ "_","w") as outfile:
                    # # json.dump(x[a],outfile)
                # if x[a] is dict or x[a] is list:
                    # normaliser_wrap(x[a],key=a)
                # else: 
                    # out[a] = x[a]
        # elif type(x) is list:
            # for a in x:
                # normaliser_wrap(a)
        # else:
            

    # normaliser_wrap(y)



