format ELF executable

segment readable executable

start:
mov eax, 4
mov ebx, 1
mov ecx, hello_msg
mov edx, hello_size
int 80h

mov eax, 1
mov ebx, 0
int 80h

segment readable writeable

hello_msg db "Hello World!",10,0
hello_size = $-hello_msg
