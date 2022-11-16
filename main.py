"""
Earthquake Detection Scraping
Modularisasi dengan function
"""
import earthquake

if __name__ == '__main__':
    print('Main App')
    result = earthquake.ekstraksi_data()
    earthquake.tampilkan_data(result)

    
