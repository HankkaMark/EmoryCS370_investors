
# Import packages that we will use
pip install alpha_vantage
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt



#Real time sector performance

def sector_performance():
    api_key = '6DYUFU9TTKWDXPZW'
    sp = SectorPerformances(key='api_key', output_format='pandas')
    data, meta_data = sp.get_sector()
    sectors=data['Rank A: Real-Time Performance']
    print(sectors.to_string())
    
    sectors.plot(kind='bar')
    plt.title('Real Time Performance per Sector')
    plt.tight_layout()
    plt.grid()
    plt.show()



sector_performance()






