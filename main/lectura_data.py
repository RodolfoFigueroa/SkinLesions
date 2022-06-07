import pandas as pd

from constantes import main_dir

metadata = pd.read_csv(main_dir + '/datos/HAM10000_metadata')

label_map = {
    akiec: 0,
    bcc: 1, 
    bkl: 2, 
    df: 3, 
    mel: 4, 
    nv: 5, 
    vasc: 6
}
 
metadata["label"] = metadata["dx"].map(label_map)
