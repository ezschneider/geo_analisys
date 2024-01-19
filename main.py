from pathlib import Path
import requests
import matplotlib.pyplot as plt

from src.download import download_geo_file

LINK_TO_SP_GEO_LIMITS = 'https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/UFs/SP/SP_Municipios_2022.zip'
SAVE_SEP_GEO_LIMITS_PATH = 'data/SP_Municipios_2022.zip'

def main():
    # Make the download file
    download_geo_file(LINK_TO_SP_GEO_LIMITS, SAVE_SEP_GEO_LIMITS_PATH)
    # data_dir = Path('data')
    # geo_limits = data_dir / 'ES_Municipios_2022.shp'

    # gdf = read_from_shp(geo_limits)
    # gdf[gdf['NM_MUN'] == 'Vila Velha'].plot(figsize=(16,14), facecolor='white', edgecolor='black')
    # # gdf_without_islands = remove_right_islands(gdf[gdf['NM_MUN'] == 'Vila Velha'])

    # # gdf_without_islands.plot(figsize=(16,14), facecolor='white', edgecolor='black')
    # # gdf.plot(figsize=(16,14), facecolor='white', edgecolor='black')
    # # # Save the plot as an image
    # # plt.savefig('out/plot.png')

    # # Save the plot as an image
    # plt.savefig('out/vv_plot.png')

    data_dir = Path('data')
    geo_setors = data_dir / 'ES_Setores_2021.shp'

    gdf = read_from_shp(geo_setors)

    print(gdf['SIGLA_UF'].head())

    # gdf.plot()

    # plt.savefig('out/plot.png')


if __name__ == "__main__":
    main()
