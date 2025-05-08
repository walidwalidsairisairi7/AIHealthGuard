import pandas as pd



def load_data(file_path):
 
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the dataset: {e}")
        return None
    

file_path = '../data/raw/Cancer_data.csv' 
df = load_data(file_path)


print(df.head()) ;  # Display the first 5 rows of the dataset
print(df.shape()) 