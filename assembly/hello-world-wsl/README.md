# Hello world assembly With WSL 
## code example 
```
nasm -f elf64 hello.asm -o hello.o; ld -o hello hello.o -m elf_x86_64 ; ./hello
```
## note 
[ WSL1 is not supporting 32 bit](https://github.com/microsoft/WSL/issues/2468)

