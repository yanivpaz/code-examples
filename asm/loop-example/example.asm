;print 0-9 code:
IDEAL
MODEL small
STACK 100h
DATASEG
counter db 1h
currentdl db 0h

CODESEG
;---------------------printNum start 
proc printMiliSec
push ax
push dx
mov dl,currentdl
mov ah, 2h
int 21h
  
pop dx
pop ax 
ret
endp printMiliSec
;---------------------printNum end 

;---------------------printNum start 
proc printNum
push ax
push dx
mov dl,counter
add dl, '0'
mov ah, 2h
int 21h
  
pop dx
pop ax 
ret
endp printNum
;---------------------printNum end 
start:
mov ax, @data
mov ds, ax

; call clock
mov ah, 2Ch
int 21h
mov al, dl ;1/100=hundredths
mov cx, 0


; loop to print 10 numbers 
loop3:
mov bx, 0

cmp counter, 5
ja exit 

call printNum
; loop to check if pass 0.055 ms
loop2:
    loop1:
        int 21h
        cmp al, dl
        mov currentdl,dl
        call printMiliSec
        je loop1

; loop to check if 18 loops of 0.055 occured 
    mov al, dl
    inc bx
    cmp bx, 18
    jne loop2
inc counter
loop loop3



exit:
mov ax, 4c00h
int 21h
END start
