import pandas as pd
import glob

def main():
    all_data = pd.DataFrame()
    for f in glob.glob("data/ADC/20220307_T47DM_Levana_QC_Export.xlsx"):
        file_name = f.rsplit('/', 1)[1]
        df = pd.read_excel(f, 'Cell Index', header=[1]) # ,index_col=0, na_values=['NA'], header=[1], usecols="B:M"
        # print(df[:10])
        # print(df[df.columns[0]][:22])

        contain_values = df[df[df.columns[0]].astype(str).str.contains('Cell Index at:')].iloc[:, 0]
        # print(contain_values[:1])   
        initial_time = pd.Series(['0:00:00'])
        # contain_values = initial_time.append(contain_values, ignore_index=True)
        contain_values = pd.concat([initial_time, contain_values], ignore_index=True)
        contain_values = contain_values.str.split('at:').str[-1]

        # print(contain_values)

        # new time frame with split HH:MM:SS value columns
        total_time = contain_values.str.split(":", n = 2, expand = True)
        # print(total_time)

        # new total hours
        contain_values = total_time[0].astype(int) + total_time[1].astype(int)/60 + total_time[2].astype(int)/3600

        # print(contain_values)
        
        df.dropna(inplace=True)
        # print(df[:12])

        # all_data = all_data.append(df, ignore_index=True, sort=False)
        all_data = pd.concat([df, all_data], ignore_index=True, sort=False)        
        # print(all_data)
        
        # all_data['1,2'] = all_data[[1, 2]].mean(axis=1)
        # all_data['3,4'] = all_data[[3, 4]].mean(axis=1)
        # all_data['5,6'] = all_data[[5, 6]].mean(axis=1)
        # all_data['7,8'] = all_data[[7, 8]].mean(axis=1)
        # all_data['9,10'] = all_data[[9, 10]].mean(axis=1)
        # all_data['11,12'] = all_data[[11, 12]].mean(axis=1)

        # print(all_data.at['A', '11,12'])
        # all_data.drop(columns=[1,2,3,4,5,6,7,8,9,10,11,12], inplace=True) 

        all_data.set_index(all_data.columns[0], inplace=True)
        # print(all_data[:25])

        writer = pd.ExcelWriter('output/output_for_' + file_name)

        by_conc = all_data.groupby(level=0)
        # print(by_conc)
   
        for conc, frame in by_conc:          
            frame.reset_index(inplace=True, drop=True)
            frame.insert(0, 'Time(in hours)', contain_values)
            frame.index = frame['Time(in hours)']
            frame.drop(columns =['Time(in hours)'], inplace = True)

            # frame.index = frame.index.set_names(['Time(in hours)']) * 0.25
            
            print(f"All entries for {conc!r}")
            print("------------------------")
            print(frame, end="\n\n")        

            frame.to_excel(writer, conc, index=True)

    writer.save()


if __name__ == '__main__':
    main()
