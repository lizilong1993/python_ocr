
@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
set /A num=0
FOR /F "tokens=*" %%i in ('dir /A-D /B /OD /TC') do (
 
   IF NOT "%%i"=="%~n0%~x0" (
        set /A num+=1
        if !num! LSS 10 (
            ren "%%i" "00000!num!%%~xi"
        ) else if !num! LSS 100 (
            ren "%%i" "0000!num!%%~xi"
        ) else if !num! LSS 1000 (
                    ren "%%i" "000!num!%%~xi"
        ) else if !num! LSS 10000 (
						ren "%%i" "00!num!%%~xi"
        ) else (
						ren "%%i" "0!num!%%~xi"
		)
    )
)
ENDLOCAL
exit