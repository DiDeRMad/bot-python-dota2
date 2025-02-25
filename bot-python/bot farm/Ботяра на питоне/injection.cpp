#include <windows.h>
#include <tlhelp32.h>
#include <iostream>

DWORD GetProcessID(const char* processName) {
    DWORD processID = 0;
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    PROCESSENTRY32 pe;
    pe.dwSize = sizeof(PROCESSENTRY32);

    if (Process32First(hSnapshot, &pe)) {
        do {
            if (!strcmp(pe.szExeFile, processName)) {
                processID = pe.th32ProcessID;
                break;
            }
        } while (Process32Next(hSnapshot, &pe));
    }
    CloseHandle(hSnapshot);
    return processID;
}

bool InjectDLL(DWORD processID, const char* dllPath) {
    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, processID);
    if (!hProcess) return false;

    LPVOID dllAlloc = VirtualAllocEx(hProcess, NULL, strlen(dllPath) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
    WriteProcessMemory(hProcess, dllAlloc, dllPath, strlen(dllPath) + 1, NULL);

    HANDLE hThread = CreateRemoteThread(hProcess, NULL, 0, (LPTHREAD_START_ROUTINE)LoadLibraryA, dllAlloc, 0, NULL);
    if (!hThread) return false;

    CloseHandle(hThread);
    CloseHandle(hProcess);
    return true;
}

int main() {
    const char* dllPath = "C:\\hack\\cheat.dll";
    DWORD pid = GetProcessID("dota2.exe");

    if (pid) {
        if (InjectDLL(pid, dllPath)) {
            std::cout << "DLL успешно загружена!" << std::endl;
        } else {
            std::cout << "Ошибка при загрузке DLL." << std::endl;
        }
    } else {
        std::cout << "Dota 2 не найдена!" << std::endl;
    }
    return 0;
}