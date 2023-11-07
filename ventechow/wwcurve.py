# wwcurve.py
# created by cubicles

# The WES weir curve is a set of curves comparing 'He/Hd' and 'h/Hd' to obtain
# the value of the x axis

import pandas as pd
import joblib

def wwcurve(He_Hd, h_Hd):
    ''' wwcurve
        -------
        The WES weir curve is a set of curves comparing 'He/Hd' and 'h/Hd' to
        obtain the value of the x axis
            usage:
            x = wwcurve(He/Hd, h/Hd)
    '''
    sample_df =  pd.DataFrame({
                          'He_Hd': [He_Hd],  # He/Hd 
                          'h_Hd': [h_Hd],    # h/Hd
                             })

    vtmodel = joblib.load('../model.pkl')
    return vtmodel.predict(sample_df)

def little_wwcurve_test():
    print(wwcurve(1.1, 0.2))

# if __name__ == '__main__':
#     little_wwcurve_test()




