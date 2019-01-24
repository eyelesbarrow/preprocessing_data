import os, re




word_list = 'filepath'
old_file = 'filepath'




dictionary ={}


	for line in open (word_list, 'r'): 
	    if not line.strip(): continue 
	    old_word, new_word = line.strip().split('=')                 
	    dictionary[old_word.strip()] = (new_word.strip())


	old_file = (filepath)


	for line in open(old_file, 'r'):

	    id = ''

	    if line:
	        line = line.strip()

	    if line:
	        if line.startswith('#'): 
	            if not id:
	                if ('id')in line:
	                    id = line[line.index('=') + 1]

	            continue   

	        if line.startswith(id):

	            split = line.split('\t')
	            if len(split) < 2: continue
	            print(split)

	            tag = split[2]
	            print(tag)

	            if tag != "O":
	                tag[:2]

	            tag_upper = tag[2:].upper()


	            if tag_upper in dictionary.keys():
	                new_tag = dictionary[tag_upper]
	                tag = new_tag
	                print(tag)
	            print(split)

	        if not line:
	            (newline)
	            id = -1

	path = ('filepath')
	folder = (path)



	for dirName, subdirList, fileList in os.walk(folder):
	        
	        for file in fileList:
	            print(file)
	        
	            if file.endswith('.tsv'):

	                #preprocess(files)
	        
	                file_name, file_ext = os.path.splitext(file)
	    

	            f = open(os.path.join(path, os.path.basename(file_name +('_processed') + '.tsv')) ,'w')
	            f.close()


