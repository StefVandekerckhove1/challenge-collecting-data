def clean_data(df):
    df['Type of property']=df['Type of property'].fillna('House')
    df['Subtype of property']=df['Subtype of property'].fillna('None')
    df['Price']=df['Price'].fillna('None')
    df['Number of rooms']=df['Number of rooms'].fillna('None')
    df['Living Area']=df['Living Area'].fillna('None')
    df['Fully equipped kitchen']=df['Fully equipped kitchen'].fillna('None')
    df['Furnished']=df['Furnished'].fillna('None')
    df['Open fire']=df['Open fire'].fillna('None')
    df['Terrace']=df['Terrace'].fillna('None')
    df['Garden']=df['Garden'].fillna('None')
    df['Surface of the land']=df['Surface of the land'].fillna('None')
    df['Surface area of the plot of land']=df['Surface area of the plot of land'].fillna('None')
    df['Number of facades']=df['Number of facades'].fillna('None')
    df['Swimming pool']=df['Swimming pool'].fillna('None')
    df['State of the building']=df['State of the building'].fillna('None')
    df["Code Immoweb"]=df['Code Immoweb'].fillna('None')
    #Create a new column with the values of the Type of Sale
    # we keep here only values of tenement building
    df['Tenement building'] = df.loc[:, 'Type of Sale']

    df['Tenement building'] = df['Tenement building'].astype(str).str.strip().str.lower()

    df['Tenement building'] = df['Tenement building'].replace({'yes': 1, 'no': 0})


    df['Tenement building'] = df['Tenement building'].replace({
        "('under option', 'no')": 'None',
        "('under option', 'yes')": 'None',
        "('public sale', 'yes')": 'None',
        "('public sale', 'no')": 'None'
    })

    #In this one we keep only unde option/public sale
    df['Type of Sale']=df['Type of Sale'].astype(str).str.strip().str.lower()
    df['Type of Sale'] = df['Type of Sale'].replace({'yes': 'None', 'no': 'None'})

    df=df.drop_duplicates(subset=['Code Immoweb']).head()

    return df

