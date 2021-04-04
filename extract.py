import pandas as pd
import numpy as np
import glob

from pandas.core.dtypes.missing import array_equivalent


def main():
    all_data = pd.DataFrame()
    for f in glob.glob("data/Xcelligence_031721_T47DM_13C3-A_ ADC_Export.xlsx"):
        df = pd.read_excel(f, 'Cell Index', header=[1]) # ,index_col=0, na_values=['NA'], header=[1], usecols="B:M"
        # print(df[df.columns[0]])
        # print(df[:8])
        df.dropna(inplace=True)

        all_data = all_data.append(df, ignore_index=True, sort=False)
        # print(all_data)
        
        all_data['1,2'] = all_data[[1, 2]].mean(axis=1)
        all_data['3,4'] = all_data[[3, 4]].mean(axis=1)
        all_data['5,6'] = all_data[[5, 6]].mean(axis=1)
        all_data['7,8'] = all_data[[7, 8]].mean(axis=1)
        all_data['9,10'] = all_data[[9, 10]].mean(axis=1)
        all_data['11,12'] = all_data[[11, 12]].mean(axis=1)

        # print(all_data.at['A', '11,12'])
        all_data.drop(columns=[1,2,3,4,5,6,7,8,9,10,11,12], inplace=True) 

        all_data.set_index(all_data.columns[0], inplace=True)

        # print(all_data[:25])

        writer = pd.ExcelWriter('data/output.xlsx')

        by_conc = all_data.groupby(level=0)
        for conc, frame in by_conc:                     
            frame.reset_index(inplace=True, drop=True)
            frame.index = frame.index.set_names(['Time(in hours)']) * 0.25
            
            print(f"All entries for {conc!r}")
            print("------------------------")
            print(frame, end="\n\n")        

            frame.to_excel(writer, conc, index=True)

    writer.save()


if __name__ == '__main__':
    main()
