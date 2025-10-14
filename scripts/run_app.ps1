# scripts/run_app.ps1
# Ativa a venv, garante o diretório do projeto e executa o entrypoint

# Ativar venv
if (Test-Path .\.venv\Scripts\Activate.ps1) {
    .\.venv\Scripts\Activate.ps1
} else {
    Write-Host "Venv não encontrada. Execute: .\scripts\setup_venv.ps1"
    exit 1
}

# Ir para a raiz do projeto (pasta deste script -> ..)
Set-Location (Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path))

# Executar aplicação
python .\src\cap06_python_e_alem\main.py
