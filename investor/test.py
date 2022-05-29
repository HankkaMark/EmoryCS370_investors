from yahoo_fin import stock_info
from alpha_vantage.sectorperformance import SectorPerformances

img=""
api_key = '6DYUFU9TTKWDXPZW'
sp = SectorPerformances(key=api_key, output_format='pandas')
data, meta_data = sp.get_sector()
sectors = data['Rank A: Real-Time Performance']

sectors = sectors.to_frame()

Health_Care = round(sectors.loc['Health Care', 'Rank A: Real-Time Performance'],5)

Utilities = round(sectors.loc['Utilities', 'Rank A: Real-Time Performance'], 5)

Materials = round(sectors.loc['Materials', 'Rank A: Real-Time Performance'],5)

Information_Technology = round(sectors.loc['Information Technology', 'Rank A: Real-Time Performance'],5)

Real_Estate = round(sectors.loc['Real Estate', 'Rank A: Real-Time Performance'],5)

Industrials = round(sectors.loc['Industrials', 'Rank A: Real-Time Performance'],5)

Financials = round(sectors.loc['Financials', 'Rank A: Real-Time Performance'],5)
Energy = round(sectors.loc['Energy', 'Rank A: Real-Time Performance'],5)

eight_data_sector = ['', f"Health_Care: {Health_Care}", f"Utilities: {Utilities}", f"Materials: {Materials}",
                f"Information_Technology: {Information_Technology}",
                f"Real_Estate: {Real_Estate}", f"Industrials: {Industrials}", f"Financials: {Financials}",
                f"Energy: {Energy}"]
print(eight_data_sector)