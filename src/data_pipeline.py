import pandas as pd

def extract(file_path):
    df = pd.read_csv(file_path)
    return df

def transform(df):
    # clean column names first
    df.columns = df.columns.str.lower().str.strip()

    # convert salary safely
    if 'salary' in df.columns:
        df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
        df['salary'] = df['salary'].fillna(df['salary'].mean())

    # handle other numeric columns safely (optional but good)
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    # drop after cleaning (NOT before)
    df = df.dropna()

    return df

def load(df, output_path):
    df.to_csv(output_path, index=False)

def run_pipeline():
    raw_data_path = r"C:/Users/Sharath/Desktop/DataScience Intern/week3task5/data/raw_data.csv"
    output_path = r"C:/Users/Sharath/Desktop/DataScience Intern/week3task5/data/cleaned_data.csv"
    
    df = extract(raw_data_path)
    df = transform(df)
    load(df, output_path)
    
    print("Pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()
