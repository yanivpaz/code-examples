;print 0-9 code:
; GUI Turbo Assembler or TASM using DoxBox 
IDEAL
MODEL small
STACK 100h
DATASEG
userInputs db 1h
currentdl db 0h
savetime dw ?
divisorTable db 10,1,0
eoltxt db 13,10,'start : ','$'
;mov dx, offset eoltxt

CODESEG
proc printComma

push ax
push dx
mov ah,9

mov dl,2Ch
mov ah, 2h
int 21h

pop dx
pop ax 
ret
endp printComma
;--------------

proc printPeriod

push ax
push dx
mov ah,9

mov dl,2Eh
mov ah, 2h
int 21h

pop dx
pop ax 
ret
endp printPeriod
;--------------

proc printSpace
push ax
push dx
mov ah,9

mov dl,20h
mov ah, 2h
int 21h

pop dx
pop ax 
ret
endp printSpace
;------------------
proc printEOL

push ax
push dx
mov ah,9

mov dl,10
mov ah, 2h
int 21h

mov dl,13
mov ah, 2h
int 21h 
pop dx
pop ax 
ret
endp printEOL
;------------------
proc printCharacter
push ax
push bx
push dx
mov ah,2
mov dl, al
int 21h
pop dx
pop ax
pop bx
ret
endp printCharacter

;---------------------printNumberber start 
proc printNumber
 push ax
 push bx
 push dx
 mov bx,offset divisorTable
nextDigit :
 xor ah,ah
 div [byte ptr bx] ;al = quotient, ah = remainder
 add al,'0'
 call printCharacter ;Display the quotient
 mov al,ah ;ah = remainder
 add bx,1 ;bx = address of next divisor
 cmp [byte ptr bx],0 ;Have all divisors been done?
 jne nextDigit
 pop dx
 pop bx
 pop ax
 ret
endp printNumber

;---------------------Print MiliSec start 
proc printMiliSec
push ax
push dx

mov dx, [savetime]
mov al, dl
call printNumber
mov dx,[savetime]
mov al,dl
call printNumber
  
pop dx
pop ax 
ret
endp printMiliSec
;---------------------printSingleNumber start 
proc printSingleNumber
push ax
push dx
mov dl,userInputs
add dl, '0'
mov ah, 2h
int 21h
  
pop dx
pop ax 
ret
endp printSingleNumber
;---------------------printSingleNumber end 
start:
mov ax, @data
mov ds, ax


; loop to print 5 numbers 
loop3:
cmp userInputs, 5
ja exit 
mov bx, 0
call printEOL
call printSingleNumber
call printPeriod  
; loop to check if pass 0.055 ms
loop2:
call printMiliSec
call printComma
    loop1:
        ; call clock
        mov ah, 2Ch
        int 21h
        cmp al, dl
        mov [savetime],dx 
        ; call printPeriod       
        je loop1
; loop to check if 18 loops of 0.055 occured 
    mov al, dl
    inc bx
    cmp bx, 18
    jne loop2

inc userInputs
loop loop3



exit:
mov ax, 4c00h
int 21h
END start
