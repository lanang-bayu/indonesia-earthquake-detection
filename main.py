"""
Earthquake Detection Scraping
Modularisasi dengan function
"""


def ekstraksi_data():
    """
    Tanggal : 15 November 2022
    Waktu : 18:02:36 WIB
    Magnitudo : 5.1
    Kedalaman : 49 km
    Lokasi LS=0.07 BT=124.38
    Pusat gempa : berada di laut 65 km Tenggara Bolaang Uki-Bolsel
    Dirasakan : II Bolaang Mongondow Selatan
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '15 November 2022'
    hasil['waktu'] = '18:02:36 WIB'
    hasil['magnitudo'] = '5.1'
    hasil['kedalaman'] = '49 km'
    hasil['lokasi'] = {'ls': 1.48, 'bt': 124.38}
    hasil['pusat_gempa'] = 'berada di laut 65 km Tenggara Bolaang Uki-Bolsel'
    hasil['dirasakan'] = 'II Bolaang Mongondow Selatan'

    return hasil


def tampilkan_date(result):
    print("Gempa terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa {result['pusat_gempa']}")
    print(f"Dirasakan {result['dirasakan']}")



if __name__ == '__main__':
    print('Main App')
    result = ekstraksi_data()
    tampilkan_date(result)

    
