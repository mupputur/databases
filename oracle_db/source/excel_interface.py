import pandas as pd

def write_exel(data_dict, filename):
    df = pd.DataFrame(data_dict)
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()

if __name__ == "__main__":

    rows = [(101, 'Ravi'), (102, 'Mavi'), (103, 'Pavi')]
    cols = list(map(list, zip(*rows)))
    heders = ["id", "name","number"]
    record = dict(zip(heders, cols))
    write_exel(record, 'output.xlsx')


