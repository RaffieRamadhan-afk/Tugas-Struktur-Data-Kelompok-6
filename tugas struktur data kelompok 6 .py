def main():
    menu_kantin = {
        "Nasi Goreng": 15000,
        "Mie Ayam": 12000,
        "Es Teh": 5000,
        "Kopi": 7000
    }

    keranjang_belanja = []

    print("=== SELAMAT DATANG DI KANTIN TUAN UBE ===")
    print("Menu tersedia hari ini:")
    for makanan, harga in menu_kantin.items():
        print(f"- {makanan}: Rp{harga}")

    while True:
        pilihan = input("\nMasukkan nama menu (atau ketik 'bayar'): ")
        
        if pilihan.lower() == 'bayar':
            break
        
        if pilihan in menu_kantin:
            keranjang_belanja.append(pilihan) 
            print(f"✓ {pilihan} berhasil ditambah ke keranjang.")
        else:
            print("❌ Maaf, menu tersebut tidak ada.")

    total_bayar = 0
    print("\n=== STRUK PEMBAYARAN ===")
    for item in keranjang_belanja:
        harga_item = menu_kantin[item]
        total_bayar += harga_item
        print(f"- {item}: Rp{harga_item}")
    
    print(f"\nTOTAL YANG HARUS DIBAYAR: Rp{total_bayar}")
    print("==========================")

if __name__ == "__main__":
    main()