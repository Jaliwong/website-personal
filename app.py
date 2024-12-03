from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Data provinsi
provinsi_data = {
    'Aceh': {
        'ibu_kota': 'Banda Aceh',
        'suku': 'Aceh',
        'makanan_khas': 'Mie Aceh',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Aceh'
    },
    'Sumatera Utara': {
        'ibu_kota': 'Medan',
        'suku': 'Batak',
        'makanan_khas': 'Saksang',
        'baju': 'Baju Batak',
        'rumah_adat': 'Rumah Adat Batak'
    },
    'Sumatera Barat': {
        'ibu_kota': 'Padang',
        'suku': 'Minangkabau',
        'makanan_khas': 'Rendang',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Gadang'
    },
    'Riau': {
        'ibu_kota': 'Pekanbaru',
        'suku': 'Melayu',
        'makanan_khas': 'Nasi Lemak',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Melayu'
    },
    'Kepulauan Riau': {
        'ibu_kota': 'Tanjung Pinang',
        'suku': 'Melayu',
        'makanan_khas': 'Ikan Bakar',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Melayu'
    },
    'Jambi': {
        'ibu_kota': 'Jambi',
        'suku': 'Jambi',
        'makanan_khas': 'Gulai Ikan Patin',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Panggung'
    },
    'Sumatera Selatan': {
        'ibu_kota': 'Palembang',
        'suku': 'Palembang',
        'makanan_khas': 'Pempek',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Limas'
    },
    'Bengkulu': {
        'ibu_kota': 'Bengkulu',
        'suku': 'Rejang',
        'makanan_khas': 'Pendap',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Panggung'
    },
    'Lampung': {
        'ibu_kota': 'Bandar Lampung',
        'suku': 'Lampung',
        'makanan_khas': 'Seruit',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Adat Lampung'
    },
    'Bangka Belitung': {
        'ibu_kota': 'Pangkal Pinang',
        'suku': 'Melayu',
        'makanan_khas': 'Lempah Kuning',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Melayu'
    },
    'Banten': {
        'ibu_kota': 'Serang',
        'suku': 'Sunda',
        'makanan_khas': 'Sate Bandeng',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Banten'
    },
    'D.K.I Jakarta': {
        'ibu_kota': 'Jakarta',
        'suku': 'Betawi',
        'makanan_khas': 'Kerak Telor',
        'baju': 'Baju Betawi',
        'rumah_adat': 'Rumah Betawi'
    },
    'Jawa Barat': {
        'ibu_kota': 'Bandung',
        'suku': 'Sunda',
        'makanan_khas': 'Nasi Timbel',
        'baju': 'Kebaya',
        'rumah_adat': 'Rumah Sunda'
    },
    'Jawa Tengah': {
        'ibu_kota': 'Semarang',
        'suku': 'Jawa',
        'makanan_khas': 'Nasi Liwet',
        'baju': 'Kebaya',
        'rumah_adat': 'Joglo'
    },
    'D.I Yogyakarta': {
        'ibu_kota': 'Yogyakarta',
        'suku': 'Jawa',
        'makanan_khas': 'Gudeg',
        'baju': 'Kebaya',
        'rumah_adat': 'Joglo'
    },
    'Jawa Timur': {
        'ibu_kota': 'Surabaya',
        'suku': 'Jawa',
        'makanan_khas': 'Rawon',
        'baju': 'Kebaya',
        'rumah_adat': 'Joglo'
    },
    'Bali': {
        'ibu_kota': 'Denpasar',
        'suku': 'Bali',
        'makanan_khas': 'Bebek Betutu',
        'baju': 'Kebaya',
        'rumah_adat': 'Rumah Bali'
    },
    'Nusa Tenggara Barat': {
        'ibu_kota': 'Mataram',
        'suku': 'Sasak',
        'makanan_khas': 'Ayam Taliwang',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Adat Sasak'
    },
    'Nusa Tenggara Timur': {
        'ibu_kota': 'Kupang',
        'suku': 'Timor',
        'makanan_khas': 'Jagung Titi',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Adat Timor'
    },
    'Kalimantan Barat': {
        'ibu_kota': 'Pontianak',
        'suku': 'Dayak',
        'makanan_khas': 'Soto Pontianak',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Betang'
    },
    'Kalimantan Tengah': {
        'ibu_kota': 'Palangkaraya',
        'suku': 'Dayak',
        'makanan_khas': 'Ikan Bakar',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Betang'
    },
    'Kalimantan Selatan': {
        'ibu_kota': 'Banjarmasin',
        'suku': 'Banjar',
        'makanan_khas': 'Soto Banjar',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Banjar'
    },
    'Kalimantan Timur': {
        'ibu_kota': 'Samarinda',
        'suku': 'Dayak',
        'makanan_khas': 'Gence Ruan',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Lamin'
    },
    'Kalimantan Utara': {
        'ibu_kota': 'Tanjung Selor',
        'suku': 'Dayak',
        'makanan_khas': 'Nasi Kuning',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Betang'
    },
        'Gorontalo': {
        'ibu_kota': 'Gorontalo',
        'suku': 'Gorontalo',
        'makanan_khas': 'Binthe Biluhuta',
        'baju': 'Biliu dan Makuta',
        'rumah_adat': 'Dulohupa'
    },
        'Sulawesi Tengah': {
        'ibu_kota': 'Palu',
        'suku': 'Kaili',
        'makanan_khas': 'Kaledo',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Adat Kaili'
    },
    'Sulawesi Selatan': {
        'ibu_kota': 'Makassar',
        'suku': 'Bugis',
        'makanan_khas': 'Coto Makassar',
        'baju': 'Baju Kurung',
        'rumah_adat': 'Rumah Adat Bugis'
    },
    'Sulawesi Tenggara': {
        'ibu_kota': 'Kendari',
        'suku': 'Buton',
        'makanan_khas': 'Lapa-lapa',
        'baju': 'Baju Adat Buton',
        'rumah_adat': 'Rumah Adat Buton'
    },
    'Sulawesi Barat': {
        'ibu_kota': 'Mamuju',
        'suku': 'Mandar',
        'makanan_khas': 'Jepa',
        'baju': 'Baju Adat Mandar',
        'rumah_adat': 'Rumah Adat Mandar'
    },
    'Maluku': {
        'ibu_kota': 'Ambon',
        'suku': 'Maluku',
        'makanan_khas': 'Ikan Bakar Colo-Colo',
        'baju': 'Baju Cele',
        'rumah_adat': 'Baileo'
    },
    'Maluku Utara': {
        'ibu_kota': 'Sofifi',
        'suku': 'Ternate',
        'makanan_khas': 'Ikan Kuah Pala Banda',
        'baju': 'Baju Adat Ternate',
        'rumah_adat': 'Rumah Hibualamo'
    },
    'Papua': {
        'ibu_kota': 'Jayapura',
        'suku': 'Dani',
        'makanan_khas': 'Papeda',
        'baju': 'Koteka',
        'rumah_adat': 'Rumah Honai'
    },
    'Papua Barat': {
        'ibu_kota': 'Manokwari',
        'suku': 'Arfak',
        'makanan_khas': 'Ikan Kuah Kuning',
        'baju': 'Baju Adat Papua',
        'rumah_adat': 'Rumah Honai'
    },
    'Papua Tengah': {
        'ibu_kota': 'Nabire',
        'suku': 'Mee',
        'makanan_khas': 'Sate Ulat Sagu',
        'baju': 'Koteka',
        'rumah_adat': 'Rumah Honai'
    },
    'Papua Pegunungan': {
        'ibu_kota': 'Wamena',
        'suku': 'Lani',
        'makanan_khas': 'Ubi Tumbuk',
        'baju': 'Koteka',
        'rumah_adat': 'Rumah Honai'
    },
    'Papua Selatan': {
        'ibu_kota': 'Merauke',
        'suku': 'Marind',
        'makanan_khas': 'Sagu Sep',
        'baju': 'Baju Adat Papua',
        'rumah_adat': 'Rumah Honai'
    },
    'Papua Barat Daya': {
        'ibu_kota': 'Sorong',
        'suku': 'Moi',
        'makanan_khas': 'Papeda',
        'baju': 'Baju Adat Papua',
        'rumah_adat': 'Rumah Honai'
    }
}

def cari_data_provinsi(provinsi, detail=None):
    data = provinsi_data.get(provinsi.title(), None)
    if not data:
        return "Provinsi tidak ditemukan."
    if detail:
        detail_lower = detail.lower()
        if detail_lower in data:
            return f"{detail.capitalize()} dari {provinsi.title()} adalah {data[detail_lower]}"
        return f"{detail.capitalize()} tidak ditemukan untuk {provinsi.title()}"
    return data
def cari_provinsi_dari_detail(detail, nilai):
    for provinsi, data in provinsi_data.items():
        if data.get(detail.lower(), "").lower() == nilai.lower():
            return provinsi
    return f"{nilai.capitalize()} tidak ditemukan di data."
def tampilkan_semua():
    print("Daftar Provinsi dan Informasi di Indonesia:\n")
    for provinsi, data in provinsi_data.items():
        print(f"Provinsi: {provinsi}")
        print(f"  Ibu Kota       : {data['ibu_kota']}")
        print(f"  Suku           : {data['suku']}")
        print(f"  Makanan Khas   : {data['makanan_khas']}")
        print(f"  Baju Adat      : {data['baju']}")
        print(f"  Rumah Adat     : {data['rumah_adat']}\n")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_input = request.json.get('query', '').strip().lower()
    result = ""

    if user_input in ['keluar', 'exit', 'quit']:
        result = "Aplikasi dihentikan."

    elif 'ibu kota' in user_input:
        parts = user_input.split('ibu kota')
        if len(parts) > 1:
            provinsi = parts[1].replace('?', '').strip()
            data = cari_data_provinsi(provinsi)
            if isinstance(data, dict):
                result = f"Ibu kota {provinsi.title()} adalah {data['ibu_kota']}."
            else:
                result = data
        else:
            result = "Silakan sebutkan provinsi yang ingin Anda ketahui ibu kotanya."

    elif 'provinsi' in user_input:
        parts = user_input.split('provinsi')
        if len(parts) > 1:
            ibu_kota = parts[1].replace('?', '').strip()
            provinsi = cari_provinsi_dari_detail('ibu_kota', ibu_kota)
            result = f"Ibu kota {ibu_kota.title()} berada di provinsi {provinsi}."
        else:
            result = "Silakan sebutkan ibu kota yang ingin Anda ketahui provinsinya."

    elif 'makanan khas' in user_input:
        parts = user_input.split('makanan khas')
        if len(parts) > 1:
            provinsi = parts[1].replace('?', '').strip()
            data = cari_data_provinsi(provinsi)
            if isinstance(data, dict):
                result = f"Makanan khas {provinsi.title()} adalah {data['makanan_khas']}."
            else:
                result = data
        else:
            result = "Silakan sebutkan provinsi yang ingin Anda ketahui makanan khasnya."

    elif 'baju adat' in user_input or 'baju' in user_input:
        parts = user_input.split('baju adat')
        if len(parts) > 1:
            provinsi = parts[1].replace('?', '').strip()
            data = cari_data_provinsi(provinsi)
            if isinstance(data, dict):
                result = f"Baju adat {provinsi.title()} adalah {data['baju']}."
            else:
                result = data
        else:
            result = "Silakan sebutkan provinsi yang ingin Anda ketahui baju adatnya."

    elif 'suku' in user_input:
        parts = user_input.split('suku')
        if len(parts) > 1:
            provinsi = parts[1].replace('?', '').strip()
            data = cari_data_provinsi(provinsi)
            if isinstance(data, dict):
                result = f"Suku {provinsi.title()} adalah {data['suku']}."
            else:
                result = data
        else:
            result = "Silakan sebutkan provinsi yang ingin Anda ketahui sukunya."

    elif 'rumah adat' in user_input or 'rumah' in user_input:
        parts = user_input.split('rumah adat')
        if len(parts) > 1:
            provinsi = parts[1].replace('?', '').strip()
            data = cari_data_provinsi(provinsi)
            if isinstance(data, dict):
                result = f"Rumah adat {provinsi.title()} adalah {data['rumah_adat']}."
            else:
                result = data
        else:
            result = "Silakan sebutkan provinsi yang ingin Anda ketahui rumah adatnya."

    elif 'semua' in user_input:
        result = "Daftar lengkap data provinsi tidak dapat ditampilkan dalam satu respons."

    elif user_input.title() in provinsi_data:
        provinsi = user_input.title()
        data = cari_data_provinsi(provinsi)
        result = f"Data lengkap tentang {provinsi}:\n{data}"
    else:
        found = False
        for detail in ['ibu_kota', 'suku', 'makanan_khas', 'baju', 'rumah_adat']:
            for provinsi, data in provinsi_data.items():
                if user_input.lower() == data.get(detail, "").lower():
                    result = f"{user_input.capitalize()} berasal dari {provinsi}."
                    found = True
                    break
            if found:
                break
        if not found:
            result = "Data tidak ditemukan. Mohon periksa input Anda."

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)

