#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include <sstream>
#include <map>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

const int PORT = 8080;

std::string get_lessons_json() {
    return R"([
        {"id": 1, "title": "1-Dars: Alif, Bo, To, So", "audio": "/static/audio/lesson1.mp3", "description": "Harflarning talaffuzi va yozilish shakllari."},
        {"id": 2, "title": "2-Dars: Jim, Ho, Xo", "audio": "/static/audio/lesson2.mp3", "description": "Tomoqdan chiquvchi harflar mashqi."},
        {"id": 3, "title": "3-Dars: Dal, Zal, Ro, Za", "audio": "/static/audio/lesson3.mp3", "description": "Qattiq va yumshoq harflar farqi."},
        {"id": 4, "title": "4-Dars: Sin, Shin, Sod, Zod", "audio": "/static/audio/lesson4.mp3", "description": "Husnixat va to'g'ri o'qish qoidalari."}
    ])";
}

std::string get_stats_json() {
    return R"({
        "total_users": 1250,
        "completed_lessons": 8400,
        "active_today": 320,
        "status": "online"
    })";
}

void handle_client(SOCKET client_socket) {
    char buffer[4096];
    int bytes_received = recv(client_socket, buffer, sizeof(buffer) - 1, 0);
    
    if (bytes_received <= 0) {
        closesocket(client_socket);
        return;
    }

    buffer[bytes_received] = '\0';
    std::string request(buffer);
    std::istringstream stream(request);
    std::string method, path, protocol;
    stream >> method >> path >> protocol;

    std::cout << "[C++ Web Server] " << method << " " << path << std::endl;

    std::string response_body;
    std::string content_type = "application/json";
    std::string status_line = "HTTP/1.1 200 OK";

    if (path == "/" || path == "/api/status") {
        response_body = R"({"message": "Iqro C++ High-Performance Backend Web Server Operational", "server": "C++ Native Winsock Server", "status": "active"})";
    } else if (path == "/api/lessons") {
        response_body = get_lessons_json();
    } else if (path == "/api/stats") {
        response_body = get_stats_json();
    } else {
        status_line = "HTTP/1.1 404 Not Found";
        response_body = R"({"error": "Endpoint Not Found", "code": 404})";
    }

    std::ostringstream http_response;
    http_response << status_line << "\r\n"
                  << "Content-Type: " << content_type << "\r\n"
                  << "Access-Control-Allow-Origin: *\r\n"
                  << "Content-Length: " << response_body.size() << "\r\n"
                  << "Connection: close\r\n\r\n"
                  << response_body;

    std::string full_response = http_response.str();
    send(client_socket, full_response.c_str(), full_response.size(), 0);
    closesocket(client_socket);
}

int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup bajarilmadi!" << std::endl;
        return 1;
    }

    SOCKET listen_socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (listen_socket == INVALID_SOCKET) {
        std::cerr << "Soket yaratishda xatolik: " << WSAGetLastError() << std::endl;
        WSACleanup();
        return 1;
    }

    sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(listen_socket, (sockaddr*)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
        std::cerr << "Portga ulanishda xatolik (" << PORT << "): " << WSAGetLastError() << std::endl;
        closesocket(listen_socket);
        WSACleanup();
        return 1;
    }

    if (listen(listen_socket, SOMAXCONN) == SOCKET_ERROR) {
        std::cerr << "Tinglashda xatolik: " << WSAGetLastError() << std::endl;
        closesocket(listen_socket);
        WSACleanup();
        return 1;
    }

    std::cout << "====================================================" << std::endl;
    std::cout << "  Iqro C++ High-Performance Web Server ishga tushdi!" << std::endl;
    std::cout << "  Port: http://localhost:" << PORT << std::endl;
    std::cout << "====================================================" << std::endl;

    while (true) {
        SOCKET client_socket = accept(listen_socket, NULL, NULL);
        if (client_socket != INVALID_SOCKET) {
            std::thread(handle_client, client_socket).detach();
        }
    }

    closesocket(listen_socket);
    WSACleanup();
    return 0;
}
