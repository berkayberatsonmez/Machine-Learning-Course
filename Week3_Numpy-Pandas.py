Numpy

#Task 1: Create a Linear Dataset

feature = np.arange(6, 21) 
print(feature)
label = (feature * 3) + 4   
print(label)

#Task 2: Add Some Noise to the Dataset

noise = (np.random.random([15]) * 4) - 2   
print(noise)
label =  label + noise 
print(label)


Pandas

#Task 1: Create a DataFrame

new_column_names = ['Eleanor', 'Chidi','Tahani','Jason']

new_data = np.random.randint(101,size=(3,4))

new_dataframe = pd.DataFrame(data=new_data, columns=new_column_names)

print(new_dataframe)

print(f"Eleanor data:\n{new_dataframe['Eleanor']}")

new_dataframe['Janet'] = new_dataframe['Tahani'] + new_dataframe['Jason']

print(new_dataframe)
