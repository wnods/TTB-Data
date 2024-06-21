#
# -------------- Reads a CSV file ----------------------------
#
def ipcsv(file):
    """
Reads a CSV file with up to 10 columns
<I/P>
file ------> A file name
<O/P>
dicy ------> A dictionary with the data fields as keys.
              It may have just one key
    """
#------------ Set initial state --------------
    values = []
    dicy   = {}
#------------ Reads file --------------
    with open(file, "r") as df:
        df = csv.reader(df, delimiter=',')
#------------ Iterate over rows --------------
        for item in df:
#------ Remove nans and blanks of line
            entry = [item for item in item if str(item) != 'nan']
#------ Header line: ##, header
            if entry[0] == '##': continue
#------------ A new data field: #, field name, ...            
            if  entry[0] == '#':
                entry[1] =  entry[1].strip()
                if entry[1] != 'EOF':
                    entry[2] = [entry[2].strip() if len(entry) <= 3
                                else ' '.join(map(str, entry[2:])).strip()]
#------------ Save data to dictionary dicy
                if bool(dicy):
#------------ Save it!
                    values = [dummy for dummy in values]
                    dummy  = np.array(values, dtype=float)
                    dummy  = np.reshape(dummy, (-1, n_cols)) if dummy.size > n_cols else dummy
                    dicy[str(key)] = np.array(dummy, dtype=float)
#                             └──> last key
                    if    entry[1] == 'EOF': break
                    key = entry[1]
                    dicy['hdr'] = dicy.get('hdr') + [entry[1], entry[2]]
                    values = []
                else:
#------------ 1st pass
                    key = str(entry[1])
                    dicy[key] = 0
                    dummy = [entry[1], entry[2]]

                    if dicy.get('hdr') is not None:
                        dicy['hdr'] = dicy.get('hdr') + dummy
                    else:
                        dicy['hdr'] = dummy
#------------ Write data to list "values"
            else:
                if len(values) == 0:
#------------ A new list begins
                    values = entry.copy()
                    n_cols = len(entry)
                else:
#------------ Append to the end
                    values.extend(entry)
#------------ Returns dictionary
    return dicy
#
# -------------- End of function   -------------------
