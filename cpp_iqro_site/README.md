# Iqro C++ High-Performance Web Backend

Ushbu papka **Iqro** loyihasi uchun to'liq **C++** tilida yozilgan backend web-serverni o'z ichiga oladi.

## Fayllar strukturasi

- `main.cpp` - Nativ HTTP/REST Web-server kodi (Winsock2 + Multi-threading asynchronous server).
- `CMakeLists.txt` - Loyihani kompiyatsya qilish uchun CMake sozlamalari.

## Serverni ishga tushirish (Kompilyatsiya va Komandalar)

### Windows (MSVC yoki MinGW):
```bash
g++ main.cpp -o server.exe -lws2_32 -std=c++17
./server.exe
```

Yoki CMake orqali:
```bash
mkdir build
cd build
cmake ..
cmake --build .
```

### Server API Yo'nalishlari (Endpoints):
- `http://localhost:8080/` - Server holati
- `http://localhost:8080/api/lessons` - Darslar ro'yxati (JSON)
- `http://localhost:8080/api/stats` - Statistik ma'lumotlar (JSON)
