wt.exe --window 0 new-tab --startingDirectory "$(pwd)\itter_backend" --profile "PowerShell" PowerShell -noexit -file "..\run_backend.ps1"
wt.exe --window 0 new-tab --startingDirectory "$(pwd)" --profile "PowerShell" PowerShell -noexit -file ".\run_frontend.ps1"