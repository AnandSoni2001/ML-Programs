import pandas as pd
df= pd.read_csv('sports.csv').values.tolist()
num_attri = 6
specific = ['Φ']*num_attri

for i in range(num_attri): 
  specific[i] = df[0][i]
print('Initial Specific Hypothesis : ', specific,'\n')

for i in range(len(df)):
  if df[i][num_attri]=='yes':
    print('\nAfter Example {} : {} \nSpecific Hypothesis : {}'.format(i+1, df[i], specific))
    for j in range(num_attri):
      if df[i][j]!=specific[j]: 
        specific[j]='?'
  else:
    print('\nAfter Example {} : {} \nSpecific Hypothesis : No Change'.format(i+1, df[i]))
print('\n\nFinal Specific :', specific)



"""
OUTPUT :


Initial Specific Hypothesis :  ['sunny', 'warm', 'normal', 'strong', 'warm', 'same'] 


After Example 1 : ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'] 
Specific Hypothesis : ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']

After Example 2 : ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'] 
Specific Hypothesis : ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']

After Example 3 : ['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'] 
Specific Hypothesis : No Change

After Example 4 : ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes'] 
Specific Hypothesis : ['sunny', 'warm', '?', 'strong', 'warm', 'same']


Final Specific : ['sunny', 'warm', '?', 'strong', '?', '?']

"""
print("End of Code")
