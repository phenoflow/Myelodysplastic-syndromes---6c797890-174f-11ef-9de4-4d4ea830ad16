# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"BBmA.00","system":"readv2"},{"code":"B937911","system":"readv2"},{"code":"BBmL.00","system":"readv2"},{"code":"ByuHD00","system":"readv2"},{"code":"7Q09700","system":"readv2"},{"code":"B937W00","system":"readv2"},{"code":"B937W11","system":"readv2"},{"code":"B937.14","system":"readv2"},{"code":"B937800","system":"readv2"},{"code":"45143.0","system":"readv2"},{"code":"56756.0","system":"readv2"},{"code":"45285.0","system":"readv2"},{"code":"14927.0","system":"readv2"},{"code":"104740.0","system":"readv2"},{"code":"16052.0","system":"readv2"},{"code":"105985.0","system":"readv2"},{"code":"19130.0","system":"readv2"},{"code":"105390.0","system":"readv2"},{"code":"60186.0","system":"readv2"},{"code":"44420.0","system":"readv2"},{"code":"106993.0","system":"readv2"},{"code":"7799.0","system":"readv2"},{"code":"105915.0","system":"readv2"},{"code":"22890.0","system":"readv2"},{"code":"102712.0","system":"readv2"},{"code":"94921.0","system":"readv2"},{"code":"4561.0","system":"readv2"},{"code":"23875.0","system":"readv2"},{"code":"10817.0","system":"readv2"},{"code":"D46","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('myelodysplastic-syndromes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["myelodysplastic-syndromes-myelodysplasia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["myelodysplastic-syndromes-myelodysplasia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["myelodysplastic-syndromes-myelodysplasia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
