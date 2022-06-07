import pandas as pd

from constantes import main_dir

metadata = pd.read_csv(main_dir + '/datos/HAM10000_metadata')

label_map = {
    akiec: 0,
    bcc: 0, 
    bkl: 0, 
    df: 0, 
    mel: 1, 
    nv: 0, 
    vasc: 0
}
 
metadata["label"] = metadata["dx"].map(label_map)
