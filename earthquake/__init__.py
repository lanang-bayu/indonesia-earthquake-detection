import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        tglwaktu = soup.find('span', {'class': 'waktu'})
        tglwaktu = tglwaktu.text.split(', ')
        tanggal = tglwaktu[0]
        waktu = tglwaktu[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            #print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                kedalaman = res.text

            i = i + 1


        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['pusat_gempa'] = 'berada di laut 65 km Tenggara Bolaang Uki-Bolsel'
        hasil['dirasakan'] = 'II Bolaang Mongondow Selatan'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menampilkan data terkini')
        return
    print("Gempa terakhir berdasarkan BMKG")
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : LS = {result['koordinat']['ls']}, BT = {result['koordinat']['bt']}")
    print(f"Pusat Gempa : {result['pusat_gempa']}")
    print(f"Dirasakan {result['dirasakan']}")


